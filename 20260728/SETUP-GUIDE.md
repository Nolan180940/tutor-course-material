# SiliconFlow-NextChat 部署指南

> 基于 NextChat 的 SiliconFlow 集成版本，支持国内用户使用 SiliconFlow API 访问多种大模型

---

## 1. 项目简介

### 1.1 什么是 SiliconFlow-NextChat？

**SiliconFlow-NextChat** 是 NextChat (ChatGPT-Next-Web) 的一个分支版本，由社区开发者 **Nolan180940** 维护。该版本在原版基础上**内置了 SiliconFlow 支持**，国内用户无需代理即可直接使用。

**GitHub 仓库**：[Nolan180940/SiliconFlow-NextChat](https://github.com/Nolan180940/SiliconFlow-NextChat)

**在线演示**：[silicon-flow-next-chat.vercel.app](https://silicon-flow-next-chat.vercel.app/)

### 1.2 与原版的区别

| 特性 | 原版 NextChat | SiliconFlow-NextChat |
|------|---------------|---------------------|
| SiliconFlow 支持 | ❌ 需手动配置 | ✅ 内置支持 |
| 模型列表 | 需手动添加 | ✅ 预置 SiliconFlow 模型 |
| 国内访问 | 需要代理 | ✅ 直连国内 API |
| 部署难度 | 较高（需配置代理） | ✅ 简单（开箱即用） |

### 1.3 支持的模型

通过 SiliconFlow，你可以访问以下模型（部分）：

| 模型 | 类型 | 说明 |
|------|------|------|
| MiniMax-M2.5-Pro | 聊天 | MiniMax 最新模型 |
| DeepSeek-V4-Pro | 多模态 | DeepSeek V4 多模态 |

---

## 2. 准备工作

### 2.1 注册 SiliconFlow 账号

1. 访问 [SiliconFlow 官网](https://siliconflow.cn)（或 [siliconflow.cn](https://www.siliconflow.cn)）
2. 使用微信/手机号注册账号
3. 进入控制台，获取 **API Key**

> 💡 **新手福利**：SiliconFlow 新用户通常赠送免费额度，可先体验再充值。

### 2.2 获取 API Key

1. 登录 SiliconFlow 控制台
2. 找到「API 密钥」或「API Key」菜单
3. 点击「创建密钥」，复制保存


---

## 3. 部署方式

### 3.1 方式一：Vercel 一键部署（推荐）

这是最简单的方式，**无需服务器**，免费且快速。

#### 步骤

1. **Fork 项目**
   
   访问 [Nolan180940/SiliconFlow-NextChat](https://github.com/Nolan180940/SiliconFlow-NextChat)，点击右上角 **Fork** 按钮。

2. **部署到 Vercel**
   
   点击下方按钮一键部署：

   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FNolan180940%2FSiliconFlow-NextChat&env=SILICONFLOW_API_KEY&env=CODE&project-name=siliconflow-nextchat)

3. **配置环境变量**

   在部署页面，添加以下环境变量：

   | 变量名 | 值 | 说明 |
   |--------|-----|------|
   | `SILICONFLOW_API_KEY` | 你的 API Key | **必填** |
   | `CODE` | 访问密码（可选） | 多个密码用逗号分隔 |

4. **完成部署**

   点击 **Deploy**，等待 1-2 分钟即可。

5. **访问使用**

   部署完成后，访问 Vercel 分配的域名即可使用。

---

### 3.2 方式二：Docker 部署

如果你有服务器或 NAS，可以使用 Docker 部署。

#### 基础部署

```bash
# 拉取镜像
docker pull yidadaa/chatgpt-next-web

# 运行容器
docker run -d -p 3000:3000 \
  -e SILICONFLOW_API_KEY=sk-你的APIKey \
  -e CODE=你的访问密码 \
  yidadaa/chatgpt-next-web
```

#### 启用代理（可选）

如果你的服务器需要代理才能访问 SiliconFlow：

```bash
docker run -d -p 3000:3000 \
  -e SILICONFLOW_API_KEY=sk-你的APIKey \
  -e CODE=你的访问密码 \
  -e PROXY_URL=http://你的代理地址:端口 \
  yidadaa/chatgpt-next-web
```

#### 启用 MCP（可选）

```bash
docker run -d -p 3000:3000 \
  -e SILICONFLOW_API_KEY=sk-你的APIKey \
  -e CODE=你的访问密码 \
  -e ENABLE_MCP=true \
  yidadaa/chatgpt-next-web
```

#### 访问

部署完成后，浏览器访问 `http://你的服务器IP:3000`

---

### 3.3 方式三：Zeabur 部署

Zeabur 是另一个免费的 Serverless 部署平台，国内访问速度较快。

1. 访问 [Zeabur](https://zeabur.com)
2. 使用 GitHub 登录
3. 点击 **New Project**
4. 选择 `Nolan180940/SiliconFlow-NextChat`
5. 添加环境变量 `SILICONFLOW_API_KEY`
6. 点击 Deploy

---

## 4. 使用指南

### 4.1 首次配置

1. 打开部署好的网站
2. 点击左下角 **设置** (Settings)
3. 在「模型提供商」中选择 **SiliconFlow**
4. 输入你的 SiliconFlow API Key
5. 保存并开始对话

### 4.2 选择模型

在聊天界面顶部，可以选择不同的模型：

- **DeepSeek-R1**：推理能力强，适合数学、编程问题
- **Qwen2.5-72B**：综合能力强，性价比高
- **GLM-4-Flash**：免费额度多，响应速度快

### 4.3 参数调整

在设置中可以调整：

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| Temperature | 创造性控制，值越高越有创意 | 0.7 |
| Max Tokens | 最大输出 tokens | 4096 |
| System Prompt | 系统提示词 | 根据需求设置 |

---

## 5. 环境变量详解

### 5.1 必填项

| 变量名 | 说明 | 示例 |
|--------|------|------|
| `SILICONFLOW_API_KEY` | SiliconFlow API Key | `sk-xxxxxx` |

### 5.2 可选项

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `CODE` | 访问密码，多个用逗号分隔 | 无 |
| `SILICONFLOW_URL` | 自定义 API 地址 | `https://api.siliconflow.cn` |
| `HIDE_USER_API_KEY` | 禁止用户输入自己的 API Key | `0` |
| `DISABLE_GPT4` | 禁用 GPT-4 | `0` |
| `DEFAULT_MODEL` | 默认模型 | 第一个可用模型 |
| `ENABLE_MCP` | 启用 MCP 功能 | `false` |

---

## 6. 常见问题

### Q1: 部署后无法访问？

- 检查 Vercel 部署状态是否成功
- 确认环境变量 `SILICONFLOW_API_KEY` 是否正确填写
- 查看 Vercel 项目的 Runtime Logs 排查错误

### Q2: 对话没有响应？

- 检查浏览器控制台是否有错误
- 确认 API Key 有余额
- 尝试更换模型

### Q3: 响应速度慢？

- SiliconFlow 本身在国内有 CDN，速度应该较快
- 如果服务器在海外，考虑使用 Vercel 或 Zeabur 部署

### Q4: 如何更新版本？

1. 在 GitHub 上 Fork 你的仓库
2. 添加上游仓库：
   ```bash
   git remote add upstream https://github.com/Nolan180940/SiliconFlow-NextChat
   ```
3. 拉取更新：
   ```bash
   git fetch upstream
   git merge upstream/master
   ```
4. 推送到你的仓库，Vercel 会自动重新部署

---

## 7. 与原版 NextChat 的区别

本 fork 版本相对于原版 [ChatGPTNextWeb/NextChat](https://github.com/ChatGPTNextWeb/NextChat) 的主要改动：

1. **SiliconFlow 深度集成**
   - 预置 SiliconFlow 模型列表
   - 内置 API 代理，无需额外配置

2. **新增模型支持**
   - DeepSeek-V4-Pro
   - MiniMax-M2.5-Pro
   - 更多推理模型

3. **国内优化**
   - 默认使用国内 API 端点
   - 无需代理即可访问

---

## 8. 相关链接

- 📦 **GitHub 仓库**：[Nolan180940/SiliconFlow-NextChat](https://github.com/Nolan180940/SiliconFlow-NextChat)
- 🌐 **在线演示**：[silicon-flow-next-chat.vercel.app](https://silicon-flow-next-chat.vercel.app/)
- 💬 **SiliconFlow 官网**：[siliconflow.cn](https://www.siliconflow.cn)
- 📖 **原版 NextChat**：[ChatGPTNextWeb/NextChat](https://github.com/ChatGPTNextWeb/NextChat)

---

*文档版本：v1.0 | 最后更新：2026-07-27*