# 🚀 Supabase 后端搭建指南 — 个人博客模板

> 从零开始，搭建 Serverless 博客后端。前端纯静态页面 + Quill 富文本编辑器，后端 Supabase PostgreSQL。所有可配置内容集中在 `CONFIG` 对象中，改一处全局生效。

---

## 目录

1. [注册 & 创建项目](#1-注册--创建项目)
2. [获取 API 密钥](#2-获取-api-密钥)
3. [设计数据库表](#3-设计数据库表)
4. [插入测试数据](#4-插入测试数据)
5. [安全策略说明](#5-安全策略说明)
6. [在前端连接 Supabase](#6-在前端连接-supabase)
7. [部署到 GitHub Pages](#7-部署到-github-pages)
8. [前端架构说明](#8-前端架构说明)

---

## 1. 注册 & 创建项目

### 1.1 注册账号

1. 打开 [supabase.com](https://supabase.com/)
2. 点击右上角 **"Start your project"**
3. 选择用 **GitHub** 登录（推荐），或使用邮箱注册
4. 完成注册后进入 Supabase Dashboard

### 1.2 创建新项目

1. 在 Dashboard 中，点击 **"New project"**
2. 填写：

| 字段 | 说明 | 示例 |
|:---|:---|:---|
| **Name** | 项目名称 | `my-blog` |
| **Database Password** | 数据库密码 | 生成强密码并**妥善保存** |
| **Region** | 服务器区域 | Northeast Asia（Tokyo）|
| **Pricing Plan** | 付费计划 | **Free**（500MB 数据库，足够个人博客）|

3. 点击 **"Create new project"**，等待 1-2 分钟初始化。

> 创建完成后，你会得到一个 **Project URL**（形如 `https://xxxxxxxxxxxx.supabase.co`），后面会用到。

---

## 2. 获取 API 密钥

进入项目 → 左侧菜单 **Settings** → **API**：

### 🔑 Project URL
```
https://xxxxxxxxxxxx.supabase.co
```
> 即 `CONFIG.supabaseUrl`，前端所有请求发往此地址。

### 🔑 Anon Key（匿名密钥）
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
> **公开的**客户端密钥。填入 `CONFIG.supabaseKey`。虽然任何人都能看到这个 key，但安全性通过管理密码保证——只有知道密码的人才能进入编辑模式。

### 🔒 Service Role Key ⚠️
> **绝对不要**填入 `CONFIG.supabaseKey`！此密钥绕过所有权限限制，仅用于后端脚本。

---

## 3. 设计数据库表

在左侧菜单 → **SQL Editor** → **"New query"**，粘贴并执行：

```sql
-- ========== 创建 posts 表 ==========
CREATE TABLE IF NOT EXISTS posts (
  id         BIGINT       PRIMARY KEY,        -- 文章 ID（用 Date.now() 生成）
  title      TEXT         NOT NULL,            -- 文章标题
  content    TEXT         NOT NULL DEFAULT '', -- 文章正文（Quill 输出的 HTML）
  date       TEXT         DEFAULT '',          -- 显示日期，如 "2025年11月27日"
  raw_date   TEXT         DEFAULT '',          -- ISO 日期，如 "2025-11-27"
  created_at TIMESTAMPTZ  DEFAULT NOW()        -- 数据库自动时间戳
);

-- ========== 索引 ==========
CREATE INDEX IF NOT EXISTS idx_posts_id ON posts(id DESC);
```

### 表结构说明

| 字段 | 类型 | 说明 |
|:---|:---|:---|
| `id` | `BIGINT` | 主键，用 `Date.now()` 生成毫秒时间戳 |
| `title` | `TEXT` | 文章标题 |
| `content` | `TEXT` | 文章正文，存储 Quill 编辑器输出的 **HTML** |
| `date` | `TEXT` | 中文格式日期，如 `2025年11月27日` |
| `raw_date` | `TEXT` | ISO 格式日期，如 `2025-11-27`，用于日期排序和解析 |
| `created_at` | `TIMESTAMPTZ` | 数据库自动填充的创建时间 |

> 对比旧版：这里**没有** `user_id`、`is_published`、`summary` 等字段，也**不使用** Supabase Auth。所有内容公开可见，编辑受前端管理密码保护。

---

## 4. 前端配置（CONFIG 对象）

打开 `index.html`，找到 `<script>` 标签开头的 `CONFIG` 对象。**所有需要修改的内容都在这里**：

```javascript
const CONFIG = {

  // ── Supabase 连接 ──
  supabaseUrl:  'https://YOUR-PROJECT-ID.supabase.co',  // ← 填 Project URL
  supabaseKey:  'YOUR-ANON-KEY',                         // ← 填 anon key
  adminPass:    'admin',                                  // ← 修改管理密码

  // ── 博客信息 ──
  siteTitle:    '我的博客',
  subtitle:     '— 个人空间',

  // ── 个人信息 ──
  avatarSeed:   'Blog',           // DiceBear 头像种子
  bioName:      '你的名字',
  bioSchool:    '你的学校 / 组织',
  bioText:      '一句话介绍自己<br>兴趣爱好、专业领域',
  bioTags:      ['标签1', '标签2', '标签3'],

  // ── 默认文章 ──
  defaultPosts: [ /* 3 篇文章模板 */ ],

  // ── 文章标签 ──
  postTag:      '# echo'
};
```

> 🎯 改完 CONFIG，刷新页面即可看到效果。标题、头像、个人信息全部自动更新。

在 **SQL Editor** 中运行（可选，也可以部署后在管理界面点击 "恢复默认数据"）：

```sql
INSERT INTO posts (id, title, content, date, raw_date) VALUES
(
  1000000000001,
  '你好，世界！',
  '<p>欢迎来到我的博客！这是我的第一篇文章。</p><p>这里会记录我的学习、思考和创作。</p>',
  '2026年1月1日',
  '2026-01-01'
),
(
  1000000000002,
  '关于本站',
  '<ul><li>前端：纯 HTML + CSS + JavaScript</li><li>后端：<a href="https://supabase.com">Supabase</a>（PostgreSQL）</li><li>托管：GitHub Pages</li><li>编辑器：Quill.js 富文本</li></ul>',
  '2026年1月1日',
  '2026-01-01'
),
(
  1000000000003,
  '我的项目',
  '<p>这里放一些项目链接和介绍。</p><ul><li><a href="#">项目一</a></li><li><a href="#">项目二</a></li></ul>',
  '2026年1月1日',
  '2026-01-01'
);
```

> 这些数据与 `CONFIG.defaultPosts` 中的内容一致。

---

## 6. 安全策略说明

本博客采用**前端管理密码**而非 Supabase Auth：

```
┌──────────────────────────────────────────────────────┐
│                    安全模型                            │
│                                                      │
│  访客：只能看到文章列表（前端渲染控制）                  │
│  管理员：点击 ⚙ → 输入密码 "admin" → 进入编辑模式       │
│                                                      │
│  ⚠️ 密码存储在 localStorage('is_admin_mode')          │
│  ⚠️ 数据库层面无 RLS — anon key 可读写                 │
│  ⚠️ 适合个人博客，但不适合多用户场景                    │
└──────────────────────────────────────────────────────┘
```

> 如果你需要更强的安全性，可参考旧版指南中的 RLS + Supabase Auth 方案。但对于个人博客，管理密码方案更简单实用。

---

## 7. 前端连接 Supabase（代码详解）

以下代码片段均来自 `index.html`，仅作解释，无需手动复制。

### 7.1 初始化客户端

```javascript
// 这些值来自 CONFIG 对象
const sb = window.supabase.createClient(CONFIG.supabaseUrl, CONFIG.supabaseKey);
```

### 7.2 读取文章列表

```javascript
const { data, error } = await sb
  .from('posts')
  .select('*')
  .order('id', { ascending: false });  // 按 ID 降序（最新在前）

if (error) {
  console.error('查询失败:', error.message);
} else {
  // data: [{ id, title, content, date, raw_date, created_at }, ...]
}
```

### 7.3 创建新文章

```javascript
const now = new Date();
const dateStr = `${now.getFullYear()}年${now.getMonth()+1}月${now.getDate()}日`;
const rawDate = now.toISOString().split('T')[0];

const { error } = await sb.from('posts').insert([{
  id: Date.now(),           // 毫秒时间戳作为唯一 ID
  title: '文章标题',
  content: '<p>Quill 编辑器输出的 HTML</p>',
  date: dateStr,            // "2026年7月11日"
  raw_date: rawDate         // "2026-07-11"
}]);
```

### 7.4 编辑文章

```javascript
const { error } = await sb
  .from('posts')
  .update({ title: '新标题', content: '<p>新内容</p>' })
  .eq('id', 1000000000001);  // 按 ID 定位
```

### 7.5 删除文章

```javascript
const { error } = await sb
  .from('posts')
  .delete()
  .eq('id', 1000000000001);
```

---

## 8. 部署到 GitHub Pages

### 8.1 确认配置

打开 `index.html`，确认 `CONFIG` 对象中的三项已替换：

```javascript
supabaseUrl:  'https://你的项目ID.supabase.co',  // ← 你的 Project URL
supabaseKey:  '你的anon-key',                     // ← 你的 anon key
adminPass:    '你的管理密码',                      // ← 修改默认密码
```

### 8.2 推送到 GitHub

```bash
git init
git add index.html
git commit -m "初始化博客"
git remote add origin https://github.com/你的用户名/你的仓库.git
git push -u origin main
```

### 8.3 启用 GitHub Pages

1. GitHub 仓库 → **Settings** → **Pages**
2. **Source**: Deploy from a branch → `main` → `/ (root)`
3. 点击 **Save**，等待部署完成
4. 访问 `https://你的用户名.github.io/仓库名/`

---

## 8. 前端架构说明

### 页面布局

```
┌────────────────────────────────────────────┐
│  Masthead: 我的博客.  — 个人空间       [⚙]  │
├────────────┬───────────────────────────────┤
│  Sidebar   │  文章列表                      │
│            │                               │
│  [头像]     │  ┌─ JAN ───────────────────┐  │
│  你的名字   │  │ 01  │ 标题               │  │
│  你的学校   │  │     │ 内容摘要…          │  │
│            │  │     │ # echo  [编辑][删除] │  │
│  Archives  │  └──────────────────────────┘  │
│   3 篇     │  ┌─ DEC ───────────────────┐  │
│            │  │ 31  │ 标题               │  │
│  (管理员)   │  │     │ …                 │  │
│  ✦ 新建文章 │  └──────────────────────────┘  │
│  [标题]     │                               │
│  [Quill]   │                               │
│  [发布]     │                               │
└────────────┴───────────────────────────────┘
```

### 管理模式

| 操作 | 实现 |
|:---|:---|
| 进入管理 | 点击 ⚙ → 输入密码 → 侧边栏切换为编辑器 |
| 退出管理 | 再次点击 ✕ → 恢复访客视图 |
| 状态持久化 | `localStorage.is_admin_mode` = `'1'` 保存登录状态 |
| 编辑文章 | 点击文章上的 **编辑** → 内容回填到 Quill → 修改后 **保存** |
| 删除文章 | 点击 **删除** → 确认后删除 |

### 富文本编辑器

使用 **Quill.js v1.3.7**，支持：
- **Bold** / *Italic* / <u>Underline</u>
- Blockquote（引用块）
- Code block（代码块）
- Bullet list（无序列表）
- Link（超链接）
- Image（图片嵌入）

编辑器输出为 HTML，直接存入 `posts.content` 并在前端用 `innerHTML` 渲染。

---

## 📋 检查清单

- [ ] Supabase 项目已创建
- [ ] `posts` 表已创建（SQL Editor 执行 DDL）
- [ ] 测试数据已插入
- [ ] `index.html` 中 `CONFIG.supabaseUrl` 和 `CONFIG.supabaseKey` 已替换
- [ ] 前端能正常加载文章列表
- [ ] 点击 ⚙ 输入管理密码进入管理模式
- [ ] 能新建、编辑、删除文章
- [ ] GitHub Pages 部署成功

---

## 🔧 常见问题

<details>
<summary><b>Q: 页面加载后显示 "加载中…" 不动？</b></summary>

检查浏览器控制台（F12）：
1. `CONFIG.supabaseUrl` 和 `CONFIG.supabaseKey` 是否正确
2. 网络是否能访问 `*.supabase.co`
3. CDN 资源是否被屏蔽（Quill / Supabase JS SDK）
</details>

<details>
<summary><b>Q: 创建文章报错？</b></summary>

1. 确认 SQL Editor 中 `posts` 表已创建
2. 确认 anon key 权限足够（默认可以 INSERT）
3. 检查 `id` 是否重复（`Date.now()` 在同一毫秒内可能重复）
</details>

<details>
<summary><b>Q: 忘记管理员密码？</b></summary>

密码写在 `index.html` 的 `CONFIG.adminPass` 字段中。打开文件直接查看或修改即可。
</details>

<details>
<summary><b>Q: 如何换掉默认文章？</b></summary>

修改 `index.html` 中 `CONFIG.defaultPosts` 数组，换成你的内容。修改后点击 "恢复默认数据" 即可写入数据库。
</details>

<details>
<summary><b>Q: Supabase 免费额度够用吗？</b></summary>

免费计划：500MB 数据库 + 50,000 月活用户 + 5GB 带宽。纯文本博客完全够用。如果放很多图片，建议用外部图床（如 Imgur、Cloudinary）。
</details>
