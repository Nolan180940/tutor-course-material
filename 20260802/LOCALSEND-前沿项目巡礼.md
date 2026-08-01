# LOCALSEND — 前沿项目巡礼

> 调研对象：[`localsend/localsend`](https://github.com/localsend/localsend)
> 调研时分支与版本：`main` 分支，最新提交 `da4464d` "feat: path sanitizing in core"（提交于调研时 2 小时前），应用版本 `1.17.0+58`（见 [`app/pubspec.yaml`](https://github.com/localsend/localsend/blob/main/app/pubspec.yaml)），Rust 协议核心从 v2.0 演进至 v2.1（多播消息版本字段 `PROTOCOL_VERSION_V2`）
> 调研时间：2026-08-02
> 文档定位：系统性技术巡礼，结合源码路径与关键代码片段，覆盖项目定位、架构、目录结构、核心功能原理、技术栈、关键文件解析、扩展与配置、安全设计、源码阅读建议等八个维度

---

## 1. 项目定位与核心架构

### 1.1 项目目标

LocalSend 是 GitHub 上最受欢迎的"开源版 AirDrop"——一款 **完全运行于本地网络、无需互联网连接** 的跨平台文件与消息传输工具。其官方定位声明见 [`README.md#L20-L23`](https://github.com/localsend/localsend/blob/main/README.md#L20-L23)：

> "LocalSend is a free, open-source app that allows you to securely share files and messages with nearby devices over your local network without needing an internet connection."

核心能力可概括为：
- **跨平台**：Android 5.0+ / iOS 12.0+ / macOS 11+ / Windows 10+ / Linux（依赖 `xdg-desktop-portal`），并提供独立的 Web 下载入口
- **零依赖**：不依赖任何外部服务器、账号、互联网连接，所有握手与传输发生在局域网内
- **协议开放**：遵循 [`localsend/protocol`](https://github.com/localsend/protocol) 规范，使用自签证书 + mTLS + REST + 可选 WebRTC
- **多元化发行**：除官网外，已上架 Winget/App Store/Flathub/Play Store/Scoop/Homebrew/Nixpkgs/F-Droid/Chocolatey/Snap/AUR 等 20+ 渠道

### 1.2 整体架构模式

项目 **不是** 传统纯 Flutter 项目，而是一个 **多语言 monorepo**（详见 [`AGENTS.md#L12-L25`](https://github.com/localsend/localsend/blob/main/AGENTS.md#L12-L25)）：

| 路径 | 职责 |
|---|---|
| `app/` | Flutter 应用（`localsend_app`）。负责 UI、Provider 状态管理、持久化、平台通道 |
| `packages/localsend_isolates/` | Dart isolate 层 + `flutter_rust_bridge`（FRB）绑定。包含 `rust/`（Flutter 插件 crate `rust_lib_localsend_app`）与 `rust_builder/`（cargokit） |
| `packages/core/` | 纯 Rust crate `localsend`：协议、HTTP 服务端/客户端、加密、WebRTC。**无任何 Flutter 依赖** |
| `packages/typed_isolates/` | 极简封装，为 Dart `Isolate` 提供类型化通道 |
| `server/` | Axum WebSocket 信令服务器（`/v1/ws`），用于 WebRTC P2P 通道建立，独立部署 |
| `cli/` | Rust CLI（`localsend-cli`），复用 `packages/core` |
| `support/scripts/` | 发布/打包脚本（MSIX、Inno Setup、FOSS 剥离等） |

依赖方向严格单向：

```
app  →  localsend_isolates  →  (typed_isolates, rust_lib_localsend_app  →  localsend core)
```

> App **只依赖** `localsend_isolates`，不直接接触 `flutter_rust_bridge`、`typed_isolates` 或 Rust 插件 crate。

### 1.3 关键设计原则

- **网络栈不在主 isolate**——`packages/localsend_isolates/lib/src/isolate/` 为 HTTP 扫描、组播发现、HTTP 上传、HTTP 服务端各开一个 child isolate，UI 线程始终保持流畅
- **核心故意不提供 `auto_accept`**——是否自动接收由应用层决定，Core 只发 `decision_tx` oneshot
- **TLS 强制 mTLS + 一次性自签证书**——peer 身份即客户端证书 DER 的 SHA-256
- **多语言占比**（GitHub 统计）：Dart **79.7%**、Rust **17.2%**、C++/Kotlin/Swift/CMake 共约 2.6%

---

## 2. 目录结构与模块职责

### 2.1 顶层一级目录

| 目录 | 作用 |
|---|---|
| `app/` | Flutter 项目根（`pubspec.yaml`、`lib/`、`assets/`、`test/`、`android/`、`ios/`、`macos/`、`windows/`、`linux/`、`web/`） |
| `packages/` | 多 package 工作区，含 `core/`（Rust）、`localsend_isolates/`（Dart+FRB）、`typed_isolates/` |
| `server/` | 独立的 Rust WebSocket 信令服务器（用于 WebRTC SDP 交换） |
| `cli/` | Rust 命令行客户端 |
| `support/` | 多语言 README 翻译（`readme/README_*.md`）、脚本、文档（含 `docs/dependency-hierarchy.svg`） |
| `fastlane/metadata/` | Play Store / F-Droid 上架元数据 |
| `.github/` | CI workflow、PR 模板、Issue 模板 |
| `linux/`、`android/`、`ios/`、`windows/`、`macos/`、`web/` | 平台原生工程（由 `flutter create` 生成，置于 `app/` 内对应子目录） |

### 2.2 `app/lib/` 核心目录（Flutter 端）

调研时 [`app/lib`](https://github.com/localsend/localsend/tree/main/app/lib) 含 7 个子目录 + `main.dart`：

| 子目录 | 关键内容与职责 |
|---|---|
| [`app/lib/config/`](https://github.com/localsend/localsend/tree/main/app/lib/config) | 应用初始化入口：`init.dart::preInit()`（初始化 logging、`RustLib.init()`、持久化、isolate 容器、tray/window，返回 `RefenaContainer`），`init_error.dart`（启动失败兜底 UI），`theme.dart`（深浅色 & 动态颜色），`refena.dart`（Provider 容器配置） |
| [`app/lib/gen/`](https://github.com/localsend/localsend/tree/main/app/lib/gen) | Slang 国际化代码生成输出（**不要手编辑**）。每个 locale 一个 `.g.dart`（如 `strings_zh_CN.g.dart`） |
| [`app/lib/model/`](https://github.com/localsend/localsend/tree/main/app/lib/model) | Dart 端 DTO 与领域模型（`@MappableClass`）：如 `cross_file.dart`、`persistence/color_mode.dart` |
| [`app/lib/pages/`](https://github.com/localsend/localsend/tree/main/app/lib/pages) | 路由级页面：`home_page.dart`（`HomeTab.send / receive / settings`）、`about/`、`debug/debug_page.dart`（含便携模式、设置路径、平台版本等调试面板）、`donation/`（FOSS 构建剥离） |
| [`app/lib/provider/`](https://github.com/localsend/localsend/tree/main/app/lib/provider) | Refena 状态层：`NotifierProvider` 处理纯状态、`ReduxProvider` + Action 类处理 isolate 交互。`network/` 下含 `server/server_provider.dart`、`webrtc/signaling_provider.dart`、`nearby_devices_provider.dart` 等 |
| [`app/lib/util/`](https://github.com/localsend/localsend/tree/main/app/lib/util) | 平台无关工具：UI helpers、`native/`（平台通道调用：android_channel.dart 调用 `org.localsend.localsend_app/localsend` MethodChannel 处理 SAF content URI） |
| [`app/lib/widget/`](https://github.com/localsend/localsend/tree/main/app/lib/widget) | 自定义 widgets：`watcher/`（`tray_watcher`、`window_watcher`、`life_cycle_watcher`、`shortcut_watcher`）、`local_send_logo.dart`、各种对话框与列表组件 |

#### 启动流程（[`app/lib/main.dart`](https://github.com/localsend/localsend/blob/main/app/lib/main.dart#L19-L57)）

```dart
Future<void> main(List<String> args) async {
  final RefenaContainer container;
  try {
    container = await preInit(args);    // ← 1. 初始化
  } catch (e, stackTrace) {
    showInitErrorApp(error: e, stackTrace: stackTrace);
    return;
  }

  runApp(
    RefenaScope.withContainer(         // ← 2. 挂载 Provider 容器
      container: container,
      child: TranslationProvider(
        child: const LocalSendApp(),    // ← 3. 进入 MaterialApp
      ),
    ),
  );
}
```

`preInit(args)` 内（[`app/lib/config/init.dart#L39-L58`](https://github.com/localsend/localsend/blob/main/app/lib/config/init.dart#L39-L58)）依次完成：
1. `WidgetsFlutterBinding.ensureInitialized()`
2. 初始化 `logging`、`RustLib.init()`、`IsolateSetupAction`
3. 注入 `nearby_devices_provider`、`server_provider`、`signaling_provider`、`purchase_provider`（被 `[FOSS_REMOVE]` 标记包住的非自由代码段）
4. 创建 `RefenaContainer` 并返回给 `main`

> 注意：用户消息中提到的 `app/lib/services/transfer_service.dart`、`app/lib/services/http_server.dart`、`app/lib/services/discovery_service.dart` 在当前 `main` 分支 **已不存在**。它们在 2025 年底的"split project"重构（commit "feat: split project into app, common, cli"）与最近的"refactor: move to packages/localsend_isolates"迁移中，转移到了 Rust 核心 `packages/core/src/` 与 Dart isolate 层 `packages/localsend_isolates/lib/src/task/`。

### 2.3 `packages/core/src/` 核心子目录（Rust 端）

| 子目录 | 职责 |
|---|---|
| [`packages/core/src/crypto/`](https://github.com/localsend/localsend/tree/main/packages/core/src/crypto) | `cert.rs`（自签证书生成）、`token.rs`（签名/校验 token key，用于 WebRTC 文件 token）、`hash.rs`（SHA-256） |
| [`packages/core/src/discovery/`](https://github.com/localsend/localsend/tree/main/packages/core/src/discovery) | `mod.rs`（`DiscoveryHandle`、`DiscoveryConfig`）+ `store.rs`（设备存储：HTTP / Signaling / WebRTC 三类通道） |
| [`packages/core/src/http/`](https://github.com/localsend/localsend/tree/main/packages/core/src/http) | `server/`（v2 协议、web 下载、internal `show`）+ `client/` + `dto.rs`、`dto_v2.rs`、`state.rs`、`mod.rs` |
| [`packages/core/src/model/`](https://github.com/localsend/localsend/tree/main/packages/core/src/model) | `transfer.rs`（`FileDto`、`FileMetadata`、`FileContent`、`FileUploadTarget`）、`discovery.rs`（`MulticastMessageV2`）、`version.rs` |
| [`packages/core/src/multicast/`](https://github.com/localsend/localsend/tree/main/packages/core/src/multicast) | `mod.rs`（`MulticastHandle`、`MulticastConfig`）、`socket.rs`（按接口绑定 UDP socket）、`interface.rs`（接口枚举与过滤） |
| [`packages/core/src/util/`](https://github.com/localsend/localsend/tree/main/packages/core/src/util) | 通用工具（base64 等） |
| [`packages/core/src/webrtc/`](https://github.com/localsend/localsend/tree/main/packages/core/src/webrtc) | `webrtc.rs`（P2P 数据通道 + 文件 token 流控）、`signaling.rs`（信令客户端封装 `ManagedSignalingConnection`） |
| [`packages/core/src/lib.rs`](https://github.com/localsend/localsend/blob/main/packages/core/src/lib.rs) | 顶层 `lib.rs`，按 `crypto` / `discovery` / `http` / `multicast` / `webrtc` 特性开关模块导出 |

---

## 3. 核心功能实现原理

### 3.1 发现机制（UDP 组播 + HTTP 注册双向握手）

LocalSend 的设备发现采用 **"UDP 宣布 + HTTP 注册"** 模式，绝不依赖中心服务器，源码集中在 [`packages/core/src/multicast/`](https://github.com/localsend/localsend/tree/main/packages/core/src/multicast) 与 [`packages/core/src/discovery/`](https://github.com/localsend/localsend/tree/main/packages/core/src/discovery)。

#### 常量定义（[`packages/core/src/multicast/mod.rs#L25-L44`](https://github.com/localsend/localsend/blob/main/packages/core/src/multicast/mod.rs#L25-L44)）

```rust
/// 224.0.0.0/24 在某些 Android 设备上是唯一能接收 UDP 组播的网段
pub const DEFAULT_MULTICAST_GROUP: Ipv4Addr = Ipv4Addr::new(224, 0, 0, 167);

/// IPv6 组播组，LocalSend 扩展（v2.1 协议）
pub const DEFAULT_MULTICAST_GROUP_V6: Ipv6Addr =
    Ipv6Addr::new(0xff12, 0, 0, 0, 0, 0, 0xfd3a, 0xe420);

/// 与默认 HTTP 端口相同
pub const DEFAULT_PORT: u16 = 53317;
```

#### 多播消息格式（[`packages/core/src/model/discovery.rs#L78-L110`](https://github.com/localsend/localsend/blob/main/packages/core/src/model/discovery.rs#L78-L110)）

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct MulticastMessageV2 {
    pub alias: String,                  // 显示名
    pub version: String,                // 协议版本
    pub device_model: Option<String>,   // "Samsung" / "Windows" 等
    pub device_type: Option<DeviceType>,// mobile/desktop/web/headless/server
    pub fingerprint: String,            // HTTPS 下为证书 SHA-256
    pub port: u16,                      // HTTP 服务端端口
    pub protocol: ProtocolTypeV2,       // http 或 https
    #[serde(default)]
    pub download: bool,                 // 是否启用 web 下载 API
}
```

#### 关键设计要点（[`packages/core/src/multicast/socket.rs#L109-L122`](https://github.com/localsend/localsend/blob/main/packages/core/src/multicast/socket.rs#L109-L122)）

```rust
fn bind_multicast_socket_v4(...) -> std::io::Result<UdpSocket> {
    // 每个接口绑一个 socket，否则单 socket 只能从一个接口发包
    socket.set_multicast_if_v4(&interface)?;

    // 同主机多实例需开启回环；自身消息按 fingerprint 过滤
    socket.set_multicast_loop_v4(true)?;

    // 仅本地子网，TTL=1
    socket.set_multicast_ttl_v4(1)?;

    socket.set_nonblocking(true)?;
    UdpSocket::from_std(socket.into())
}
```

`MulticastHandle::announce()`（[`packages/core/src/multicast/mod.rs#L213-L230`](https://github.com/localsend/localsend/blob/main/packages/core/src/multicast/mod.rs#L213-L230)）按固定时序发送一组（burst）多播消息以应对丢包：

```rust
pub async fn announce(&self) {
    for delay in ANNOUNCE_DELAYS {
        tokio::select! {
            _ = self.cancel.cancelled() => return,
            _ = tokio::time::sleep(delay) => {}
        }
        tracing::debug!("Announcing via UDP multicast");
        self.state.send().await;
    }
}
```

#### 响应方的工作流（[`packages/core/src/discovery/mod.rs#L197-L243`](https://github.com/localsend/localsend/blob/main/packages/core/src/discovery/mod.rs#L197-L243)）

```rust
impl DiscoveryHandle {
    pub async fn announce(&self) {
        if let Ok(multicast) = &self.multicast {
            multicast.announce().await;
        }
    }
    // ...discover() / scan_subnet() / set_answer_announcements()
}
```

收到他人 announce 后，接收端走 `answer_announcement()`（[`packages/core/src/discovery/mod.rs#L342-L468`](https://github.com/localsend/localsend/blob/main/packages/core/src/discovery/mod.rs#L342-L468)），并发发起 **HTTP 注册请求**：

1. 从 announce 中取出 `ip` / `port` / `fingerprint`
2. 用本机自签证书作为客户端证书发起 HTTPS POST `/api/localsend/v2/register`
3. 服务端验证客户端证书指纹与 payload 中的 `fingerprint` 一致后才确认（防止中间人伪造身份）
4. 注册成功后设备进入 `DeviceStore`，并向 App 发出 `Discovered` 或 `Updated` 事件

**回退路径**：当多播被禁用（如路由器开启 AP 隔离）时，仍可工作：
- `discover(host, port)`：手动对已知 IP 发起注册
- `scan_subnet(interface_ip)`：对 `/24` 子网广播注册（[`packages/localsend_isolates/lib/rust/api/discovery.dart#L87-L106`](https://github.com/localsend/localsend/blob/main/packages/localsend_isolates/lib/rust/api/discovery.dart#L87-L106)）

### 3.2 传输流程（HTTP + 自签证书 + 字节流通道）

文件传输完全发生在应用层与 Rust 核心之间通过 mpsc channel 传递的数据流上，不存在"先存到临时文件再发送"这种绕路。

#### Server→App 事件（[`packages/core/src/http/server/mod.rs`](https://github.com/localsend/localsend/tree/main/packages/core/src/http/server)）

`start_with_port(ServerConfigV2 { pin, event_tx, web_send })` 返回的 server 发送以下事件（[`AGENTS.md#L100-L103`](https://github.com/localsend/localsend/blob/main/AGENTS.md#L100-L103)）：

| `ServerEventV2` 事件 | 用途 |
|---|---|
| `Register` | 客户端注册（携带证书指纹） |
| `PrepareUpload` | 客户端准备上传，含 `decision_tx` oneshot——App 可异步决定是否接受 |
| `FileUpload` | 携带字节流 `binary_tx` + 结果 `result_tx`，App 写入文件 |
| `PrepareDownload` | 浏览器下载触发（web send） |
| `SessionEnd` | 会话结束 |
| `PrepareUploadAborted` / `CancelReceived` | 异常路径 |

> 同时 **只有一个上传会话处于活动状态**；通过 drop guard（`PendingSessionGuard`、`UploadGuard`、`PendingWebSessionGuard`）保证取消安全。

#### 文件接收落地（[`packages/core/src/http/server/common/save.rs#L244-L334`](https://github.com/localsend/localsend/blob/main/packages/core/src/http/server/common/save.rs#L244-L334)）

`spawn_file_writer()` 启动一个 tokio 任务消费 chunk 流：

```rust
async fn write_file_from_receiver(
    open: impl Future<Output = Result<tokio::fs::File, String>>,
    expected_size: u64,
    rx: &mut mpsc::Receiver<Bytes>,
    progress_tx: Option<mpsc::Sender<u64>>,
    timestamps: FileTimestamps,
) -> Result<(), String> {
    // ...循环 rx.recv().await → file.write_all() → try_send(progress_tx)...
    // 大小校验：超过 expected_size 立即终止
    if written > expected_size {
        return Err(format!("Expected {expected_size} bytes, received at least {written}"));
    }
    // 收尾：截断到实际写入大小（防止残留旧内容）+ 应用 RFC 3339 时间戳
}
```

#### 文件发送抽象（[`packages/core/src/model/transfer.rs#L0-L94`](https://github.com/localsend/localsend/blob/main/packages/core/src/model/transfer.rs#L0-L94)）

```rust
#[derive(Debug)]
pub enum FileContent {
    Stream(mpsc::Receiver<Bytes>),           // 内存或调用方流式提供
    Path(PathBuf),                          // 普通文件
    #[cfg(target_os = "android")]
    Fd(std::os::fd::RawFd),                 // Android：直接用 fd，不复制
}

impl FileContent {
    pub fn into_receiver(self) -> mpsc::Receiver<Bytes> {
        // Path/Fd → 后台 tokio 任务读 → 转 stream
        // Stream → 原样返回
    }
}
```

这意味着大文件不进入内存——Core 通过 16-cap mpsc 通道持续向 hyper body 推送 chunk。

#### Web send（浏览器接收）

[`packages/core/src/http/server/web.rs#L320-L345`](https://github.com/localsend/localsend/blob/main/packages/core/src/http/server/web.rs#L320-L345) 实现"通过 HTTP 短链让浏览器下载"，要点：
- 静态 HTML/JS 嵌入自 `packages/core/assets/web/`（含 `index.html`、`main.js`，main.js 自带 IE8 兼容注释！）
- 应用通过 `WebSendConfig { files, pin, i18n, event_tx }` 注册
- 服务端事件 `WebSendEvent::FileDownload { file_id, content_tx }` → App 注入 `FileContent::Stream(rx)` → 服务端用 `receiver_stream_body()` 渲染 HTTP response body

### 3.3 状态管理与进程隔离

**Refena**（而非 Riverpod）是 App 的状态管理框架，约束见 [`AGENTS.md#L81-L87`](https://github.com/localsend/localsend/blob/main/AGENTS.md#L81-L87)：

- **Provider 位置**：`app/lib/provider/`
- **`NotifierProvider`** 处理纯状态
- **`ReduxProvider` + Action 类** 处理与 isolate 层的交互（因为 isolate 是异步命令式）

**Isolate 拓扑**（[`packages/localsend_isolates/lib/src/isolate/`](https://github.com/localsend/localsend/tree/main/packages/localsend_isolates/lib/src/isolate)）：

```
ParentIsolateState 持有:
  - IsolateConnector × N（每种重任务一个 child）：
    * http_scan_discovery
    * multicast_discovery
    * http_upload
    * http_server
  - 镜像给每个 child 的 SyncState
```

通信规则（[`AGENTS.md#L88-L97`](https://github.com/localsend/localsend/blob/main/AGENTS.md#L88-L97)）：
- **唯一通道**：`parent/actions.dart` + `parent/actions_sync.dart` 是 App 与 child isolate 的**唯一**通讯方式
- **child 入口**：`child/*_isolate.dart`，将类型化任务消息转为 `lib/src/task/` 调用
- **lib/src/task/**：纯辅助逻辑，**禁止**写 isolate 代码（见其 `README.md`）
- **同步字段**（alias、port、protocol、是否启动 server、是否开启 web send）由 `IsolateSyncServerStateAction` 推送，child 启动时读取

**模型序列化**：使用 `dart_mappable`（`@MappableClass` + `.mapper.dart` part）。约定：
- `fromJson` / `toJson` — Map 转换器
- `deserialize` / `serialize` — String 转换器

**FRB 边界**：Freezed 用于 `flutter_rust_bridge` 邻接的 union 类型。

---

## 4. 技术栈与依赖清单

### 4.1 Flutter 端（[`app/pubspec.yaml`](https://github.com/localsend/localsend/blob/main/app/pubspec.yaml)）

```yaml
name: localsend_app
description: An open source cross-platform alternative to AirDrop
publish_to: "none"
version: 1.17.0+58
environment:
  flutter: ^3.41.0
  sdk: ^3.11.0
```

| 核心依赖 | 版本 | 用途 |
|---|---|---|
| `refena_flutter` | 3.2.1 | 状态管理框架 |
| `localsend_isolates` | path: `../packages/localsend_isolates` | Dart isolate + FRB 绑定 |
| `refena_inspector_client` | 2.1.1 | 状态调试工具 |
| `flutter_localizations` | sdk | 多语言基础 |
| `connectivity_plus` | 7.2.0 | 网络状态监测 |
| `network_info_plus` | 7.0.0 | 获取本地 IP（多网卡） |
| `permission_handler` | 12.0.3 | Android/iOS 权限申请 |
| `path_provider` / `path_provider_foundation` | 2.1.6 / 2.6.0 | 系统目录获取 |
| `device_info_plus` | 12.4.0 | 设备型号、SDK 版本 |
| `package_info_plus` | 9.0.1 | App 版本信息 |
| `flutter_local_notifications` | (隐含通过 init.dart) | 传输通知 |
| `file_selector` / `file_picker` | 1.1.0 / 11.0.2 | 文件/目录选择 |
| `image_picker` | 1.2.3 | 媒体选择 |
| `desktop_drop` | 0.7.1 | 桌面拖放支持 |
| `share_handler` | (隐含) | iOS/Android share intent |
| `window_manager` | (隐含) | 多窗口 / 托盘 |
| `flutter_displaymode` | 0.7.0 | Android 高刷支持 |
| `dynamic_color` | 1.8.1 | Android 12+ Material You |
| `saf_stream` | (隐含) | Android SAF 流式读 |
| `pretty_qr_code` | 3.6.0 | 接收方二维码展示 |
| `dart_mappable` | 4.8.0 | 模型序列化 |
| `freezed_annotation` | 3.1.0 | FRB 邻接 union |
| `logging` | 1.3.0 | 日志门面 |
| `slang` | (隐含) | i18n 代码生成 |
| `routerino` | 0.8.1 | 路由 |
| `in_app_purchase` | 3.3.0 `# [FOSS_REMOVE]` | 捐赠（非自由） |
| `mime` / `glob` / `path` / `image` | 2.0.0 / 2.1.3 / 1.9.1 / 4.8.0 | 工具 |
| `intl` | ^0.20.2 | 数字/日期格式化 |

### 4.2 Rust 核心（`packages/core/Cargo.toml`）

按特性开关（[`AGENTS.md`](https://github.com/localsend/localsend/blob/main/AGENTS.md#L60-L62) 强调 `default = []`，**必须** `--features full`）：
- `crypto`、`discovery`、`http`、`multicast`、`webrtc`、`webrtc-signaling`、`full`

关键 crates（基于源码观察）：
- `hyper` / `hyper-util` / `http-body-util` — HTTP 服务端/客户端
- `rustls` / `rustls-pki-types` — TLS（含 mandatory client cert）
- `tokio` — 异步运行时（含 `mpsc`、`oneshot`、`CancellationToken`）
- `reqwest` — HTTP 客户端（feature `http` 时再导出）
- `serde` / `serde_json` — JSON
- `socket2` — 精细 socket 选项（多播接口、TTL 等）
- `lru` — PIN 尝试 LRU 缓存
- `webrtc` — WebRTC 数据通道
- `bytes` / `futures-util` / `tokio-util` — 流/字节工具

### 4.3 支持平台

| 平台 | 最低版本 | 备注 |
|---|---|---|
| Android | 5.0 | 需授权本地网络、文件访问、APK 安装 |
| iOS | 12.0 | 需开启"本地网络"权限 |
| macOS | 11 Big Sur | 旧 Mac 可用 OpenCore Legacy Patcher 2.0.2 |
| Windows | 10 | v1.15.4 是 Windows 7 最后支持版本 |
| Linux | N/A | Gnome 需 `xdg-desktop-portal` + `xdg-desktop-portal-gtk`；KDE 需 `-kde` 版 |

构建工具：**Flutter 3.41**（pinned via `.fvmrc`，**必须用 `fvm flutter`**）+ **Rust toolchain**。

---

## 5. 关键文件级解析

> 选择标准：能完整反映"启动→发现→传输"主链路的 5 个代表性文件。

### 5.1 [`app/lib/main.dart`](https://github.com/localsend/localsend/blob/main/app/lib/main.dart)

App 唯一入口。共 88 行，核心结构：

```dart
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:localsend_app/config/init.dart';          // preInit
import 'package:localsend_app/gen/strings.g.dart';       // Slang i18n
import 'package:localsend_app/pages/home_page.dart';
import 'package:localsend_app/widget/watcher/life_cycle_watcher.dart';
import 'package:localsend_app/widget/watcher/shortcut_watcher.dart';
import 'package:localsend_app/widget/watcher/tray_watcher.dart';
import 'package:localsend_app/widget/watcher/window_watcher.dart';
import 'package:refena_flutter/refena_flutter.dart';
```

**核心模式**：
1. **`main(args)` 调 `preInit(args)`**（init.dart）→ 失败兜底 UI（`showInitErrorApp`）
2. **`runApp(RefenaScope.withContainer(...))`** — Provider 容器挂在 widget 树根
3. **`LocalSendApp` 嵌套多个 Watcher**：`TrayWatcher`（托盘事件）→ `WindowWatcher`（多窗口）→ `LifeCycleWatcher`（前后台切换时重扫本地 IP）→ `ShortcutWatcher`（全局快捷键）

**应用生命周期恢复**（main.dart#L57-L83）：

```dart
case AppLifecycleState.resumed:
  ref.redux(localIpProvider).dispatch(InitLocalIpAction());
  break;
```

> 重扫本地 IP 是因为 VPN/网络切换后网卡变化时必须刷新多播接口绑定。

### 5.2 [`app/lib/config/init.dart`](https://github.com/localsend/localsend/blob/main/app/lib/config/init.dart)

应用启动的真正"大脑"（共 200+ 行）。关键片段（[`init.dart#L0-L23`](https://github.com/localsend/localsend/blob/main/app/lib/config/init.dart#L0-L23)）展示了 **FOSS 剥离机制**：

```dart
// [FOSS_REMOVE_START]
import 'package:localsend_app/provider/purchase_provider.dart';
// [FOSS_REMOVE_END]
```

`support/scripts/remove_proprietary_dependencies.sh`（L0-L26）会把 `// [FOSS_REMOVE_START]` 替换为 `/*`、`// [FOSS_REMOVE_END]` 替换为 `*/`，让非自由代码在 F-Droid 版本里整段被注释掉。`pubspec.yaml` 的 `in_app_purchase: 3.3.0 # [FOSS_REMOVE]` 则直接被 `sed -i '/# \[FOSS_REMOVE\]/d'` 删除。

### 5.3 [`packages/core/src/model/transfer.rs`](https://github.com/localsend/localsend/tree/main/packages/core/src/model/transfer.rs)

文件传输模型的"数据契约"——所有跨语言 DTO 的源头。

#### `FileDto`（L95-L117）—— 协议层文件元数据：

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct FileDto {
    pub id: String,
    pub file_name: String,
    pub size: u64,
    pub file_type: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub sha256: Option<String>,          // 完整性校验（最新功能）
    #[serde(skip_serializing_if = "Option::is_none")]
    pub preview: Option<String>,         // 缩略图 base64
    #[serde(skip_serializing_if = "Option::is_none")]
    pub metadata: Option<FileMetadata>,  // RFC 3339 时间戳
}
```

#### `FileContent::into_receiver()`（L34-L46）—— 抽象文件源到字节流：

```rust
impl FileContent {
    pub fn into_receiver(self) -> mpsc::Receiver<Bytes> {
        match self {
            FileContent::Stream(rx) => {
                tracing::info!("Reading file content via byte stream from application");
                rx
            }
            FileContent::Path(path) => {
                let (tx, rx) = mpsc::channel(FILE_CHANNEL_CAPACITY);
                tokio::spawn(async move {
                    match tokio::fs::File::open(&path).await {
                        Ok(file) => read_file_into_sender(file, tx).await,
                        Err(e) => { /* error */ }
                    }
                });
                rx
            }
            #[cfg(target_os = "android")]
            FileContent::Fd(_) => { /* raw fd → tokio spawn */ }
        }
    }
}
```

> **设计亮点**：发送和接收共享同一个 `FileContent`，HTTP 客户端上传和 HTTP 服务端下载都用 `into_receiver()` 标准化为字节流。

### 5.4 [`packages/core/src/multicast/mod.rs`](https://github.com/localsend/localsend/blob/main/packages/core/src/multicast/mod.rs)

UDP 多播模块入口。关键函数 `start()`（L252-L295）：

```rust
pub async fn start(
    config: MulticastConfig,
    stop_rx: oneshot::Receiver<()>,
) -> anyhow::Result<MulticastHandle> {
    let sockets = socket::bind_multicast_sockets(
        config.group, config.group_v6, config.port, &config.interface_filter,
    )?;
    if sockets.is_empty() {
        anyhow::bail!("No network interface available for multicast on port {}", config.port);
    }
    // ...state 包装 + JoinSet 启动每个 socket 的 receive_loop
}
```

`receive_loop`（同文件内私有 fn）：每个 socket 一个任务，将原始 datagram 解析为 `MulticastEvent::Discovered { ip, scope_id, message }` 并送到 mpsc。

### 5.5 [`packages/core/src/discovery/mod.rs`](https://github.com/localsend/localsend/blob/main/packages/core/src/discovery/mod.rs)

发现模块的"上层"。关键设计：
- **`DiscoveryConfig`（L49-L73）**：含 `MulticastDevice`（alias/version/fingerprint/port/protocol）、`DeviceIdentity`（cert_pem + private_key_pem）、`interface_filter`（白/黑名单）、`timeout`
- **`DiscoveryHandle::start()`（L342-L468）**："启动不可能失败"——多播失败时仍可工作
- **`answer_announcement()`（同文件）**：收到他人 announce 时，**并发**发起 HTTP 注册（避免单次超时阻塞整轮）

```rust
let MulticastEvent::Discovered { ip, scope_id, message } = event;
// register 请求可能耗时（最长 = timeout），因此并发回答
tokio::spawn(answer_announcement(state.clone(), ip, scope_id, message));
```

### 5.6 [`packages/core/src/http/server/v2.rs`](https://github.com/localsend/localsend/blob/main/packages/core/src/http/server/v2.rs)

v2 协议 HTTP 服务端实现，含 `prepare_upload()`（L290-L318）：

```rust
pub(crate) async fn prepare_upload(
    req: Request<Incoming>,
    state: AppState,
    client_info: RequestClientInfo,
) -> Result<Response<BoxedBody>, AppError> {
    let PrepareUploadDecisionV2::Accept(ids) = ...;  // ← App 通过 oneshot 决策
    let files: HashMap<String, SessionFileV2> = payload
        .files.into_iter()
        .filter(|(id, _)| accepted_ids.contains(id))
        .map(|(id, dto)| {
            let file = SessionFileV2 {
                dto,
                token: Uuid::new_v4().to_string(),   // ← 每个文件生成 token
                status: FileStatusV2::Pending,
                attempts: 0,
            };
            (id, file)
        })
        .collect();

    if files.is_empty() {
        // 全部拒绝 → 204 NO_CONTENT
        let mut res = Response::new(empty_body());
        *res.status_mut() = StatusCode::NO_CONTENT;
        return Ok(res);
    }
    // ...返回 token 给客户端作为上传凭据
}
```

> 这是 **partial accept**（部分接收）功能的源头——`PrepareUploadRequestDtoV2.files` 是 HashMap，可只接受部分。

---

## 6. 扩展与配置机制

### 6.1 资源与外部配置（[`app/assets/`](https://github.com/localsend/localsend/tree/main/app/assets)）

| 文件/目录 | 用途 |
|---|---|
| `app/assets/CHANGELOG.md` | Flutter 端历史 changelog |
| `app/assets/i18n/*.json` + `_missing_translations_*.json` | Slang 翻译源，Weblate 同步 |
| `app/assets/localsend_logo_*` | 多分辨率 logo |
| `app/assets/icon.png` + `app/icons/` | 应用图标 |
| `packages/core/assets/web/` | 浏览器下载页（`index.html` + `main.js`），**编译时嵌入二进制** |

### 6.2 工具类（[`app/lib/util/`](https://github.com/localsend/localsend/tree/main/app/lib/util)）

| 文件 | 职责 |
|---|---|
| `util/native/channel/android_channel.dart` | 调 MethodChannel `org.localsend.localsend_app/localsend`，处理 Android SAF content URI 编解码 |
| `util/native/open_file.dart` | 用 `OpenFilex` + `permission_handler` 打开本地文件（APK 还会请求 `Permission.requestInstallPackages`） |
| `util/native/file_picker.dart` | 跨平台文件选择器（iOS/Android/desktop 不同路径） |
| `util/native/pick_directory_path.dart` | 目录选择 |
| `util/native/cross_file_converters.dart` | 各 picker → `CrossFile` 转换 |
| `util/native/platform_check.dart` | `checkPlatform([TargetPlatform.android])` 辅助 |
| `util/ui/dynamic_colors.dart` | 动态颜色实现 |
| `util/determine_image_type.dart` / `util/image_converter.dart` | 图片处理 |

### 6.3 运行参数调整

**便携模式**（v1.13.0 引入，[README.md](https://github.com/localsend/localsend/blob/main/README.md)）：

> 在可执行文件同目录创建空 `settings.json`，设置改存这里而不是默认位置。

**隐藏启动**（v1.15.0 更新）：

```bash
localsend_app.exe --hidden
```

**CLI 配置**（[`cli/src/main.rs#L13-L33`](https://github.com/localsend/localsend/blob/main/cli/src/main.rs#L13-L33)）：

```rust
#[derive(Parser)]
#[command(name = "localsend-cli", version, about, after_help = HELP_SECTIONS)]
pub struct Args {
    /// 设备名（默认 config.toml，否则 hostname）
    #[arg(long, env = "LOCALSEND_ALIAS")]
    pub alias: Option<String>,

    /// HTTP 服务端口（默认 config.toml，否则 53317）
    #[arg(long, env = "LOCALSEND_PORT")]
    pub port: Option<u16>,

    /// 接收文件保存目录（默认 config.toml，否则 Downloads）
    #[arg(long, env = "LOCALSEND_DESTINATION")]
    pub destination: Option<PathBuf>,

    /// 要发送的文件（重复可多次）
    #[arg(short, long = "file", value_name = "PATH")]
    pub file: Vec<PathBuf>,
}
```

支持的环境变量：`XDG_CONFIG_HOME`、`LOCALSEND_ALIAS`、`LOCALSEND_PORT`、`LOCALSEND_DESTINATION`。

**网络接口过滤**：App 通过 `start_discovery()` 的 `networkWhitelist` / `networkBlacklist` 参数（[`packages/localsend_isolates/lib/rust/api/discovery.dart`](https://github.com/localsend/localsend/blob/main/packages/localsend_isolates/lib/rust/api/discovery.dart)）传入 `InterfaceFilter`，控制哪些网卡参与发现。

---

## 7. 安全性设计

### 7.1 自签证书生成

- **每台设备启动时按需生成** 自签 RSA 证书（PEM），私钥永不出设备
- 证书 DER 的 **SHA-256 指纹**（uppercase hex）作为设备 `fingerprint`
- `cert.rs` 中的 `generate_self_signed()` 是入口（[`packages/core/src/crypto/`](https://github.com/localsend/localsend/tree/main/packages/core/src/crypto)）

### 7.2 信任策略

**核心原则**（[`AGENTS.md#L114-L116`](https://github.com/localsend/localsend/blob/main/AGENTS.md#L114-L116)）：

> "TLS uses per-device on-the-fly certificates with **mandatory client certificates**; the peer identity is the uppercase-hex SHA-256 of the client cert DER, and `Register` is simply not emitted when a payload's claimed fingerprint disagrees with the cert."

**强制 mTLS**：每次 HTTP 注册请求，服务端要求客户端证书：
1. 验证客户端证书链（虽然自签根，但有客户端 cert 即可识别身份）
2. 计算客户端 cert DER 的 SHA-256，与 announce payload 中的 `fingerprint` 比对
3. **不一致则不发 `Register` 事件**——这是抵御 ARP 欺骗 / 中间人的关键

**应用层建议**（[`AGENTS.md`](https://github.com/localsend/localsend/blob/main/AGENTS.md)）：
- 优先使用 `event.certFingerprint ?? event.info.fingerprint` —— payload 字段仅在"加密关闭"模式下作为 fallback

### 7.3 加密可关闭模式（HTTP-only）

- 设置为 HTTP 而非 HTTPS 时，`fingerprint` 为随机字符串（[`packages/core/src/model/discovery.rs#L78-L110`](https://github.com/localsend/localsend/blob/main/packages/core/src/model/discovery.rs#L78-L110)）
- 适用场景：老路由器 / 不支持的设备，但失去 TLS 保护

### 7.4 PIN 二次验证

- `ServerConfigV2.pin` 在 `start_with_port` 时固定，**更改需要重启 server**
- Web send 也有独立 `pin`，逻辑相同
- PIN 校验错误使用 LRU 缓存防爆破（`NonZeroUsize::new(200)`）—— 超过 200 次直接锁定

### 7.5 权限与数据隔离

- **文件保存路径**：`prepareFileSaveTarget` 在 Dart 层决定（[`AGENTS.md`](https://github.com/localsend/localsend/blob/main/AGENTS.md)），Rust 端仅负责写
- **Android SAF**：通过 `org.localsend.localsend_app/localsend` MethodChannel 拿 `RawFd`，**绕过 scoped storage 限制**，直接写用户授权的目录
- **路径清洗**（最新提交 `da4464d`）：Core 提供 `path sanitizing`，防止 `../` 穿越（[`packages/localsend_isolates/test/task/server/file_saver_test.dart#L35-L59`](https://github.com/localsend/localsend/blob/main/packages/localsend_isolates/test/task/server/file_saver_test.dart#L35-L59) 有专门测试 `still rejects path traversal`）
- **重名策略**：`digest()` 函数自动处理（`file.txt` → `file (2).txt`），保留已存在的同名文件

### 7.6 同时上传会话约束

**核心故意只允许一个上传会话**（[`AGENTS.md`](https://github.com/localsend/localsend/blob/main/AGENTS.md#L100-L103)）：
- 通过 `PendingSessionGuard`、`UploadGuard`、`PendingWebSessionGuard` 三个 RAII 类型保证
- 新请求会取消旧的（`CancelReceived` 事件）

---

## 8. 附录：源码阅读建议

### 8.1 推荐阅读路径

**目标：理解"启动 → 发现 → 传输 → 落地"全链路**

```
Step 1: 入口与启动
  app/lib/main.dart                                       # runApp 入口
  app/lib/config/init.dart :: preInit()                   # 初始化逻辑
  
Step 2: 状态层
  app/lib/provider/local_ip_provider.dart                  # 本机 IP 重扫
  app/lib/provider/network/nearby_devices_provider.dart   # 设备列表 UI 状态
  app/lib/provider/network/server/server_provider.dart     # 服务端事件路由
  
Step 3: 核心协议
  packages/core/src/multicast/mod.rs :: start()           # 多播 socket 绑定
  packages/core/src/discovery/mod.rs :: start()           # 上层发现（多播 + HTTP 注册）
  packages/core/src/discovery/mod.rs :: answer_announcement()
  
Step 4: HTTP 服务端
  packages/core/src/http/server/mod.rs :: start_with_port()
  packages/core/src/http/server/v2.rs :: prepare_upload() # 接收决策
  packages/core/src/http/server/common/save.rs :: write_file_from_receiver()
  
Step 5: 数据契约
  packages/core/src/model/transfer.rs :: FileDto, FileContent, FileMetadata
  packages/core/src/model/discovery.rs :: MulticastMessageV2
```

### 8.2 关键理解难点（新手标注）

1. **`PeerIp` 与 IPv6 scope ID**：link-local 地址 `fe80::1%3` 中的 `%3` 是接口索引。HTTP 客户端必须接受 `fe80::1%eth0` 写法回退为 host；事件里的 IP 必须保持可拨号（[`AGENTS.md`](https://github.com/localsend/localsend/blob/main/AGENTS.md#L114-L116)）。
2. **WebRTC 关闭处理**：WebRTC 数据通道关闭时，正在传输的文件需要走完"EOS → result callback → send RTCSendFileResponse"的完整序列，否则对端会卡住（参考 `packages/core/src/webrtc/webrtc.rs#L843-L914`）。
3. **平台通道调用**：Android 上获取 SAF `RawFd` 必须经 `MethodChannel('org.localsend.localsend_app/localsend')`；这是 Dart ↔ Kotlin 的边界，调试时需要打开 Logcat。
4. **FRB 自动生成的 `frb_generated.{dart,rs}`**：修改 Rust API 后必须 `flutter_rust_bridge_codegen generate`，否则调用会不匹配（`packages/localsend_isolates/rust/src/frb_generated.rs#L536-L552` 是 `RsDiscovery_discover` 的实现）。
5. **Drop guard 链**：`PendingSessionGuard` / `UploadGuard` / `PendingWebSessionGuard` 的所有权流转保证"只允许一个活跃上传会话"——理解 RAII 在异步上下文的语义。

### 8.3 补充资源

| 资源 | 链接 |
|---|---|
| 协议规范仓库 | https://github.com/localsend/protocol |
| 官网 | https://localsend.org |
| Discord | https://discord.gg/GSRWmQNP87 |
| Weblate 翻译平台 | https://hosted.weblate.org/projects/localsend/app |
| 依赖层级图 | [`support/docs/dependency-hierarchy.svg`](https://github.com/localsend/localsend/blob/main/support/docs/dependency-hierarchy.svg) |
| AGENTS.md（开发者导览） | [`AGENTS.md`](https://github.com/localsend/localsend/blob/main/AGENTS.md) |
| 构建说明 | [`README.md`](https://github.com/localsend/localsend/blob/main/README.md) "Building" 段 |

### 8.4 关键提交参考

| Commit | 说明 |
|---|---|
| `da4464d` | feat: path sanitizing in core（最新） |
| `0aea05a` | feat: implement CLI（CLI 引入） |
| `b13bbeb` | fix: timestamp handling on Android |
| `ea7e2cf` | docs: add dependency diagram |

### 8.5 工程化亮点总结

- **零依赖中心服务器**：通过 UDP 组播 + HTTPS 自签证书实现完全 P2P
- **跨平台原生体验**：Android SAF 直接拿 fd、iOS 14+ Share Extension、Linux 走 xdg-desktop-portal
- **多进程隔离**：所有网络 I/O 在 child isolate，UI 永不卡顿
- **协议开放 + 实现严谨**：有官方规范仓库 + 全面 Rust 单元/集成测试（含真实多播测试）
- **FOSS 友好**：通过注释标记在构建时剔除专有代码，F-Droid 版本与 Play 版本同源

---

> **文档结束**。如需进一步研究，建议从 [`AGENTS.md`](https://github.com/localsend/localsend/blob/main/AGENTS.md) 开始——它是项目维护者专为新贡献者（含 AI Agent）撰写的最高密度入口文档。