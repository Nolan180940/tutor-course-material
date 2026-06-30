# 🎓 第2课：用 Agent 打造你的第一个 Python 项目

## 🎯 今日目标

用一个**真实的小项目**，一次性学会：

| 技能 | 你会学到 |
|:---|:---|
| 🖥️ 终端命令 | `mkdir`, `cd`, `code .` |
| 🤖 AI Agent | 让 Github Copilot 帮你写代码 |
| 🌐 API | 调用 GitHub 接口拿数据 |
| 🐍 Python | `print`, `input`, `if`, `import`, 变量、字典 |
| ⏳ Git | `init`, `add`, `commit` 保存版本 |

---

## 🚀 我们要做什么？

**GitHub 用户信息查询器**

> 输入任意 GitHub 用户名 → 程序返回头像、粉丝数、仓库数

```
请输入 GitHub 用户名: torvalds

👤 用户名: torvalds
📷 头像: https://avatars.githubusercontent.com/u/1024025?v=4
👥 粉丝数: 227000+
📦 公开仓库: 8
```

---

# 🖥️ 第一步：搭建项目环境

打开 VSCode 终端（快捷键 `Ctrl + `` `），输入以下命令：

```bash
# 创建一个项目文件夹
mkdir github-finder

# 进入这个文件夹
cd github-finder

# 用 VSCode 打开当前文件夹
code .
```

> 💡 **解释**：`mkdir` = make directory（创建文件夹），`cd` = change directory（切换文件夹）

现在你有了一个空的项目文件夹，接下来让 AI 帮你写代码！

---

# 🤖 第二步：让 Agent 帮你写代码

## 打开 Cline（或 Copilot Chat）

在 VSCode 侧边栏找到 Cline 图标，在对话框里输入：

```
帮我写一个 Python 程序：
输入 GitHub 用户名，
调用 https://api.github.com/users/{用户名} 这个接口，
显示用户名、头像链接、粉丝数、公开仓库数。
```

## Agent 会做什么？

1. 📝 自动创建 `github_finder.py` 文件
2. 📦 自动安装 `requests` 库（`pip install requests`）
3. ✅ 自动运行测试

> 🎉 **神奇吧？你什么都没写，代码就有了！**

---

## Agent 大概会生成这样的代码：



```python
# 🤖 这段代码由 AI Agent (Cline) 自动生成
# 你只需要告诉它"做什么"，不需要亲自写！

import requests  # 导入 requests 库：用来发网络请求的"工具箱"

# 让用户输入 GitHub 用户名
username = input("请输入 GitHub 用户名: ")

# 拼接 API 地址（f-string：把变量塞进字符串里）
url = f"https://api.github.com/users/{username}"

# 向 GitHub 服务器发送请求
response = requests.get(url)

# 判断是否成功
if response.status_code == 200:
    # 把返回的 JSON 数据转成 Python 字典
    data = response.json()

    # 打印用户信息
    print(f"\n👤 用户名: {data['login']}")
    print(f"📷 头像: {data['avatar_url']}")
    print(f"👥 粉丝数: {data['followers']}")
    print(f"📦 公开仓库: {data['public_repos']}")
else:
    print("❌ 查不到这个用户哦，检查一下拼写！")
```

---

# 🐍 第三步：读懂代码（Python 语法速成）

别怕，我们一行一行来看：

## 1. `import requests` — 导入工具箱

Python 自带很多功能，但"发网络请求"需要额外工具。`requests` 就是这样一个库。

```
import requests   →   导入"网络请求工具箱"
```

## 2. `username = input("...")` — 变量 + 输入

```python
username = input("请输入 GitHub 用户名: ")
```

| 部分 | 含义 |
|:---|:---|
| `input("...")` | 弹出一个输入框，等用户打字 |
| `username = ...` | 把用户输入的内容放进一个叫 `username` 的盒子（**变量**） |

> 📦 **变量 = 贴了标签的盒子**，里面可以放任何东西

## 3. `f"...{username}..."` — f-string

```python
url = f"https://api.github.com/users/{username}"
```

- `f"..."` 是 f-string
- `{username}` 会被替换成变量里的内容
- 如果输入 `torvalds`，这行就变成 `https://api.github.com/users/torvalds`

## 4. `requests.get(url)` — 发请求

```python
response = requests.get(url)
```

这行代码向 GitHub 服务器"喊话"："把 torvalds 的信息给我！"
服务器返回的数据被放进 `response` 变量里。

## 5. `if response.status_code == 200:` — 条件判断

| 状态码 | 含义 |
|:---|:---|
| `200` | ✅ 成功！查到用户了 |
| `404` | ❌ 没找到这个用户 |

```python
if response.status_code == 200:
    # 成功时执行的代码
else:
    # 失败时执行的代码
```

## 6. `data['login']` — 字典取值

API 返回的数据长这样（JSON 格式）：

```json
{
  "login": "torvalds",
  "avatar_url": "https://avatars.githubusercontent.com/u/1024025?v=4",
  "followers": 227000,
  "public_repos": 8
}
```

Python 把它变成**字典（dict）**，就像查字典一样取数据：

```python
data['login']        →  "torvalds"
data['followers']    →  227000
data['public_repos'] →  8
```

---

## 📊 一张图总结今天学的 Python 语法

| 语法 | 作用 | 例子 |
|:---|:---|:---|
| `import` | 导入库 | `import requests` |
| `变量 = 值` | 存数据 | `name = "小明"` |
| `input()` | 获取用户输入 | `age = input("几岁")` |
| `f"{变量}"` | 拼字符串 | `f"你好{name}"` |
| `if ... else` | 条件判断 | `if score > 60: ...` |
| `dict['key']` | 字典取值 | `data['login']` |

---

# ▶️ 第四步：运行你的程序

在终端输入：

```bash
python github_finder.py
```

然后试试查这些用户名：

| 输入 | 是谁 |
|:---|:---|
| `torvalds` | Linux 操作系统之父 |
| `gaearon` | React 框架作者 |
| `你未来的用户名` | 你自己！ |

> 🎮 **试试看！能查到多少粉丝？**

---

# ✏️ 第五步：亲手改代码

现在试试自己修改代码！以下是几个挑战：

## 挑战 1：多加一行信息

在 `print` 区域加一行，显示用户的主页链接：

```python
print(f"🔗 主页: {data['html_url']}")
```

> 💡 提示：看看 `data` 里还有什么字段？在终端输入 `print(data)` 就能看到全部！

## 挑战 2：改输出风格

把输出改成你自己的风格：

```python
print(f"\n🔥 {data['login']} 的资料卡 🔥")
print(f"===========================")
```

## 挑战 3：加表情包

根据粉丝数量显示不同评价：

```python
if data['followers'] > 1000:
    print("🌟 这是个大佬！")
else:
    print("🌱 还在成长中，加油！")
```

> 🤖 **卡住了？问 Cline / Copilot！** 这就是 Agent 的用处。


```python
# ✏️ 在这里修改你的代码！
# 试试挑战 1、2、3

import requests

username = input("请输入 GitHub 用户名: ")
url = f"https://api.github.com/users/{username}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # 👇 在这里改输出内容
    print(f"\n👤 用户名: {data['login']}")
    print(f"📷 头像: {data['avatar_url']}")
    print(f"👥 粉丝数: {data['followers']}")
    print(f"📦 公开仓库: {data['public_repos']}")

    # 👇 挑战 1：多加一行主页链接
    # print(f"🔗 主页: {data['html_url']}")

    # 👇 挑战 3：加粉丝评价
    # if data['followers'] > 1000:
    #     print("🌟 这是个大佬！")

else:
    print("❌ 查不到这个用户哦，检查一下拼写！")
```

---

# ⏳ 第六步：用 Git 保存你的作品

Git = **时光机**，可以保存代码的每个版本，随时回到过去。

在终端输入：

```bash
# 初始化 Git 仓库（告诉 Git："开始监控这个文件夹"）
git init

# 把所有文件加入暂存区（"这些文件我要保存"）
git add .

# 提交（"咔嚓！拍一张快照"）
git commit -m "我的第一个项目：GitHub查询器"
```

| 命令 | 翻译成人话 |
|:---|:---|
| `git init` | "Git，开始工作！盯着这个文件夹" |
| `git add .` | "把所有改动打包好，准备保存" |
| `git commit -m "..."` | "咔嚓！保存当前版本，备注是..." |

> 🕰️ **以后改坏了代码？** `git checkout` 就能回到之前的版本！

---

# 📋 今日知识点清单

勾一下你今天学会的：

## 基础
- [ ] `mkdir` 创建文件夹
- [ ] `cd` 切换文件夹
- [ ] 用 Cline/Copilot 让 AI 写代码
- [ ] `import` 导入库
- [ ] 变量 `name = "小明"`
- [ ] `input()` 获取用户输入
- [ ] `f"{变量}"` 拼字符串
- [ ] `if ... else` 条件判断
- [ ] 字典 `dict['key']`
- [ ] `requests.get()` 调 API
- [ ] `git init` / `git add` / `git commit`

## 进阶 🔥
- [ ] 什么是爬虫（Crawler）
- [ ] API vs 爬虫 的区别
- [ ] `FirecrawlApp` 初始化
- [ ] `scrape_url()` 爬取网页
- [ ] 切片 `content[:500]`
- [ ] `with open(...) as f` 写入文件

---

## 🏠 课后作业

1. 查 5 个 GitHub 用户，截图你的结果
2. 用 Firecrawl 爬 3 个你喜欢的网站，保存 `.md` 文件
3. 把代码 push 到 GitHub（下次课教 `git push`）
4. 试试让 Agent 给程序加新功能：**一次性查多个用户名 + 爬多个网址**

> 🎉 **恭喜！你今天用 Agent 做了两个项目：API 查询 + 网页爬虫！**

---

# 🔥 进阶板块：用 Firecrawl 爬取网页内容

## 这是什么？

刚才我们调了 GitHub **API** 拿数据 — API 就像一个官方窗口，数据整整齐齐给你。

但世界上大部分网站**没有 API**！那怎么拿数据呢？

**Firecrawl** = 一个"网页爬虫"工具，能把任何网页的内容**自动抓下来**，转成干净的文本或 Markdown。

> 🕷️ **爬虫（Crawler）**：像一只蜘蛛，自动爬网页、抓内容。

---

## 能做什么？

| 场景 | 例子 |
|:---|:---|
| 📰 抓新闻标题 | 爬取新闻网站首页，提取所有标题 |
| 📖 抓文章内容 | 把一篇博客全文抓下来保存 |
| 🏠 抓 GitHub README | 爬自己的项目主页，看别人看到什么 |
| 🔍 批量搜资料 | 搜一个关键词，抓多个网站的结果 |

今天我们用 Firecrawl 做一个：**输入任意网址 → 返回网页的主要内容**


---

## 🛠️ 安装 Firecrawl

先装库（在终端或这个单元格运行）：

```bash
pip install firecrawl-py
```

然后设置你的 API Key。我们已经有了一个 Key，告诉 Cline / Copilot 让它帮你初始化：

> "帮我初始化 Firecrawl，API key 是 fc-xxxxx（用你的真实 key）"



```python
# 🔥 Firecrawl 爬虫演示
# 输入任意网址，抓取网页主要内容

from firecrawl import FirecrawlApp

# 初始化（请替换为你的真实 API Key）
app = FirecrawlApp(api_key="fc-YOUR-API-KEY-HERE")

# 让用户输入要爬的网址
url = input("请输入要爬取的网址: ")
print(f"\n🕷️ 正在爬取 {url} ...\n")

# 爬取网页，返回 Markdown 格式
result = app.scrape_url(url, formats=["markdown"])

# 显示结果（新版 Firecrawl 返回对象，用 .markdown 取值）
if result and result.markdown:
    content = result.markdown

    # 显示前 500 个字符（太长的话截断）
    preview = content[:500]
    print("=" * 50)
    print("📄 网页内容预览：")
    print("=" * 50)
    print(preview)

    if len(content) > 500:
        print(f"\n... 还有 {len(content) - 500} 个字符未显示")

    # 保存到文件
    with open("crawled_page.md", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ 完整内容已保存到 crawled_page.md")
else:
    print("❌ 爬取失败，请检查网址是否正确")
```


```python
# 🐛 调试：看看 Firecrawl 到底返回了什么
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR-API-KEY-HERE")

url = "https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/github_copilot"
result = app.scrape_url(url, formats=["markdown"])

# 打印原始结果，看看结构
print("=" * 50)
print("🔍 原始返回结果：")
print("=" * 50)
print(f"类型: {type(result)}")
print(f"内容: {result}")
```

---

## 📖 代码解读

```python
app = FirecrawlApp(api_key="fc-...")
```
→ 初始化爬虫，用 API Key 证明身份

```python
result = app.scrape_url(url, formats=["markdown"])
```
→ 爬取网页，要求返回 **Markdown 格式**（干净的文本，不带 HTML 标签）
> 返回的是一个**对象**，用 `.markdown` 取内容，而不是 `["markdown"]`

```python
content[:500]
```
→ 只取前 500 个字符预览（`[:500]` 是 Python 的**切片**语法）

```python
with open("crawled_page.md", "w", encoding="utf-8") as f:
    f.write(content)
```
→ 把内容**写入文件**保存起来

> 🆚 **对比 GitHub API vs Firecrawl**：
> - GitHub API → 返回**结构化 JSON**，用 `["xxx"]` 取值
> - Firecrawl → 返回**Document 对象**，用 `.xxx` 取值

---

## 🎮 试试爬这些网站

| 网址 | 会抓到什么 |
|:---|:---|
| `https://hellogithub.com` | HelloGitHub 首页的热门项目列表 |
| `https://zh.wikipedia.org/wiki/Python` | Python 的维基百科介绍 |
| `https://github.com/torvalds` | 你的 GitHub 个人主页内容 |

---

## ✏️ 挑战：做一个"任意网页摘要器"

在 Cline 里输入：

> "帮我改进 Firecrawl 程序，爬取网页后，用 `print` 显示标题、正文前 200 字，并统计总字数"

让 Agent 帮你改代码！


```python
# ✏️ 挑战区：改进你的爬虫！
# 让 Agent 帮你改成"网页摘要器"

from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR-API-KEY-HERE")
url = input("请输入要爬取的网址: ")
print(f"\n🕷️ 正在爬取...\n")

result = app.scrape_url(url, formats=["markdown"])

if result and result.markdown:
    content = result.markdown

    # 👇 在这里加你的改进代码！
    print(f"📊 总字数: {len(content)} 字")
    print(f"📄 前 200 字预览:\n{content[:200]}...")
    print(f"\n✅ 全文已保存到 crawled_page.md")

    with open("crawled_page.md", "w", encoding="utf-8") as f:
        f.write(content)
```
