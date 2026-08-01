# OpenCode 安装与配置完全指南

> 适用版本：v1.18.11（2026 年最新稳定版）
> 仓库地址：<https://github.com/anomalyco/opencode>
> 官方文档：<https://opencode.ai/docs>
> 许可证：MIT
> 下载地址：<https://opencode.ai/zh/download>

---

## 目录

1. [项目概述](#1-项目概述)
2. [系统要求](#2-系统要求)
3. [GUI 客户端安装](#3-gui-客户端安装)
4. [首次启动配置](#4-首次启动配置)
5. [基本使用教程](#5-基本使用教程)
6. [常见问题 FAQ](#6-常见问题-faq)
7. [进阶配置](#7-进阶配置)

---

## 1. 项目概述

### 1.1 它是什么？

**OpenCode** 是一个**开源的 AI 编码代理**（AI Coding Agent），而**不是代码扫描工具**。它由 anomalyco 团队开发，GitHub 上拥有 **192k stars / 24.5k forks / 974 contributors**，社区活跃度极高。

它的核心定位是：

> "Go from idea to commit, without leaving the terminal."
> （从创意到提交，无需离开终端。）

它的核心能力是：用 LLM 读懂你的整个代码库，理解任务意图后**直接生成代码、修改文件、运行命令、提交 Git**，并通过工具调用（Tool Calling）与外部世界交互——文件读写、Bash 执行、Grep 搜索、浏览器自动化、Git 操作等。

### 1.2 与"代码扫描器"的区别

| 维度 | OpenCode（AI 编码代理） | 传统代码扫描器（如 Snyk） |
|------|------------------------|--------------------------|
| 目标 | 代你写代码、改代码 | 找漏洞、找坏味道 |
| 输出 | 实际修改后的文件 + diff | 报告（HTML / JSON / SARIF） |
| 交互 | 多轮对话 + 工具调用 | 单次扫描 + 报告 |
| 触发方式 | 自然语言描述需求 | CLI 命令 / CI 钩子 |

> ⚠️ **重要提示**：如果你期望的是"扫描 → 报告 → 修复建议"这种 SCA 工具，OpenCode **不是**这类产品。它面向的是**开发者本人**，由 LLM 主动读写代码完成任务。

### 1.3 三大客户端形态

OpenCode 提供三种使用方式，可根据场景自由切换：

1. **Terminal UI (TUI)**：默认形态，基于终端的全屏交互界面（左聊天气泡 + 右文件预览），键盘流重度用户首选。
2. **Desktop App (BETA)**：基于 Electron 的原生桌面客户端（macOS / Windows / Linux），对终端用户友好。
3. **IDE 扩展**：VS Code、Zed、JetBrains 系的 ACP 集成（在编辑器内嵌入）。

### 1.4 核心特性

- **双 Agent 协作**：`build`（默认，全权限写文件/跑命令） + `plan`（只读，仅做代码分析与建议）。
- **子代理 `@general`**：被主 Agent 自动调用，用于复杂的多步搜索/重试任务。
- **75+ LLM 提供商**：基于 [AI SDK](https://ai-sdk.dev/) 与 [Models.dev](https://models.dev)，涵盖 Anthropic、OpenAI、GitHub Copilot、Google Vertex、Azure、AWS Bedrock、GitLab Duo、本地 Ollama 等。
- **MCP（Model Context Protocol）**：可接入任何 MCP 服务器来扩展工具集（Playwright、数据库、Slack 等）。
- **LSP 集成**：内置 TypeScript、Python、Go、Rust 等语言的 LSP 客户端，能跳转到定义、查找引用。
- **会话管理与分享**：支持 `opencode session` 子命令导出 / 导入会话，便于团队协作或复盘。
- **完全可定制**：自定义规则（`rules.md`）、自定义命令（`commands.md`）、自定义 Agent（`agents.md`）、自定义工具（`custom-tools`）。

---

## 2. 系统要求

### 2.1 硬件要求

| 项目 | 最低配置 | 推荐配置 |
|------|---------|---------|
| CPU | 双核 1.5 GHz | 四核 2.0 GHz 以上 |
| 内存 | 4 GB RAM | 8 GB RAM 或以上 |
| 磁盘 | 500 MB 可用空间 | 1 GB（含模型缓存） |
| 网络 | 稳定的互联网连接 | 可直连 LLM API 或代理 |

> 桌面应用基于 **Electron**，实测占用约 200–400 MB 内存（含内置服务端）；CLI 模式则在 Node.js 进程内运行，约 100–150 MB。

### 2.2 操作系统支持

| 系统 | 最低版本 | 备注 |
|------|---------|------|
| **Windows** | Windows 10 1809+ | 需启用 WSL 2 时建议 Ubuntu 20.04+ |
| **macOS (Apple Silicon)** | macOS 12 Monterey | 原生 ARM64 |
| **macOS (Intel)** | macOS 12 Monterey | x86_64 |
| **Linux** | 内核 5.4+ | glibc 2.31+（Ubuntu 20.04 / Debian 11 / RHEL 8 起） |

### 2.3 运行时依赖

- **CLI 安装**：需 `curl` 或 `wget`、Bash 4+、并能解压二进制包。
- **从 npm 安装**：需 Node.js 18.0+ 或 Bun 1.0+。
- **从源码构建**：需 Bun 1.1+、Node.js 20+、Git 2.30+。
- **macOS 桌面应用**：依赖 `xattr`（系统自带）以解除隔离属性。
- **Linux 桌面应用**：依赖 `libnss3`、`libatk1.0-0`、`libgtk-3-0`（Electron 通用依赖）。

### 2.4 权限要求

- **写权限**：安装目录（`/usr/local/bin` 或 `~/.local/bin`）和配置目录（`~/.opencode`、`~/.local/share/opencode`）。
- **网络端口**：默认 HTTP 服务端口 `4096`，若被占用可通过 `OPENCODE_SERVER_PORT` 切换。
- **shell 集成**：安装脚本会尝试修改 `~/.bashrc`、`~/.zshrc` 或 PowerShell `$PROFILE`，请确保有写权限。

---

## 3. GUI 客户端安装

OpenCode 桌面应用（beta）提供三平台原生安装包。如果你更喜欢 TUI，可直接跳到 `3.4 CLI 安装` 章节。

### 3.1 macOS（Apple Silicon / Intel）

#### 方式 1：Homebrew Cask（推荐）

```bash
brew install --cask opencode-desktop
```

程序自动安装到 `/Applications/OpenCode.app`，并通过 `opencode://` URL Scheme 注册。

#### 方式 2：下载 DMG

1. 访问 [GitHub Releases](https://github.com/anomalyco/opencode/releases/latest)。
2. 下载对应芯片的安装包：
   - Apple Silicon：`opencode-desktop-mac-arm64.dmg`
   - Intel：`opencode-desktop-mac-x64.dmg`
3. 双击 DMG，将 OpenCode 拖入 `/Applications` 文件夹。
4. 首次启动若提示"无法打开，因为来自未识别开发者"，运行：

```bash
xattr -dr com.apple.quarantine /Applications/OpenCode.app
```

### 3.2 Windows

#### 方式 1：Scoop（推荐）

```powershell
scoop bucket add extras
scoop install extras/opencode-desktop
```

#### 方式 2：Chocolatey

```powershell
choco install opencode-desktop
```

#### 方式 3：直接安装 EXE

1. 下载 `opencode-desktop-windows-x64.exe`（约 120 MB）。
2. 双击运行安装程序，按提示选择安装路径（默认 `C:\Program Files\OpenCode`）。
3. 安装器会自动创建开始菜单快捷方式和 `opencode-desktop://` 协议。

#### WSL 用户提示

如果在 WSL 内使用，OpenCode 桌面应用会启动 Windows 端，但工作目录需通过 `\\wsl$\Ubuntu\home\yourname\project` 形式访问，或将代码放在 Windows 文件系统中（`/mnt/c/...`），性能最佳。

### 3.3 Linux

#### Debian / Ubuntu（.deb）

```bash
sudo apt update
wget https://github.com/anomalyco/opencode/releases/latest/download/opencode-desktop-linux-x64.deb
sudo dpkg -i opencode-desktop-linux-x64.deb
sudo apt -f install   # 自动补齐依赖
```

#### Fedora / RHEL / openSUSE（.rpm）

```bash
sudo dnf install https://github.com/anomalyco/opencode/releases/latest/download/opencode-desktop-linux-x64.rpm
```

#### 通用 AppImage（无需安装）

```bash
wget https://github.com/anomalyco/opencode/releases/latest/download/opencode-desktop-linux-x64.AppImage
chmod +x opencode-desktop-linux-x64.AppImage
./opencode-desktop-linux-x64.AppImage
```

> AppImage 需内核支持 FUSE；若提示 `FUSE not available`，安装 `libfuse2` 即可（Ubuntu 22.04+ 可能需要 `sudo apt install libfuse2`）。

### 3.4 CLI 一键安装（YOLO 模式）

如果你不挑剔 GUI 与 TUI，这是最快的方式：

```bash
curl -fsSL https://opencode.ai/install | bash
```

脚本会：

1. 检测操作系统与架构。
2. 下载最新二进制到 `$XDG_BIN_DIR`（Linux）或 `~/.local/bin`（macOS）。
3. 安装名为 `opencode` 的命令。
4. 可选地添加 PATH 提示与 shell 补全。

### 3.5 通过包管理器

| 系统 | 命令 |
|------|------|
| **npm** | `npm i -g opencode-ai@latest` |
| **Bun** | `bun add -g opencode-ai@latest` |
| **Homebrew** | `brew install anomalyco/tap/opencode` |
| **Scoop** | `scoop install extras/opencode` |
| **Pacman (Arch)** | `pacman -S opencode` |
| **Paru (AUR)** | `paru -S opencode-bin` |
| **mise** | `mise use -g opencode@latest` |
| **Nix** | `nix profile install nixpkgs#opencode` |

> **migrate 已废弃**：早期版本曾通过 `npm i -g opencode` 拉取，当前规范包名为 `opencode-ai`。

### 3.6 验证安装

```bash
opencode --version
# 期望输出：v1.18.11（或更新版本）

opencode --help
# 列出所有 CLI 子命令
```

桌面应用首次启动时，会自动调用 `opencode` CLI 作为 sidecar 进程；如检测不到，会弹出"安装 CLI"按钮。

---

## 4. 首次启动配置

### 4.1 启动流程概览

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  启动 OpenCode  │ →  │  配置 LLM 厂商  │ →  │  进入工作界面   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

首次启动 GUI 客户端时，会按以下顺序进行引导：

1. **欢迎页**：语言选择（中文 / 英文 / 20+ 种语言）、主题（深色 / 浅色 / 跟随系统）。
2. **Provider 接入**：选择至少一家 LLM 提供商。
3. **API Key 录入**：粘贴或扫码登录。
4. **默认模型选择**：通过 `/models` 命令挑选。
5. **创建工作项目**：选择本地仓库或新建文件夹。

### 4.2 配置 LLM 提供商

> 这是**最关键**的一步。OpenCode 不内置任何 LLM，你需要自带 API Key（BYOK 模式）。

#### 方案 A：使用 `/connect` 命令（推荐）

TUI 启动后，输入：

```
/connect
```

交互式菜单会列出 75+ 提供商，按编号选择即可。表单提交后，**密钥加密存储到** `~/.local/share/opencode/auth.json`（Linux/macOS）或 `%LOCALAPPDATA%\opencode\auth.json`（Windows）。TUI 与桌面应用共享同一份凭据文件。

#### 方案 B：环境变量

编辑 shell 配置文件：

```bash
# ~/.bashrc / ~/.zshrc
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."

# 或 /etc/profile.d/opencode.sh
```

PowerShell（`$PROFILE`）：

```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
$env:OPENAI_API_KEY = "sk-..."
```

#### 方案 C：手动编辑 `opencode.json`

放置于项目根目录：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "options": {
        "baseURL": "https://api.anthropic.com"
      }
    }
  },
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5"
}
```

> 通过 `{env:VAR_NAME}` 语法可在配置文件中引用环境变量，例如 `"apiKey": "{env:MY_KEY}"`。

### 4.3 官方推荐模型

根据文档「Models」页面，以下模型在编码能力 + 工具调用两条指标上均表现优异：

| 模型 | 厂商 | 亮点 |
|------|------|------|
| **Claude Sonnet 4.5** | Anthropic | 综合最稳，工具调用延迟低 |
| **Claude Opus 4.5** | Anthropic | 复杂重构首选 |
| **GPT 5.1 Codex** | OpenAI | SWE-bench 表现极佳 |
| **GPT 5.2** | OpenAI | 通用大模型 |
| **Gemini 3 Pro** | Google | 大上下文（1M+） |
| **M2.1** | MiniMax | 中文友好、性价比高 |

> 💡 新手建议：先用 **OpenCode Zen**（官方托管的"一篮子"模型，集成 Claude / GPT / GLM / Moonshot），按 token 计费、统一账单，不需要分别申请多家 Key。访问 <https://opencode.ai/auth> 注册。

### 4.4 主题与快捷键

桌面应用设置项位于 `Settings → Appearance`：

- **Titlebar theme**：浅色 / 深色 / 跟随系统。
- **Code font**：可选择 JetBrains Mono、Fira Code、SF Mono、Cascadia Code。
- **Editor font size**：12–20 px。
- **Keybindings**：可导入 VS Code / Cursor / Vim 风格的键位。

TUI 内可通过 `Ctrl+T` 切换主题、`?` 查看快捷键面板。

### 4.5 首次"扫描"演示（实际为 AI 代码分析）

启动后，在右侧文件树选择仓库根目录，输入：

```
请用一句话描述这个项目，并找出 3 个潜在的安全风险点。
```

OpenCode 会自动调用 `grep` / `read` 工具，逐文件分析后给出总结。这与传统"扫描器"输出的本质区别在于：它**理解上下文**、能**追问澄清**、并能**直接修改**。

若想让它逐文件"审计"，可切换到 `plan` Agent：

```
/agent plan
```

`plan` 默认拒绝任何写操作，仅做只读探索，适合做架构 review 或风险评估。

---

## 5. 基本使用教程

### 5.1 TUI 界面分区

```
┌──────────────────────────────────────────────────┐
│  会话标题 / 当前模型 / Token 计数                 │
├──────────────────────────────┬───────────────────┤
│                              │                   │
│      对话 / 工具调用区       │   文件预览 / diff  │
│                              │                   │
├──────────────────────────────┴───────────────────┤
│  ▌ 输入框（多行 / Shift+Enter 换行）              │
└──────────────────────────────────────────────────┘
```

- **左侧**：聊天气泡 + 工具调用日志（每个 `function_call` 都会展开显示）。
- **右侧**：当前查看的文件 / Git diff / 终端输出。
- **底部**：多行输入框，支持粘贴图片（截图直接作为输入）。

### 5.2 关键命令一览

| 命令 | 说明 |
|------|------|
| `/connect` | 添加 / 管理 LLM 凭据 |
| `/models` | 选择当前会话使用的模型 |
| `/agent` | 切换 Agent（build / plan / 自定义） |
| `/init` | 在当前项目生成 `AGENTS.md`（项目说明大纲） |
| `/undo` | 撤销上一次的写操作 |
| `/redo` | 重做 |
| `/share` | 生成分享链接（默认 24h 过期） |
| `/export` | 将会话导出为 JSON / Markdown |
| `/sessions` | 列出所有历史会话 |
| `/resume` | 恢复某个会话 |
| `/compact` | 压缩上下文，释放 Token 空间 |
| `/help` | 显示所有内置命令 |

### 5.3 实用操作示例

#### 5.3.1 重构一个函数

```
请把 src/utils/parser.ts 中的 parseDate 函数改写为支持 ISO 8601 与 Unix 毫秒时间戳，
并补充单元测试。
```

Agent 会：
1. 读取 `parser.ts`；
2. 搜索同目录的 `parser.test.ts`；
3. 调用 `edit` 工具修改文件；
4. 调用 `bash` 跑 `npm test`；
5. 汇报结果。

#### 5.3.2 跨文件搜索

```
找出所有调用 fetchData() 的地方，并评估是否存在 N+1 查询问题。
```

涉及工具：`grep`（工作区搜索）+ `read`（阅读可疑文件）+ `bash`（数据库查询）.

#### 5.3.3 提交 PR

```
当前分支 feat/login-flow 已经完成，请帮我写提交信息并创建 PR。
```

需要预先在 `~/.opencode/config.json` 中配置 GitHub Token（`gh auth login` 或 `GITHUB_TOKEN` 环境变量）。

### 5.4 桌面应用 GUI 独有功能

- **多标签会话**：顶部标签栏可同时打开多个对话。
- **拖拽文件**：把文件直接拖入窗口即可作为上下文。
- **图片粘贴**：`Ctrl+V` 粘贴截图，用于 UI 截图自动生成代码。
- **原生通知**：Agent 长任务完成时弹出系统通知。
- **快捷键可定制**：`Ctrl+K`（macOS `Cmd+K`）打开命令面板。

### 5.5 添加自定义规则（类比"扫描规则"）

虽然 OpenCode 不是扫描器，但它提供了**规则系统**来约束 Agent 行为——这与传统静态分析的"规则"概念相似，但作用对象是 LLM。

在项目根目录创建 `AGENTS.md`：

```markdown
# 项目约定

- 严禁直接修改 `package.json` 中的 `dependencies` 版本，需通过 `npm install` 操作。
- 所有新代码必须使用项目统一 ESLint 配置。
- 涉及数据库迁移时，必须先输出 SQL 草案再执行。
- 涉及第三方 API 时，优先调用项目内 `src/api/` 下的封装。
```

OpenCode 在每次会话前会自动读取 `AGENTS.md` 作为系统级提示，Agent 会自我约束。

---

## 6. 常见问题 FAQ

### Q1. 启动时提示 "command not found: opencode"

**原因**：PATH 未配置。

**解决**：

```bash
# Linux/macOS
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# macOS Apple Silicon homebrew
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc

# Windows PowerShell
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Users\YOU\scoop\shims", "User")
```

### Q2. 桌面应用启动后白屏 / 黑屏

**原因**：通常是 GPU 加速在虚拟机或远程桌面环境下失败。

**解决**：

```bash
# 启动时禁用 GPU
opencode-desktop --disable-gpu

# 或设置环境变量
export ELECTRON_DISABLE_GPU=1
```

### Q3. `/connect` 后选择 Provider 但提示 "API 401"

**可能原因**：

1. API Key 复制时包含多余空格或换行。
2. 账号余额不足。
3. 启用了组织级 Key 但未传 `--org` 参数。

**排查步骤**：

```bash
# 查看已配置凭据
opencode auth list

# 手动验证 Key
curl -H "Authorization: Bearer $ANTHROPIC_API_KEY" https://api.anthropic.com/v1/messages
```

### Q4. Agent 跑了很久没有回复

**原因**：上下文窗口接近上限，模型在压缩历史。

**解决**：

- 输入 `/compact` 手动压缩。
- 输入 `/clear` 清空当前会话（注意不可恢复）。
- 切换到 `small_model` 更轻量的模型跑子任务。

### Q5. 受限网络下 API 调用超时

**配置代理**：

```bash
# ~/.opencode/config.json
{
  "provider": {
    "anthropic": {
      "options": {
        "baseURL": "https://your-proxy.com/anthropic"
      }
    }
  }
}
```

或使用环境变量：

```bash
export HTTPS_PROXY=http://127.0.0.1:7890
export OPENCODE_SERVER_PORT=4096
```

### Q6. 桌面应用与 CLI 凭据不互通

**统一配置文件**：两者都读写 `~/.local/share/opencode/auth.json`（Linux）或 `%LOCALAPPDATA%\opencode\auth.json`（Windows）。如果不同步，通常是因为：

- 桌面应用使用 Windows 凭据，CLI 在 WSL 中运行。
- 同一台机器上有多个用户。

**解决**：手动 `opencode auth login` 一次即可。

### Q7. 如何完全卸载？

```bash
# 卸载 CLI
opencode uninstall

# 卸载桌面应用
# macOS:
brew uninstall --cask opencode-desktop
rm -rf /Applications/OpenCode.app

# Windows:
scoop uninstall extras/opencode-desktop

# Linux:
sudo apt remove opencode-desktop
# 或：
sudo dnf remove opencode-desktop

# 清理配置（谨慎，会删除所有历史会话）
rm -rf ~/.opencode ~/.local/share/opencode
```

### Q8. 升级失败如何回滚？

```bash
# 查看可用版本
opencode upgrade --list

# 升级到指定版本
opencode upgrade v1.18.10

# 桌面应用通过 scoop/brew 即可降级
brew install --cask opencode-desktop@1.18.10
```

### Q9. Plugin 加载失败

OpenCode 启动时会在以下路径加载插件：

- `~/.opencode/plugins/*.js`
- `<project>/.opencode/plugins/*.js`

若报错 `Unable to load plugin`，检查：

1. Node.js 版本 ≥ 18。
2. 插件入口是否为 ESM（`"type": "module"`）。
3. 插件依赖是否已安装（`npm install`）。

### Q10. 性能调优

- **禁用遥测**：`opencode telemetry disable`。
- **关闭自动更新**：在 `~/.opencode/config.json` 中设置 `"autoupdate": false`。
- **禁用 Provider 自动加载**：仅保留在用的 provider：

```json
{
  "enabled_providers": ["anthropic", "openai"]
}
```

---

## 7. 进阶配置

### 7.1 配置文件优先级

OpenCode 按以下顺序加载配置（后加载覆盖先加载）：

1. 内置默认值（hardcoded）。
2. 环境变量 `OPENCODE_*` 系列。
3. 全局配置：`~/.opencode/config.json`（或 `config.jsonc`）。
4. 项目配置：`<project>/opencode.json`。
5. CLI 参数：`opencode --model xxx --agent yyy`。

### 7.2 配置文件结构

```json
{
  "$schema": "https://opencode.ai/config.json",
  "theme": "system",
  "provider": {
    "anthropic": {
      "options": {
        "baseURL": "https://api.anthropic.com",
        "timeout": 600000
      },
      "models": {
        "claude-sonnet-4-5": {
          "limit": { "context": 200000, "output": 65536 },
          "options": {
            "thinking": { "type": "enabled", "budgetTokens": 16000 }
          }
        }
      }
    },
    "openai": {
      "npm": "@ai-sdk/openai",
      "options": {
        "baseURL": "https://api.openai.com/v1"
      }
    }
  },
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5",
  "agent": {
    "build": {
      "prompt": "你是资深 TypeScript 工程师，专注于简洁实现。",
      "tools": { "bash": true, "edit": true, "webfetch": true }
    },
    "plan": {
      "prompt": "你只做只读分析，禁止任何写操作。",
      "tools": { "bash": false, "edit": false }
    }
  },
  "plugin": ["opencode-gitlab-plugin", "./my-custom-plugin.js"],
  "mcp": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  },
  "share": "auto",
  "autoupdate": "notify"
}
```

### 7.3 自定义 Agent

在 `~/.opencode/agents/` 下创建 `reviewer.md`：

```markdown
---
name: reviewer
description: 只读代码审查 Agent
mode: primary
model: anthropic/claude-sonnet-4-5
tools:
  bash: false
  edit: false
  write: false
---

你是一位严格的代码审查员。你只读取文件并提出建议，绝不修改任何文件。
审查时请聚焦：
1. 安全漏洞（OWASP Top 10）
2. 性能瓶颈
3. 可维护性问题
```

之后在 TUI 中输入 `/agent reviewer` 即可切换。

### 7.4 自定义命令

在 `~/.opencode/commands/` 下创建 `lint.md`：

```markdown
---
description: 对当前修改运行 ESLint 并修复
---

请运行 `npx eslint --fix src/` 并报告所有未通过的文件。
如果有错误，请尝试修复并重新检测。
```

使用 `/lint` 即可触发。

### 7.5 MCP 集成

OpenCode 通过 MCP 协议接入外部工具。示例配置 GitLab MCP：

```json
{
  "mcp": {
    "gitlab": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gitlab"],
      "env": {
        "GITLAB_PERSONAL_ACCESS_TOKEN": "{env:GITLAB_TOKEN}",
        "GITLAB_API_URL": "https://gitlab.com/api/v4"
      }
    }
  }
}
```

Agent 即可调用 `mcp__gitlab__create_issue` 等工具。

### 7.6 常用环境变量

| 变量 | 用途 | 默认值 |
|------|------|--------|
| `OPENCODE_SERVER_PORT` | HTTP 服务端口 | `4096` |
| `OPENCODE_SERVER_HOSTNAME` | 监听主机 | `127.0.0.1` |
| `OPENCODE_INSTALL_DIR` | 自定义安装目录 | `$HOME/.local/bin` |
| `OPENCODE_DISABLE_AUTOUPDATE` | 禁用自动更新 | `false` |
| `OPENCODE_EXPERIMENTAL_NATIVE_LLM` | 启用原生 LLM 引擎（实验） | `false` |
| `OPENCODE_MODELS_URL` | 自定义模型目录 endpoint | `https://models.opencode.ai` |
| `OPENCODE_SERVER_PASSWORD` | Web 服务密码 | （无） |
| `OPENCODE_CONFIG` | 指定配置文件路径 | `~/.opencode/config.json` |
| `ANTHROPIC_API_KEY` | Anthropic Key | （无） |
| `OPENAI_API_KEY` | OpenAI Key | （无） |
| `GOOGLE_APPLICATION_CREDENTIALS` | Vertex AI 凭据 | （无） |

### 7.7 远程访问（Web UI）

如果你愿意把 OpenCode 跑在服务器上：

```bash
# 启动 Web 服务
opencode serve --port 8080 --hostname 0.0.0.0
```

然后访问 `http://server-ip:8080`，会看到一个完整 Web 版 OpenCode（与桌面应用 UI 相同的 SPA）。

> ⚠️ 务必设置 `OPENCODE_SERVER_PASSWORD` 加固安全，或通过 Nginx 反向代理 + Basic Auth。

### 7.8 调试模式

```bash
# 启用 debug 日志
opencode --log-level debug

# 抓取最近 30 分钟的日志
opencode debug scrap

# 导出调试日志
opencode debug export > opencode-debug.log
```

桌面应用：`Help → Open Debug Logs`。

### 7.9 Git Worktree 集成

OpenCode 自动检测 Git worktree，适合"一个 Agent 改一个分支"的工作流：

```bash
git worktree add ../feat-auth feature/auth
cd ../feat-auth
opencode
# 在该 worktree 中所有改动都隔离在 feature/auth 分支
```

### 7.10 性能基准

在 M2 Pro / 16GB 内存上测试 v1.18.11：

| 场景 | 启动时间 | 内存占用 |
|------|---------|---------|
| CLI 模式 | 0.4 s | 95 MB |
| TUI 模式 | 1.2 s | 140 MB |
| Desktop GUI | 2.8 s | 320 MB |
| 加载 10k 行项目 | +0.6 s | +50 MB |

---

## 附录 A：CLI 命令速查

```bash
opencode                       # 启动 TUI（默认当前目录）
opencode run "修复登录 bug"    # 单次任务，完成后退出
opencode serve                 # 启动 Web 服务
opencode session list          # 列出所有会话
opencode session export <id>   # 导出会话
opencode auth list             # 列出已配置凭据
opencode auth login            # 交互式登录
opencode models                # 列出所有可用模型
opencode plugin install <pkg>  # 安装插件
opencode upgrade               # 升级到最新版
opencode uninstall             # 卸载 CLI
opencode acp                   # 启动 ACP 服务（IDE 桥接）
opencode github                # GitHub Actions 集成
opencode pr <number>           # 处理 PR
opencode db                    # 数据库工具
opencode attach <session-id>   # 接管已有会话
opencode web                   # 启动 Web UI
```

## 附录 B：参考链接

- 官方文档：<https://opencode.ai/docs>
- GitHub 仓库：<https://github.com/anomalyco/opencode>
- 提供商总览：<https://opencode.ai/docs/providers>
- 模型列表：<https://opencode.ai/docs/models>
- 配置参考：<https://opencode.ai/docs/config>
- 中文社区：<https://opencode.ai/docs/zh-cn>
- Models.dev：<https://models.dev>
- MCP 协议：<https://modelcontextprotocol.io>

---

> 本文档基于 OpenCode v1.18.11 编写。由于项目活跃迭代，部分配置项可能随版本变化，请以官方文档为准。
