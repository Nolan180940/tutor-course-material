# 🎓 计算机科学入门教学大纲

---

## 📋 课程体系总览

| 模块 | 主题 | 核心目标 |
|:---:|:---:|:---:|
| 1 | 编程环境搭建 | 掌握开发工具，建立极客思维 |
| 2 | Python基础 | 掌握编程思维和基本语法 |
| 3 | AI与大模型 | 理解AI，会用大模型辅助编程 |
| 4 | 实战项目 | 打造个人网站，看懂开源项目 |
| 5 | Data Science入门 | 理解AI输出原理 |

---

## 🌍 模块一：编程环境搭建

### 第1课：认识VSCode——你的超级武器

**教学目标**：让学生了解VSCode是什么，为什么它是"程序员的神器"

**知识点**：
- VSCode = 写代码的编辑器 + 终端 + 文件管理器 + 调试器
- 界面介绍：左侧Explorer（文件浏览器）、底部Terminal（终端）、右侧代码区
- 为什么专业程序员都用VSCode？（插件生态、免费、开源）

**动手操作**：
1. 打开VSCode，创建第一个文件夹
2. 新建一个 `.txt` 文件，体验打字
3. 打开终端，体验第一个命令 `echo "Hello World"`

**家庭作业**：
- 在VSCode里创建一个文件夹，命名为 `my-first-project`
- 在里面新建一个文件，写上自己的名字

---

### 第2课：终端与命令行基础

**教学目标**：掌握命令行操作，这是"程序员的基本功"

**知识点**：
- 什么是终端（Terminal）？
- 常用命令：
  - `cd` = 切换文件夹 (change directory)
  - `ls` / `dir` = 查看当前文件夹内容
  - `mkdir` = 创建新文件夹 (make directory)
  - `pwd` = 查看当前在哪 (print working directory)
- 为什么程序员喜欢用命令行？（高效、酷、可以自动化）

**动手操作**：
1. 在终端里新建一个文件夹
2. 切换进去，再退出来
3. 创建一个文件并删除它

---

### 第3课：Python安装与pip

**教学目标**：安装Python，了解包管理工具

**知识点**：
- Python = 一种"像英语一样容易读"的编程语言
- pip = Python的"应用商店"，用来安装各种工具库
- 常用命令：`pip install xxx`（安装xxx包）

**动手操作**：
1. 打开终端，输入 `python --version` 确认安装成功
2. 输入 `pip install requests`，安装第一个库
3. 写第一行Python代码：`print("Hello Python!")`

---

### 第4课：Git与GitHub——程序员的社交网络

**教学目标**：理解版本控制，会用GitHub

**知识点**：
- **Git** = 时光机，可以保存代码的每个版本
- **GitHub** = 全球最大的"代码朋友圈"，可以分享自己的代码
- 什么是 `commit`、`push`、`pull`？

**动手操作**：
1. 注册GitHub账号
2. 创建一个Repository（仓库）
3. 体验上传第一段代码

**补充知识**：
- Hello GitHub: https://hellogithub.com/ （发现有趣的开源项目）

---

### 第5课：Node.js与npm（选学）

**教学目标**：了解前端开发环境

**知识点**：
- Node.js = 让JavaScript可以在服务器上运行
- npm / pnpm = JavaScript的"包管理器"
- 了解即可，不需要深入

---

## 🐍 模块二：Python基础语法

### 课程安排

| 课次 | 主题 | 内容 |
|:---:|:---|:---|
| 1 | 入门 | print、变量、input |
| 2 | 数据类型 | 字符串、数字、布尔值 |
| 3 | 条件判断 | if / else / elif |
| 4 | 循环1 | for 循环 |
| 5 | 循环2 | while 循环 |
| 6 | 函数 | def 函数定义与调用 |
| 7 | 列表 | list 创建、增删改查 |
| 8 | 元组与集合 | tuple、set |
| 9 | 字典 | dict 键值对 |
| 10 | 文件操作 | 读写文件 |
| 11 | 异常处理 | try / except |
| 12 | 面向对象 | 类与对象（选学） |

### 第1课：Hello World与变量

**第一个Python程序**：
```python
print("Hello, World!")
```

**变量** = 装数据的"盒子"：
```python
name = "小明"  # 字符串
age = 12      # 数字
is_student = True  # 布尔值

print("我叫" + name)
print("我今年" + str(age) + "岁")
```

**动手练习**：
- 写一个程序，输入你的名字和年龄，然后打印出来

---

### 第2课：数据类型

```python
# 字符串
name = "小明"
message = '你好'

# 数字
age = 12
height = 1.5
price = 19.99

# 布尔值
is_learning = True
is_done = False
```

**字符串操作**：
```python
name = "小明"
print(name.upper())  # 大写
print(name.lower())  # 小写
print(len(name))     # 长度
```

---

### 第3-5课：条件判断与循环

**条件判断**：
```python
score = 85

if score >= 90:
    print("优秀！")
elif score >= 80:
    print("良好")
else:
    print("继续努力")
```

**for循环**：
```python
for i in range(5):
    print("第" + str(i+1) + "次循环")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print("我喜欢吃" + fruit)
```

**while循环**：
```python
count = 0
while count < 5:
    print("计数：" + str(count))
    count = count + 1
```

---

### 第6课：函数

```python
def say_hello():
    print("你好！")

def greet(name):
    print("你好，" + name + "！")

def add(a, b):
    return a + b

# 调用
say_hello()
greet("小明")
result = add(3, 5)
print(result)  # 8
```

---

### 第7-11课：数据结构与文件

**列表**：
```python
fruits = ["苹果", "香蕉", "橙子"]
fruits.append("葡萄")  # 添加
fruits[0] = "草莓"     # 修改
del fruits[1]          # 删除
print(fruits[0])       # 访问
```

**字典**：
```python
student = {
    "name": "小明",
    "age": 12,
    "grade": "六年级"
}
print(student["name"])
student["score"] = 95  # 添加
```

**文件读写**：
```python
# 写入
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("你好！")

# 读取
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

---

## 🤖 模块三：AI与大模型

### 第1课：认识大模型

**什么是大语言模型（LLM）？**
- 就像一个"读过全世界所有书"的超级大脑
- 你问它问题，它会"猜"下一个最可能的词来回答

**主流AI模型梯队**：

| 梯队 | 模型 | 特点 |
|:---:|:---|:---|
| 🥇 第一梯队 | Anthropic Claude (Sonnet, Opus) | 代码能力最强 |
| 🥇 第一梯队 | OpenAI GPT-4.5 / o1 | 综合能力强 |
| 🥇 第一梯队 | Google Gemini 2.5 Pro | 多模态强 |
| 🥈 第二梯队 | xAI Grok | 实时信息 |
| 🥉 第三梯队 | MiniMax、GLM、DeepSeek、Kimi | 国内主流 |

**代码能力排名**：
- 国外：Claude > GPT > Gemini
- 国内：MiniMax > GLM > DeepSeek > Kimi

---

### 第2课：学会调用API

**什么是API？**
- API = 应用程序接口，就像"打电话"给AI服务

**基本概念**：
- `BASE_URL`：API的地址
- `API_KEY`：你的"身份证"，证明你可以使用服务
- `model`：选择用哪个模型

**实战：调用硅基流动(SiliconFlow) API**

```python
import requests

API_KEY = "你的API密钥"
BASE_URL = "https://api.siliconflow.cn/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "messages": [
        {"role": "user", "content": "你好！"}
    ]
}

response = requests.post(BASE_URL, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])
```

**动手练习**：
1. 去 SiliconFlow 注册账号：https://cloud.siliconflow.cn/
2. 获取API Key
3. 运行上面的代码，体验AI对话

---

### 第3课：Agent与MCP

**什么是Agent（智能体）？**
- Agent = AI + 工具 = 会"自己做事"的AI
- 比如：让AI自己查资料、写代码、执行命令

**MCP (Model Context Protocol)**：
- 相当于AI的"工具箱"
- 让AI可以调用外部工具（搜索、读写文件、执行代码等）

**VSCode中的Agent**：
- GitHub Copilot：代码补全
- Claude Code / 通义灵码 / Qwen Code：智能编程助手

---

### 第4课：Prompt Engineering（提示词工程）

**什么是好的Prompt？**

| ❌ 差 | ✅ 好 |
|:---|:---|
| "写代码" | "用Python写一个计算器，包含加减乘除功能，界面要简洁" |
| "帮我" | "帮我写一封邮件，语气要友好，长度约100字" |

**万能Prompt公式**：
```
角色 + 任务 + 要求 + 格式
```

示例：
```
你是一位Python老师，用通俗易懂的语言解释什么是变量，
举例说明，控制在100字以内
```

**提示词工程-提示词优化**：[PROMPT-OPTIMIZER](https://prompt.always200.com/#/basic/user)

---

## 🌐 模块四：实战项目

### 项目一：参观热门GitHub仓库

**目的**：开阔眼界，看看别人在做什么

**推荐仓库**：

| 仓库 | 简介 |
|:---|:---|
| [NextChat](https://github.com/ChatGPTNextWeb/NextChat) | AI聊天应用，可以自己部署 |
| [Anthropic Skills](https://github.com/anthropics/skills) | Claude的技能系统 |
| [md-to-word](https://github.com/Nolan180940/md-to-word) | Markdown转Word（老师的项目） |
| [PasteMD](https://github.com/RICHQAQ/PasteMD) | 一键将Markdown/AI对话粘贴到Word/WPS |
| [OpenClaw](https://github.com/openclaw/openclaw) | 开源AI助手，支持任意系统和平台 |
| [HelloGitHub](https://hellogithub.com/) | 发现有趣项目的网站 |

**动手操作**：
1. 打开一个仓库，看看README
2. 理解什么是 `star`、`fork`

---

### 项目二：打造个人主页

**目标**：用AI帮助，写一个属于自己的网站

**技术栈**：HTML + CSS + JavaScript（不需要任何框架）

**效果要求**：
- 暗色主题，极客/科技感
- 动态背景（粒子效果或数字雨）
- 打字机动画显示名字
- 三个导航卡片：博客、关于我、GitHub

**Prompt参考**：
```
创建一个单页个人导航站，使用HTML、CSS和原生JavaScript。
整体风格为暗色赛博朋克风。

1. 全屏开场：动态粒子背景 + 打字机效果显示"我是xxx，来自xxx"
2. 向下滚动后：个人头像 + 三个导航卡片
3. 响应式设计，手机端适配
```

**托管网站**：
- GitHub Pages（免费）
- Vercel（免费且简单）
- Streamlit（Python专用）

---

### 项目三：本地运行小模型（选学）

**Ollama**：在本地运行AI模型

```bash
# 安装Ollama
# 下载一个小模型试试
ollama pull phi3:mini

# 对话
ollama run phi3:mini
```

**好处**：不需要联网，可以随便问隐私问题

---

## 📊 模块五：Data Science基础

### 第1课：AI是如何"打字"的？

**流式输出原理**：
- AI不是一次性输出所有文字
- 而是一个字一个字地"猜"出来的
- 就像打字机，一个字符一个字符显示

**技术实现**：
```python
# 模拟流式输出
import time

text = "你好，我是AI助手！"
for char in text:
    print(char, end="", flush=True)
    time.sleep(0.1)  # 模拟延迟
```

---

### 第2课：了解Token

**什么是Token？**
- Token = AI理解文字的"基本单位"
- 1个中文 ≈ 1-2个Token
- 1个英文单词 ≈ 1-4个Token

**为什么重要？**
- API按Token收费
- 了解Token可以控制成本

---

## 📦 附录：环境与软件清单

### 必须安装

| 软件 | 用途 | 下载地址 |
|:---|:---|:---|
| VSCode | 代码编辑器 | https://code.visualstudio.com/ |
| Python | 编程语言 | https://www.python.org/ |
| Git | 版本控制 | https://git-scm.com/ |

### 推荐安装

| 软件 | 用途 | 备注 |
|:---|:---|:---|
| Chrome | 浏览器 | 开发必备 |
| Postman | API测试 | |
| Docker | 容器化 | 进阶 |

### AI服务

| 服务 | 用途 | 地址 |
|:---|:---|:---|
| SiliconFlow | 国内API平台 | https://cloud.siliconflow.cn/ |
| OpenAI | GPT模型 | https://platform.openai.com/ |
| Anthropic | Claude模型 | https://www.anthropic.com/ |

### 网站托管

| 服务 | 特点 | 地址 |
|:---|:---|:---|
| GitHub Pages | 免费静态网站 | github.com |
| Vercel | 简单快速 | vercel.app |
| Streamlit | Python专用 | streamlit.io |
| ngrok | 内网穿透 | ngrok.com |



