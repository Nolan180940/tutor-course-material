# 行业术语黑话大全

> 涵盖前端、后端、AI、云原生、DevOps 等多领域术语的详细定义与用法指南

---

## 1. 前端开发

### 1.1 框架与库

## React

**英文原名**: React | **中文译名**: React（React.js）

- **定义**: Facebook 开发的用于构建用户界面的声明式、组件化 JavaScript 库，采用虚拟 DOM 提升渲染性能。
- **使用场景**: 单页应用（SPA）、企业级后台系统、需要频繁交互的动态界面。
- **代码示例**:
```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      点击次数: {count}
    </button>
  );
}
```
- **关联术语**: JavaScript, TypeScript, Next.js, MUI, Tailwind CSS

---

## Vue

**英文原名**: Vue.js | **中文译名**: Vue.js（渐进式 JavaScript 框架）

- **定义**: 尤雨溪创建的渐进式 JavaScript 框架，核心库只关注视图层，易于与其他库或现有项目集成。
- **使用场景**: 中小型项目、快速原型开发、需要渐进式引入的前端架构。
- **代码示例**:
```vue
<script setup>
import { ref } from 'vue'
const message = ref('Hello Vue!')
</script>

<template>
  <h1>{{ message }}</h1>
</template>
```
- **关联术语**: JavaScript, TypeScript, Nuxt.js, Vite

---

## Angular

**英文原名**: Angular | **中文译名**: Angular（Angular.js 继任者）

- **定义**: Google 维护的完整前端框架，提供依赖注入、路由、表单处理等完整解决方案。
- **使用场景**: 企业级大型应用、需要严格架构的大型团队项目。
- **代码示例**:
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: '<h1>{{ title }}</h1>'
})
export class AppComponent {
  title = 'Hello Angular';
}
```
- **关联术语**: TypeScript, RxJS, SCSS

---

## Svelte

**英文原名**: Svelte | **中文译名**: Svelte（编译型前端框架）

- **定义**: Rich Harris 创建的编译型框架，在构建时将组件转换为高效的命令式代码，无需虚拟 DOM。
- **使用场景**: 追求极致性能的小型应用、交互密集型界面、需要小 bundle 体积的项目。
- **代码示例**:
```svelte
<script>
  let count = 0;
</script>

<button on:click={() => count++}>
  点击次数: {count}
</button>
```
- **关联术语**: JavaScript, TypeScript, SvelteKit, Vite

---

## SolidJS

**英文原名**: SolidJS | **中文译名**: SolidJS（响应式前端框架）

- **定义**: 类似 React 但使用细粒度响应式系统的框架，组件只渲染一次，通过响应式原语更新 DOM。
- **使用场景**: 需要高性能的复杂交互应用、对 bundle 大小有严格要求的项目。
- **代码示例**:
```jsx
import { createSignal } from 'solid-js';

function Counter() {
  const [count, setCount] = createSignal(0);
  return <button onClick={() => setCount(c => c + 1)}>{count()}</button>;
}
```
- **关联术语**: JavaScript, TypeScript, JSX

---

## Next.js

**英文原名**: Next.js | **中文译名**: Next.js（React 全栈框架）

- **定义**: Vercel 开发的 React 全栈框架，支持服务端渲染（SSR）、静态站点生成（SSG）、API 路由等功能。
- **使用场景**: 需要 SEO 优化的网站、企业级 Web 应用、全栈 JavaScript 项目。
- **代码示例**:
```typescript
// app/page.tsx
export default function Home() {
  return <h1>欢迎来到 Next.js</h1>;
}

// app/api/hello/route.ts
export async function GET() {
  return Response.json({ message: 'Hello!' });
}
```
- **关联术语**: React, TypeScript, Vercel, Tailwind CSS

---

## Nuxt.js

**英文原名**: Nuxt.js | **中文译名**: Nuxt.js（Vue 全栈框架）

- **定义**: Vue 的全栈框架，提供自动导入、路由管理、SSR/SSG 支持，类似于 Vue 生态的 Next.js。
- **使用场景**: Vue 项目的全栈开发、需要 SEO 的 Vue 应用、企业级 Vue 项目。
- **代码示例**:
```vue
<!-- pages/index.vue -->
<template>
  <div>
    <h1>欢迎来到 Nuxt</h1>
    <NuxtLink to="/about">关于页面</NuxtLink>
  </div>
</template>
```
- **关联术语**: Vue, TypeScript, Vercel

---

## SvelteKit

**英文原名**: SvelteKit | **中文译名**: SvelteKit（Svelte 全栈框架）

- **定义**: Svelte 的官方全栈框架，提供文件-based 路由、SSR、API 端点等功能。
- **使用场景**: Svelte 项目的全栈开发、高性能 Web 应用。
- **代码示例**:
```svelte
<!-- src/routes/+page.svelte -->
<script>
  export let data;
</script>

<h1>{data.title}</h1>
```
- **关联术语**: Svelte, TypeScript, Vercel

---

## Electron

**英文原名**: Electron | **中文译名**: Electron（跨平台桌面应用框架）

- **定义**: GitHub 开发的框架，使用 Chromium + Node.js 构建跨平台桌面应用，支持 Windows、macOS、Linux。
- **使用场景**: 桌面应用开发、需要原生系统能力的 Web 技术项目、跨平台工具软件。
- **代码示例**:
```javascript
const { app, BrowserWindow } = require('electron');

function createWindow() {
  const win = new BrowserWindow({ width: 800, height: 600 });
  win.loadFile('index.html');
}

app.whenReady().then(createWindow);
```
- **关联术语**: Node.js, JavaScript, Chromium

---

## Tauri

**英文原名**: Tauri | **中文译名**: Tauri（轻量级桌面/移动应用框架）

- **定义**: 使用 Rust 后端 + Web 前端的轻量级跨平台应用框架，生成的二进制文件体积远小于 Electron。
- **使用场景**: 需要小体积应用的项目、对性能要求高的桌面应用、移动端应用。
- **代码示例**:
```rust
// src-tauri/src/main.rs
fn main() {
    tauri::Builder::default()
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```
- **关联术语**: Rust, WebView, React, Vue

---

### 1.2 UI 组件库

## MUI

**英文原名**: Material-UI (MUI) | **中文译名**: MUI（Material Design 组件库）

- **定义**: 实现 Google Material Design 规范的 React 组件库，提供丰富的预制 UI 组件。
- **使用场景**: 需要 Material Design 风格的企业应用、快速开发 React UI。
- **代码示例**:
```jsx
import { Button, TextField } from '@mui/material';

function Form() {
  return (
    <div>
      <TextField label="用户名" />
      <Button variant="contained">提交</Button>
    </div>
  );
}
```
- **关联术语**: React, TypeScript, CSS

---

## Ant Design

**英文原名**: Ant Design | **中文译名**: Ant Design（蚂蚁金服组件库）

- **定义**: 蚂蚁金服开源的企业级 React 组件库，提供丰富的中文文档和设计规范。
- **使用场景**: 中后台管理系统、企业内部应用、需要复杂表单和表格的项目。
- **代码示例**:
```jsx
import { Button, Table, Form, Input } from 'antd';

function UserTable() {
  const columns = [{ title: '姓名', dataIndex: 'name' }];
  return <Table columns={columns} dataSource={data} />;
}
```
- **关联术语**: React, TypeScript, JavaScript

---

## NaiveUI

**英文原名**: Naive UI | **中文译名**: NaiveUI（Vue 3 组件库）

- **定义**: 基于 Vue 3 的 TypeScript 组件库，提供简洁美观的 UI 组件，API 设计友好。
- **使用场景**: Vue 3 项目、需要现代简洁 UI 的应用。
- **代码示例**:
```vue
<script setup>
import { NButton, NInput } from 'naive-ui';
</script>

<template>
  <NInput placeholder="请输入内容" />
  <NButton type="primary">提交</NButton>
</template>
```
- **关联术语**: Vue, TypeScript, Vite

---

## Tailwind CSS

**英文原名**: Tailwind CSS | **中文译名**: Tailwind CSS（实用优先 CSS 框架）

- **定义**: 实用优先（utility-first）的 CSS 框架，通过组合类名实现样式，无需编写自定义 CSS。
- **使用场景**: 快速原型开发、需要高度定制化 UI 的项目、React/Vue 项目。
- **代码示例**:
```html
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  点击我
</button>

<div class="flex items-center justify-between p-4">
  <span class="text-gray-700">内容区域</span>
</div>
```
- **关联术语**: CSS, PostCSS, Next.js, React, Vue

---

### 1.3 基础技术

## HTML

**英文原名**: HyperText Markup Language | **中文译名**: HTML（超文本标记语言）

- **定义**: 构建网页的基础标记语言，用于定义网页的结构和内容。
- **使用场景**: 所有 Web 页面开发、邮件模板、静态页面。
- **代码示例**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>页面标题</title>
</head>
<body>
  <header>
    <h1>欢迎</h1>
  </header>
  <main>
    <p>这是一个段落。</p>
  </main>
</body>
</html>
```
- **关联术语**: CSS, JavaScript, HTTP

---

## CSS

**英文原名**: Cascading Style Sheets | **中文译名**: CSS（层叠样式表）

- **定义**: 用于控制网页外观和布局的样式语言，支持选择器、盒模型、Flexbox、Grid 等布局方式。
- **使用场景**: Web 页面样式设计、响应式布局、动画效果。
- **代码示例**:
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}

.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
```
- **关联术语**: HTML, JavaScript, Tailwind CSS, SCSS

---

## JavaScript

**英文原名**: JavaScript | **中文译名**: JavaScript（网页脚本语言）

- **定义**: 浏览器原生支持的脚本语言，是 Web 三大核心技术之一（HTML + CSS + JS）。
- **使用场景**: 前端交互开发、后端服务开发（Node.js）、桌面/移动应用。
- **代码示例**:
```javascript
// 异步函数
async function fetchData(url) {
  const response = await fetch(url);
  return response.json();
}

// 数组方法
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
console.log(doubled); // [2, 4, 6, 8, 10]
```
- **关联术语**: HTML, CSS, TypeScript, Node.js, React, Vue

---

## TypeScript

**英文原名**: TypeScript | **中文译名**: TypeScript（类型安全 JavaScript）

- **定义**: JavaScript 的超集，提供静态类型检查和最新的 ECMAScript 特性，编译为纯 JavaScript。
- **使用场景**: 大型项目开发、需要类型安全的代码库、企业级应用。
- **代码示例**:
```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

function greetUser(user: User): string {
  return `你好，${user.name}！`;
}

const user: User = { id: 1, name: '张三', email: 'zhangsan@example.com' };
console.log(greetUser(user));
```
- **关联术语**: JavaScript, React, Vue, Node.js, VS Code

---

### 1.4 数据格式

## JSON

**英文原名**: JavaScript Object Notation | **中文译名**: JSON（JavaScript 对象表示法）

- **定义**: 轻量级的数据交换格式，易于人类阅读和编写，也易于机器解析和生成。
- **使用场景**: API 数据传输、配置文件、前后端数据交换。
- **代码示例**:
```json
{
  "name": "张三",
  "age": 25,
  "skills": ["JavaScript", "Python", "Go"],
  "address": {
    "city": "北京",
    "district": "朝阳区"
  }
}
```
- **关联术语**: JavaScript, REST API, YAML

---

## JSONL

**英文原名**: JSON Lines | **中文译名**: JSONL（JSON 行格式）

- **定义**: 每行一个有效 JSON 对象的格式，适合处理大规模流式数据。
- **使用场景**: 日志处理、大模型训练数据、批量数据导入导出。
- **代码示例**:
```jsonl
{"prompt": "你好", "completion": "你好！有什么可以帮助你的吗？"}
{"prompt": "今天天气怎么样", "completion": "今天天气晴朗，适合外出。"}
{"prompt": "讲个笑话", "completion": "为什么程序员总是弄坏他们的键盘？因为他们总是按 Ctrl+Alt+Del！"}
```
- **关联术语**: JSON, LLM, 训练数据

---

## YAML

**英文原名**: YAML Ain't Markup Language | **中文译名**: YAML（人类友好的数据序列化语言）

- **定义**: 强调可读性的数据序列化格式，使用缩进表示层级，常见于配置文件。
- **使用场景**: 配置文件（Docker Compose、Kubernetes、CI/CD）、数据交换。
- **代码示例**:
```yaml
# Kubernetes Deployment 配置
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: my-app:latest
        ports:
        - containerPort: 8080
```
- **关联术语**: JSON, TOML, Kubernetes, Docker

---

## TOML

**英文原名**: Tom's Obvious, Minimal Language | **中文译名**: TOML（简洁配置文件格式）

- **定义**: 强调简洁和明确的配置文件格式，比 YAML 更适合机器解析。
- **使用场景**: Python 项目配置（pyproject.toml）、Rust 项目配置（Cargo.toml）。
- **代码示例**:
```toml
# Cargo.toml
[package]
name = "my-project"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }

[build-dependencies]
```

```toml
# pyproject.toml
[project]
name = "my-package"
version = "0.1.0"
requires-python = ">=3.9"

[project.optional-dependencies]
dev = ["pytest", "black"]
```
- **关联术语**: YAML, JSON, Python, Rust

---

## XML

**英文原名**: Extensible Markup Language | **中文译名**: XML（可扩展标记语言）

- **定义**: 早期的结构化数据格式，支持自定义标签，用于表示结构化数据。
- **使用场景**: 配置文件（传统 Java 项目）、SOAP API、Office 文档格式。
- **代码示例**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<users>
  <user id="1">
    <name>张三</name>
    <email>zhangsan@example.com</email>
  </user>
  <user id="2">
    <name>李四</name>
    <email>lisi@example.com</email>
  </user>
</users>
```
- **关联术语**: HTML, JSON, SOAP

---

## CSV

**英文原名**: Comma-Separated Values | **中文译名**: CSV（逗号分隔值）

- **定义**: 简单的表格数据格式，每行用逗号分隔字段，适合大规模数据导出。
- **使用场景**: 数据导出/导入、Excel 数据交换、机器学习数据集。
- **代码示例**:
```csv
姓名,年龄,城市,职业
张三,28,北京,软件工程师
李四,32,上海,产品经理
王五,25,深圳,设计师
赵六,30,广州,数据分析师
```
- **关联术语**: JSON, Excel, 数据分析

---

## 2. 后端开发

### 2.1 编程语言

## Go

**英文原名**: Go | **中文译名**: Go（Go 语言/Golang）

- **定义**: Google 2009 年发布的编译型语言，以简洁语法、高并发支持和快速编译著称。
- **使用场景**: 云原生服务、微服务、容器编排工具（Kubernetes、Docker）、高并发 API。
- **代码示例**:
```go
package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}
```
- **关联术语**: Gin, Docker, Kubernetes, gRPC

---

## Rust

**英文原名**: Rust | **中文译名**: Rust（Rust 语言）

- **定义**: Mozilla 开发的系统编程语言，以内存安全、零成本抽象和并发安全为核心特性。
- **使用场景**: 系统编程、WebAssembly、高性能组件、Tauri 后端、区块链开发。
- **代码示例**:
```rust
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Mutex::new(0);
    let handles: Vec<_> = (0..10).map(|_| {
        thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        })
    }).collect();

    for handle in handles {
        handle.join().unwrap();
    }
    
    println!("结果: {}", *counter.lock().unwrap());
}
```
- **关联术语**: Tauri, WebAssembly, Cargo

---

## Kotlin

**英文原名**: Kotlin | **中文译名**: Kotlin（Kotlin 语言）

- **定义**: JetBrains 开发的 JVM 语言，与 Java 完全互操作，语法更简洁，支持空安全。
- **使用场景**: Android 开发、后端服务（Spring Boot）、JVM 系项目。
- **代码示例**:
```kotlin
data class User(val name: String, val email: String)

fun main() {
    val user = User("张三", "zhangsan@example.com")
    println("用户: ${user.name}, 邮箱: ${user.email}")
    
    // 列表操作
    val numbers = listOf(1, 2, 3, 4, 5)
    val doubled = numbers.map { it * 2 }
    println(doubled) // [2, 4, 6, 8, 10]
}
```
- **关联术语**: Java, Spring Boot, Android

---

## Python

**英文原名**: Python | **中文译名**: Python（Python 语言）

- **定义**:Guido van Rossum 创建的动态解释型语言，语法简洁易读，拥有丰富的生态系统。
- **使用场景**: AI/机器学习、数据分析、Web 后端、自动化脚本、DevOps 工具。
- **代码示例**:
```python
from dataclasses import dataclass
from typing import List

@dataclass
class User:
    name: str
    email: str
    
    def greet(self) -> str:
        return f"你好，我是 {self.name}！"

# 异步 HTTP 请求
import aiohttp

async def fetch_data(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```
- **关联术语**: Django, Flask, FastAPI, LangChain, pip

---

## Java

**英文原名**: Java | **中文译名**: Java（Java 语言）

- **定义**: Sun Microsystems 1995 年发布的面向对象语言，"一次编写，到处运行"，企业级后端主流语言。
- **使用场景**: 企业级后端系统、Android 应用（历史版本）、大数据处理、Spring 生态。
- **代码示例**:
```java
// Spring Boot 控制器
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
        return userService.findById(id);
    }
    
    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.save(user);
    }
}
```
- **关联术语**: Spring Boot, JVM, Kotlin, Maven

---

## Node.js

**英文原名**: Node.js | **中文译名**: Node.js（Node 运行时）

- **定义**: 基于 Chrome V8 引擎的 JavaScript 运行时，允许在服务端执行 JavaScript。
- **使用场景**: 实时 Web 应用、API 服务器、微服务、Electron 桌面应用后端。
- **代码示例**:
```javascript
const express = require('express');
const app = express();

app.get('/api/users/:id', async (req, res) => {
  const user = await getUserById(req.params.id);
  res.json(user);
});

app.listen(3000, () => {
  console.log('服务器运行在 http://localhost:3000');
});
```
- **关联术语**: JavaScript, Express, npm, TypeScript

---

### 2.2 后端框架

## Express

**英文原名**: Express.js | **中文译名**: Express.js（Node.js Web 框架）

- **定义**: Node.js 最流行的 Web 框架，简洁灵活，提供中间件机制和路由功能。
- **使用场景**: 快速构建 REST API、原型开发、小型 Web 应用、微服务。
- **代码示例**:
```javascript
const express = require('express');
const app = express();

// 中间件
app.use(express.json());

// 路由
app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello World!' });
});

app.post('/api/users', (req, res) => {
  const newUser = req.body;
  // 保存用户...
  res.status(201).json(newUser);
});

app.listen(3000);
```
- **关联术语**: Node.js, JavaScript, REST API, npm

---

## NestJS

**英文原名**: NestJS | **中文译名**: NestJS（Node.js 企业级框架）

- **定义**: 基于 TypeScript 的渐进式 Node.js 框架，灵感来自 Angular，采用模块化架构。
- **使用场景**: 企业级 Node.js 应用、需要清晰架构的中大型项目、微服务。
- **代码示例**:
```typescript
// users.controller.ts
@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get(':id')
  async findOne(@Param('id') id: string) {
    return this.usersService.findOne(+id);
  }

  @Post()
  async create(@Body() createUserDto: CreateUserDto) {
    return this.usersService.create(createUserDto);
  }
}
```
- **关联术语**: TypeScript, Node.js, Express, GraphQL

---

## Django

**英文原名**: Django | **中文译名**: Django（Python 全栈框架）

- **定义**: Python 高级 Web 框架，强调快速开发和简洁实用的设计原则。
- **使用场景**: Python Web 开发、内容管理系统、REST API、快速原型。
- **代码示例**:
```python
# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# views.py
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```
- **关联术语**: Python, REST API, PostgreSQL, ORM

---

## Flask

**英文原名**: Flask | **中文译名**: Flask（Python 轻量级框架）

- **定义**: Python 轻量级 Web 框架，核心简单但可通过扩展增强功能。
- **使用场景**: 小型 Web 应用、REST API、微服务原型、机器学习模型部署。
- **代码示例**:
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    return jsonify(user)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = create_new_user(data)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(debug=True)
```
- **关联术语**: Python, REST API, SQLAlchemy

---

## Spring Boot

**英文原名**: Spring Boot | **中文译名**: Spring Boot（Java 企业级框架）

- **定义**: Spring 框架的简化配置版本，提供自动配置和嵌入式服务器，快速构建生产级应用。
- **使用场景**: Java 企业级后端、微服务、REST API、Spring 生态项目。
- **代码示例**:
```java
// 主类
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

// 控制器
@RestController
@RequestMapping("/api")
public class HelloController {
    
    @GetMapping("/hello")
    public Map<String, String> hello() {
        return Map.of("message", "Hello, World!");
    }
}
```
- **关联术语**: Java, Maven, Gradle, Kotlin

---

## FastAPI

**英文原名**: FastAPI | **中文译名**: FastAPI（Python 高性能框架）

- **定义**: 现代快速的 Python Web 框架，基于类型提示自动生成 API 文档，性能接近 Go。
- **使用场景**: Python REST API、高性能微服务、异步请求处理、机器学习模型部署。
- **代码示例**:
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    user = await db.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user

@app.post("/api/users")
async def create_user(user: User):
    new_user = await db.create_user(user)
    return new_user
```
- **关联术语**: Python, Pydantic, Uvicorn, OpenAPI

---

## Gin

**英文原名**: Gin | **中文译名**: Gin（Go Web 框架）

- **定义**: Go 语言的高性能 Web 框架，API 简洁，渲染速度快。
- **使用场景**: Go 高性能 API 服务、微服务、高并发后端。
- **代码示例**:
```go
package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type User struct {
    Name  string `json:"name"`
    Email string `json:"email"`
}

func main() {
    r := gin.Default()
    
    r.GET("/api/users/:id", func(c *gin.Context) {
        id := c.Param("id")
        c.JSON(http.StatusOK, gin.H{
            "id":   id,
            "name": "张三",
        })
    })
    
    r.POST("/api/users", func(c *gin.Context) {
        var user User
        if err := c.ShouldBindJSON(&user); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }
        c.JSON(http.StatusCreated, user)
    })
    
    r.Run(":8080")
}
```
- **关联术语**: Go, REST API, Docker

---

### 2.3 数据库

## SQLite

**英文原名**: SQLite | **中文译名**: SQLite（嵌入式数据库）

- **定义**: 轻量级嵌入式关系型数据库，整个数据库存储在一个文件中，无需独立服务器进程。
- **使用场景**: 移动应用、嵌入式系统、小型网站、开发和测试环境。
- **代码示例**:
```python
import sqlite3

# 连接数据库（文件不存在则创建）
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# 插入数据
cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('张三', 'zhangsan@example.com'))
conn.commit()

# 查询
cursor.execute('SELECT * FROM users')
for row in cursor.fetchall():
    print(row)

conn.close()
```
- **关联术语**: SQL, Python, Django, Flask

---

## PostgreSQL

**英文原名**: PostgreSQL | **中文译名**: PostgreSQL（高级关系型数据库）

- **定义**: 功能最强大的开源关系型数据库，支持复杂查询、事务、存储过程、JSON 等。
- **使用场景**: 企业级应用、地理信息系统（GIS）、需要复杂数据处理的项目。
- **代码示例**:
```sql
-- 创建扩展
CREATE EXTENSION IF NOT EXISTS postgis;

-- 创建表
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB
);

-- 复杂查询
SELECT 
    u.name,
    COUNT(o.id) as order_count,
    SUM(o.amount) as total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id
HAVING COUNT(o.id) > 5
ORDER BY total_spent DESC;
```
- **关联术语**: SQL, MySQL, Docker, Prisma

---

## MySQL

**英文原名**: MySQL | **中文译名**: MySQL（流行关系型数据库）

- **定义**: Oracle 旗下的开源关系型数据库，最流行的 Web 数据库之一，性能优秀。
- **使用场景**: Web 应用、内容管理系统、电子商务平台、LAMP/LEMP 栈。
- **代码示例**:
```sql
-- 创建数据库和表
CREATE DATABASE IF NOT EXISTS myapp;
USE myapp;

CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    author_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users(id)
);

-- 插入和查询
INSERT INTO posts (title, content, author_id) VALUES 
    ('第一篇文章', '内容...', 1),
    ('第二篇文章', '内容...', 1);

SELECT p.*, u.name as author_name 
FROM posts p
JOIN users u ON p.author_id = u.id
WHERE p.created_at >= '2024-01-01'
ORDER BY p.created_at DESC;
```
- **关联术语**: SQL, PHP, Node.js, Docker

---

## MongoDB

**英文原名**: MongoDB | **中文译名**: MongoDB（文档型数据库）

- **定义**: 最流行的 NoSQL 文档数据库，使用 JSON 风格文档存储，灵活易扩展。
- **使用场景**: 内容管理系统、日志系统、快速原型、需要灵活数据模型的项目。
- **代码示例**:
```javascript
// 使用 mongoose (Node.js)
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, unique: true },
  age: Number,
  address: {
    city: String,
    country: String
  },
  tags: [String]
});

const User = mongoose.model('User', userSchema);

// 插入文档
const newUser = await User.create({
  name: '张三',
  email: 'zhangsan@example.com',
  age: 28,
  tags: ['developer', 'python']
});

// 查询
const users = await User.find({
  tags: { $in: ['developer'] }
}).sort({ createdAt: -1 });
```
- **关联术语**: NoSQL, JSON, Node.js, Mongoose

---

## Redis

**英文原名**: Redis | **中文译名**: Redis（内存数据结构存储）

- **定义**: 开源的内存键值存储，支持字符串、哈希、列表、集合、有序集合等多种数据结构。
- **使用场景**: 缓存系统、会话存储、消息队列、实时排行榜、分布式锁。
- **代码示例**:
```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# 字符串操作
r.set('user:1:name', '张三')
r.setex('token:abc123', 3600, 'user_session_data')

name = r.get('user:1:name').decode()
print(f"用户名: {name}")

# 哈希操作
r.hset('user:1', mapping={
    'name': '张三',
    'email': 'zhangsan@example.com',
    'age': '28'
})
user_info = r.hgetall('user:1')
print(user_info)

# 列表操作
r.lpush('recent_searches', 'Python 教程')
r.lpush('recent_searches', 'Redis 入门')
recent = r.lrange('recent_searches', 0, 4)

# 有序集合（排行榜）
r.zadd('leaderboard', {'player1': 100, 'player2': 95, 'player3': 90})
top3 = r.zrevrange('leaderboard', 0, 2, withscores=True)
```
- **关联术语**: 缓存, 消息队列, Docker, Python

---

## Elasticsearch

**英文原名**: Elasticsearch | **中文译名**: Elasticsearch（分布式搜索引擎）

- **定义**: 基于 Lucene 的分布式搜索和分析引擎，提供全文搜索、结构化搜索、分析等功能。
- **使用场景**: 全文搜索、日志分析（ELK 栈）、业务数据分析、实时应用搜索。
- **代码示例**:
```python
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])

# 创建索引
es.indices.create(index='products', body={
    'mappings': {
        'properties': {
            'name': {'type': 'text', 'analyzer': 'ik_max_word'},
            'price': {'type': 'float'},
            'category': {'type': 'keyword'},
            'tags': {'type': 'keyword'}
        }
    }
})

# 索引文档
es.index(index='products', id=1, body={
    'name': 'iPhone 15 Pro',
    'price': 7999.0,
    'category': '手机',
    'tags': ['苹果', '手机', '旗舰']
})

# 搜索
result = es.search(index='products', body={
    'query': {
        'multi_match': {
            'query': 'iPhone',
            'fields': ['name', 'tags']
        }
    },
    'aggs': {
        'categories': {'terms': {'field': 'category'}}
    }
})

for hit in result['hits']['hits']:
    print(hit['_source'])
```
- **关联术语**: 全文搜索, ELK, 日志分析, Docker

---

### 2.4 ORM 与工具

## Prisma

**英文原名**: Prisma | **中文译名**: Prisma（Node.js/TypeScript ORM）

- **定义**: 现代的数据库 ORM，提供类型安全的数据库访问，支持 PostgreSQL、MySQL、SQLite 等。
- **使用场景**: TypeScript/Node.js 项目、需要类型安全的数据库操作、快速开发。
- **代码示例**:
```typescript
// schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  name      String
  email     String   @unique
  posts     Post[]
  createdAt DateTime @default(now())
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  author    User     @relation(fields: [authorId], references: [id])
  authorId  Int
}

// 代码中使用
import { PrismaClient } from '@prisma/client'
const prisma = new PrismaClient()

const user = await prisma.user.create({
  data: {
    name: '张三',
    email: 'zhangsan@example.com',
    posts: {
      create: {
        title: '我的第一篇文章',
        content: '内容...'
      }
    }
  },
  include: { posts: true }
})
```
- **关联术语**: TypeScript, Node.js, PostgreSQL, MySQL

---

## Supabase

**英文原名**: Supabase | **中文译名**: Supabase（开源 Firebase 替代）

- **定义**: 开源的 Firebase 替代方案，提供 PostgreSQL 数据库、实时订阅、身份验证、存储等服务。
- **使用场景**: 快速构建 MVP、后端即服务（BaaS）、需要实时功能的应用。
- **代码示例**:
```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  'https://xxx.supabase.co',
  'your-anon-key'
)

// 认证
const { user, session } = await supabase.auth.signUp({
  email: 'user@example.com',
  password: 'password123'
})

// 数据库操作
const { data, error } = await supabase
  .from('users')
  .select('*')
  .eq('role', 'admin')
  .order('created_at', { ascending: false })

// 实时订阅
const channel = supabase
  .channel('messages')
  .on('postgres_changes', { 
    event: 'INSERT', 
    schema: 'public', 
    table: 'messages' 
  }, (payload) => {
    console.log('新消息:', payload.new)
  })
  .subscribe()
```
- **关联术语**: PostgreSQL, Firebase, 实时订阅, Docker

---

## 3. AI 与大模型

### 3.1 核心概念

## LLM

**英文原名**: Large Language Model | **中文译名**: LLM（大语言模型）

- **定义**: 基于大规模文本数据训练的语言模型，能够理解和生成人类语言，进行推理和问答。
- **使用场景**: 智能对话、文本生成、代码辅助、内容创作、知识问答。
- **代码示例**:
```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "你是一位专业的技术作家"},
        {"role": "user", "content": "请解释什么是大语言模型"}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
```
- **关联术语**: Prompt Engineering, RAG, Fine-tuning, LangChain

---

## RAG

**英文原名**: Retrieval-Augmented Generation | **中文译名**: RAG（检索增强生成）

- **定义**: 结合信息检索与大语言模型生成的技术，先从知识库检索相关文档，再让 LLM 基于检索结果生成答案。
- **使用场景**: 企业知识库、客服系统、需要引用准确来源的问答、私有数据问答。
- **代码示例**:
```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# 1. 文档加载与分块
texts = load_documents("knowledge/")
splitter = RecursiveCharacterTextSplitter(chunk_size=500)
docs = splitter.split_documents(texts)

# 2. 向量化存储
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(docs, embeddings)

# 3. 检索增强生成
def rag_query(query):
    # 检索相关文档
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])
    
    # 构建提示词
    prompt = f"""基于以下参考文档回答问题：
    
参考文档：
{context}

问题：{query}

回答："""
    
    # LLM 生成
    llm = ChatOpenAI(model_name="gpt-4")
    return llm.predict(prompt)
```
- **关联术语**: LLM, Vector Database, LangChain, Prompt Engineering

---

## Prompt Engineering

**英文原名**: Prompt Engineering | **中文译名**: Prompt Engineering（提示词工程）

- **定义**: 设计和完善向大语言模型输入的提示词，以获得更好输出的实践和技术。
- **使用场景**: 优化 LLM 输出质量、构建 AI 应用、实现特定任务自动化。
- **代码示例**:
```python
# 基础提示词
basic_prompt = "写一首关于春天的诗"

# 结构化提示词（带角色和格式）
structured_prompt = """你是一位资深软件架构师。
请为以下需求提供架构建议：

需求：构建一个支持百万并发的电商平台

请按以下格式输出：
1. 技术选型建议
2. 系统架构图（文字描述）
3. 关键挑战与解决方案
4. 性能优化建议"""

# 少样本提示词（Few-shot）
few_shot_prompt = """将以下句子转换为JSON格式：

例子：
输入：苹果 5个
输出：{"fruit": "苹果", "count": 5}

输入：香蕉 3根
输出："""

# 思维链提示词（Chain of Thought）
cot_prompt = """问题：小明有10个苹果，小红给了他5个，小明吃了3个，请问小明还有多少个苹果？

让我们一步步思考：
1. 小明原有10个苹果
2. 小红给了5个，所以 10 + 5 = 15 个
3. 小明吃了3个，所以 15 - 3 = 12 个
答案是：12个

问题：商店里有50个鸡蛋，上午卖了20个，下午又进了15个，请问现在有多少个鸡蛋？

让我们一步步思考："""
```
- **关联术语**: LLM, ReAct, Function Calling

---

## Fine-tuning

**英文原名**: Fine-tuning | **中文译名**: Fine-tuning（微调）

- **定义**: 在预训练模型基础上，使用特定领域数据进一步训练，以调整模型参数使其适应特定任务。
- **使用场景**: 构建垂直领域专家模型、降低 API 成本、提高特定任务准确率。
- **代码示例**:
```python
from openai import OpenAI

client = OpenAI()

# 创建微调任务
response = client.fine_tuning.jobs.create(
    training_file="file-abc123",  # 训练数据文件 ID
    model="gpt-4",
    hyperparameters={
        "n_epochs": 3,
        "batch_size": 2,
        "learning_rate_multiplier": 1.5
    }
)

# 训练数据格式（JSONL）
# {"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
# {"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}

# 使用微调后的模型
response = client.chat.completions.create(
    model="ft:gpt-4:your-org:model-id",
    messages=[
        {"role": "user", "content": "帮我写一封商务邮件"}
    ]
)
```
- **关联术语**: LLM, 训练数据, LoRA, RLHF

---

## Function Calling

**英文原名**: Function Calling | **中文译名**: Function Calling（函数调用）

- **定义**: LLM 根据用户请求自动调用预定义函数的能力，使 AI 能与外部系统交互。
- **使用场景**: AI 助手调用外部 API、操作数据库、控制系统、获取实时信息。
- **代码示例**:
```python
from openai import OpenAI

client = OpenAI()

# 定义可用函数
functions = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如北京、上海"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "执行数学计算",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "数学表达式，如 2+3*5"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

# 发送请求
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "北京今天天气怎么样？"}],
    tools=functions
)

# 处理函数调用
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    for call in tool_calls:
        if call.function.name == "get_weather":
            args = json.loads(call.function.arguments)
            result = get_weather(args["city"])  # 调用实际函数
```
- **关联术语**: LLM, Tool Use, LangChain

---

## Tool Use

**英文原名**: Tool Use | **中文译名**: Tool Use（工具使用）

- **定义**: AI 模型使用外部工具（如搜索引擎、数据库、API）来完成任务的能力。
- **使用场景**: 实时信息查询、数据库操作、自动化工作流、复杂任务处理。
- **代码示例**:
```python
# 使用 LangChain 的 Tool 功能
from langchain.agents import load_tools, initialize_agent
from langchain_openai import ChatOpenAI
from langchain.tools import Tool

# 定义自定义工具
def search_wikipedia(query: str) -> str:
    """搜索维基百科"""
    # 实现搜索逻辑
    return "搜索结果..."

def calculate(expression: str) -> str:
    """数学计算器"""
    return str(eval(expression))

tools = [
    Tool(
        name="wikipedia",
        func=search_wikipedia,
        description="当需要查询百科知识时使用"
    ),
    Tool(
        name="calculator",
        func=calculate,
        description="当需要进行数学计算时使用"
    )
]

# 初始化 Agent
llm = ChatOpenAI(model="gpt-4")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

# 执行任务
result = agent.run("计算 123 * 456 的结果，并告诉我牛顿是谁")
```
- **关联术语**: LLM, Function Calling, ReAct, Agent

---

## ReAct

**英文原名**: Reasoning + Acting | **中文译名**: ReAct（推理+行动框架）

- **定义**: 结合推理（Reasoning）和行动（Acting）的 AI 框架，让模型先思考再行动。
- **使用场景**: 复杂问题求解、多步骤任务、需要在行动中学习的场景。
- **代码示例**:
```python
# ReAct 提示词模式
react_prompt = """你是一个 AI 助手，需要通过推理和行动来解决问题。

请按照以下格式思考和行动：
思考：<你的推理>
行动：<你要执行的行动>
观察：<行动的结果>
...（重复直到找到答案）
最终答案：<最终结果>

问题：{question}

开始解决问题：
"""

# LangChain ReAct 实现
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.tools import Tool

tools = [
    Tool(name="Search", func=search_func, description="搜索信息"),
    Tool(name="Calculator", func=calc_func, description="数学计算")
]

agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.REACT_DOCSTORE,
    verbose=True
)

result = agent.run("爱因斯坦获得诺贝尔奖的年份是哪一年？")
```
- **关联术语**: LLM, Tool Use, Chain, Agent

---

## Chain

**英文原名**: Chain | **中文译名**: Chain（链式调用）

- **定义**: LangChain 中的核心概念，将多个处理步骤串联起来形成处理流程。
- **使用场景**: 复杂的数据处理流程、多步骤 AI 任务、流水线处理。
- **代码示例**:
```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain, SimpleSequentialChain

# 简单链
prompt = PromptTemplate(
    input_variables=["topic"],
    template="用一句话解释 {topic}："
)
chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run("机器学习")

# 顺序链（多步骤）
chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="summary")
chain2 = LLMChain(llm=llm, prompt=prompt2, input_variables=["summary"])

sequential = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["article"],
    output_variables=["final_summary"]
)

result = sequential({"article": "长文章内容..."})
```
- **关联术语**: LangChain, LLM, Agent, ReAct

---

## Agent

**英文原名**: Agent | **中文译名**: Agent（智能代理）

- **定义**: 能够自主感知环境、规划行动、执行任务的 AI 系统，可使用工具完成复杂目标。
- **使用场景**: 自动化工作流、复杂任务处理、多系统协调、智能助手。
- **代码示例**:
```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate

# 定义工具
tools = [search_tool, calculator_tool, database_tool]

# 创建 Agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个智能助手，可以调用各种工具完成任务。"),
    ("user", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 执行任务
result = agent_executor.invoke({
    "input": "帮我查一下北京今天的天气，然后提醒我带伞"
})
```
- **关联术语**: LLM, Chain, Tool Use, ReAct, LangChain

---

## MCP (Model Context Protocol)

**英文原名**: Model Context Protocol | **中文译名**: MCP（模型上下文协议）

- **定义**: Anthropic 提出的标准化协议，让 AI 模型能够安全地与外部系统和服务交互。
- **使用场景**: AI 应用与外部系统集成、标准化工具调用、安全的数据访问。
- **代码示例**:
```typescript
// MCP 服务器示例
import { MCPServer } from '@modelcontextprotocol/server';

const server = new MCPServer({
  name: 'filesystem-server',
  version: '1.0.0',
  capabilities: {
    tools: {
      read_file: {
        description: '读取文件内容',
        parameters: {
          type: 'object',
          properties: {
            path: { type: 'string', description: '文件路径' }
          },
          required: ['path']
        }
      },
      write_file: {
        description: '写入文件内容',
        parameters: {
          type: 'object',
          properties: {
            path: { type: 'string' },
            content: { type: 'string' }
          },
          required: ['path', 'content']
        }
      }
    }
  }
});

server.handle('read_file', async ({ path }) => {
  const content = await fs.promises.readFile(path, 'utf-8');
  return { content };
});

server.start();
```
- **关联术语**: LLM, Claude Code, Tool Use, Function Calling

---

## Vector Database

**英文原名**: Vector Database | **中文译名**: Vector Database（向量数据库）

- **定义**: 专门用于存储和检索高维向量数据的数据库，常用于相似性搜索和 RAG。
- **使用场景**: RAG、知识库检索、语义搜索、推荐系统、图像/音频检索。
- **代码示例**:
```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# 1. 文档向量化
texts = ["第一个文档内容", "第二个文档内容", "第三个文档内容"]
embeddings = OpenAIEmbeddings()

# 2. 存储到向量数据库
db = Chroma.from_texts(texts, embeddings, persist_directory="./chroma_db")

# 3. 相似性搜索
query = "查找相关内容"
docs = db.similarity_search(query, k=2)

# 4. 带分数的搜索
docs_with_score = db.similarity_search_with_score(query, k=2)
for doc, score in docs_with_score:
    print(f"内容: {doc.page_content}, 相似度分数: {score}")
```
- **关联术语**: RAG, LangChain, Pinecone, Weaviate, Milvus, Embedding

---

### 3.2 模型与平台

## OpenAI Compatible Completions

**英文原名**: OpenAI Compatible Completions | **中文译名**: OpenAI 兼容接口

- **定义**: 与 OpenAI API 格式兼容的接口规范，让应用可以无缝切换到不同的 LLM 提供商。
- **使用场景**: 多模型切换、成本优化、避免供应商锁定、私有化部署。
- **代码示例**:
```python
from openai import OpenAI

# 使用 OpenAI
client = OpenAI(api_key="sk-openai-xxx")

# 切换到兼容的第三方服务（如 Ollama、SiliconFlow）
client = OpenAI(
    api_key="sk-xxx",  # 第三方 API Key
    base_url="https://api.siliconflow.cn/v1"  # 第三方服务地址
)

# 使用方式完全相同
response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",  # 使用第三方模型
    messages=[{"role": "user", "content": "你好"}]
)

print(response.choices[0].message.content)
```
- **关联术语**: LLM, Ollama, vLLM, SiliconFlow, Hugging Face

---

## Hugging Face

**英文原名**: Hugging Face | **中文译名**: Hugging Face（AI 模型社区）

- **定义**: 全球最大的 AI 模型社区和平台，提供超过 100 万个预训练模型和数据集。
- **使用场景**: 模型下载、微调、数据集获取、模型部署、论文复现。
- **代码示例**:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# 下载并使用模型
model_name = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 生成文本
inputs = tokenizer("请介绍一下北京：", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(result)

# 使用 pipeline 简化
from transformers import pipeline
generator = pipeline("text-generation", model="microsoft/Phi-3-mini-4k-instruct")
result = generator("你好，请介绍一下自己", max_new_tokens=50)
```
- **关联术语**: LLM, Fine-tuning, Transformers, Ollama

---

## Ollama

**英文原名**: Ollama | **中文译名**: Ollama（本地大模型运行工具）

- **定义**: 在本地运行大语言模型的工具，支持多种开源模型，提供类似 OpenAI 的 API。
- **使用场景**: 本地部署大模型、隐私敏感场景、离线使用、开发测试。
- **代码示例**:
```bash
# 安装 Ollama
# macOS: brew install ollama
# Linux: curl -fsSL https://ollama.com/install.sh | sh

# 下载模型
ollama pull llama2
ollama pull qwen:7b
ollama pull mistral

# 运行模型
ollama run llama2 "解释一下什么是机器学习"

# API 调用
curl http://localhost:11434/api/chat -d '{
  "model": "llama2",
  "messages": [
    {"role": "user", "content": "你好"}
  ],
  "stream": false
}'
```
```python
import ollama

response = ollama.chat(
    model='llama2',
    messages=[
        {'role': 'user', 'content': '什么是 Python？'}
    ]
)
print(response['message']['content'])
```
- **关联术语**: LLM, vLLM, Docker, OpenAI Compatible

---

## vLLM

**英文原名**: vLLM | **中文译名**: vLLM（高效大模型推理引擎）

- **定义**: 伯克利大学开发的快速大模型推理框架，使用 PagedAttention 技术大幅提升吞吐量。
- **使用场景**: 大模型生产部署、高并发推理服务、私有化模型服务。
- **代码示例**:
```bash
# 使用 Docker 运行 vLLM
docker run --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    -p 8000:8000 \
    --runtime nvidia \
    vllm/vllm-openai:latest \
    --model meta-llama/Llama-2-7b-chat-hf \
    --tensor-parallel-size 1

# API 调用
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-2-7b-chat-hf",
    "messages": [{"role": "user", "content": "你好"}]
  }'
```
- **关联术语**: LLM, Ollama, SGLang, Docker, Hugging Face

---

## SGLang

**英文原名**: SGLang | **中文译名**: SGLang（大模型推理框架）

- **定义**: 开源的大模型推理框架，支持高效的多模态模型推理和复杂推理模式。
- **使用场景**: 多模态模型部署、复杂推理任务、高性能推理服务。
- **代码示例**:
```python
from sglang import sgl, runtime

# 基础推理
@sgl.function
def basic_qa(s, question):
    s += sgl.user(question)
    s += sgl.assistant(sgl.gen("answer", max_tokens=256))

result = basic_qa.run(
    question="什么是大语言模型？",
    llm=runtime.LLM("meta-llama/Llama-2-7b-chat-hf")
)
print(result["answer"])

# 思维链推理
@sgl.function
def cot_reasoning(s, problem):
    s += sgl.user(problem)
    s += sgl.assistant(
        "让我们一步步思考：\n" + 
        sgl.gen("reasoning", max_tokens=512) +
        "\n最终答案：" +
        sgl.gen("answer", max_tokens=64)
    )

result = cot_reasoning.run(problem="小明有10个苹果...")
```
- **关联术语**: LLM, vLLM, 多模态, 推理

---

### 3.3 开发框架

## LangChain

**英文原名**: LangChain | **中文译名**: LangChain（大模型应用开发框架）

- **定义**: 开发大语言模型应用的框架，提供链（Chain）、代理（Agent）、工具（Tools）等抽象。
- **使用场景**: 构建 AI 应用、RAG 系统、聊天机器人、自动化工作流。
- **代码示例**:
```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType

# 1. 基础链
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一位{role}专家"),
    ("user", "{input}")
])

chain = LLMChain(
    llm=ChatOpenAI(model="gpt-4"),
    prompt=prompt
)

result = chain.run(role="编程", input="Python 有什么优势？")

# 2. RAG 链
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

vectorstore = Chroma.from_documents(docs, embeddings)
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 3. Agent
tools = load_tools(["serpapi", "llm-math"], llm=ChatOpenAI())
agent = initialize_agent(tools, ChatOpenAI(), agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
result = agent.run("搜索最新 AI 新闻并计算 123*456")
```
- **关联术语**: LLM, RAG, Agent, Chain, Tool Use, LlamaIndex

---

## LlamaIndex

**英文原名**: LlamaIndex | **中文译名**: LlamaIndex（数据索引框架）

- **定义**: 专门用于构建知识库索引的框架，提供高效的数据摄入和检索能力。
- **使用场景**: RAG、知识库构建、文档问答、私有数据处理。
- **代码示例**:
```python
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import ChromaVectorStore

# 1. 加载文档
documents = SimpleDirectoryReader("./data").load_data()

# 2. 创建索引
index = VectorStoreIndex.from_documents(documents)

# 3. 查询
query_engine = index.as_query_engine()
response = query_engine.query("什么是机器学习？")
print(response)

# 4. 自定义向量存储
chromadb = chromadb.Client()
collection = chromadb.create_collection("my_docs")
vector_store = ChromaVectorStore(chroma_collection=collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

# 5. 结构化数据查询
from llama_index import SQLDatabase
sql_db = SQLDatabase.from_uri("sqlite:///my.db")
query_engine = sql_db.as_query_engine("SELECT * FROM users WHERE age > 20")
```
- **关联术语**: RAG, Vector Database, LangChain, 知识库

---

### 3.4 AI 工具

## Codex

**英文原名**: Codex | **中文译名**: Codex（代码生成模型）

- **定义**: OpenAI 开发的专门用于代码生成的大语言模型，是 GitHub Copilot 的核心技术。
- **使用场景**: 代码补全、代码生成、代码解释、技术文档编写。
- **代码示例**:
```python
# Codex 通过 API 调用（通过 OpenAI API）
from openai import OpenAI

client = OpenAI(api_key="your-key")

# Codex 模型（通过 codex 模型标识）
response = client.completions.create(
    model="codex",
    prompt="""# Python 函数：计算斐波那契数列
def fibonacci(n):
    '''计算第 n 个斐波那契数''',
    max_tokens=100,
    temperature=0
)

print(response.choices[0].text)
```
- **关联术语**: LLM, Copilot, 代码生成, GitHub

---

## Claude Code

**英文原名**: Claude Code | **中文译名**: Claude Code（AI 编程助手）

- **定义**: Anthropic 推出的 AI 编程助手，专注于代码编写、调试和项目级任务处理。
- **使用场景**: 代码开发、项目重构、bug 修复、技术调研、终端命令执行。
- **代码示例**:
```bash
# 安装 Claude Code CLI
npm install -g @anthropic-ai/claude-code

# 初始化项目
claude-code init

# 在项目中运行
claude-code --dangerously-skip-permissions

# 常见命令
claude-code "帮我重构这个函数"
claude-code "解释这段代码的逻辑"
claude-code "修复这个 bug"
```
- **关联术语**: Claude, AI 编程, MCP, Agent

---

## Cursor

**英文原名**: Cursor | **中文译名**: Cursor（AI 增强代码编辑器）

- **定义**: 基于 VS Code 的 AI 增强编辑器，深度集成 LLM，支持智能补全、代码生成、聊天功能。
- **使用场景**: AI 辅助编程、项目开发、代码重构、快速原型开发。
- **代码示例**:
```python
# Cursor 的核心使用方式是通过编辑器交互
# 1. Cmd+K: 生成代码
# 2. Cmd+L: 聊天窗口
# 3. Cmd+K: 编辑选中代码

# 示例：在 Cursor 中使用
# 用户输入注释 "# 创建用户注册函数"
# Cursor 自动生成：
def register_user(username: str, email: str, password: str) -> dict:
    """创建新用户"""
    if not username or not email or not password:
        raise ValueError("所有字段都是必需的")
    
    # 验证邮箱格式
    if "@" not in email:
        raise ValueError("无效的邮箱格式")
    
    # 哈希密码
    hashed_password = hash_password(password)
    
    # 保存到数据库
    user = User.create(
        username=username,
        email=email,
        password=hashed_password
    )
    
    return {"id": user.id, "username": user.username, "email": user.email}
```
- **关联术语**: VS Code, AI 编程, LLM, Copilot

---

## Windsurf

**英文原名**: Windsurf | **中文译名**: Windsurf（AI 代码编辑器）

- **定义**: Codeium 推出的 AI 代码编辑器，提供深度集成的 AI 辅助编程功能。
- **使用场景**: AI 辅助开发、代码补全、项目级 AI 任务处理。
- **代码示例**:
```python
# Windsurf 使用方式与 Cursor 类似
# 通过编辑器界面交互

# 1. Tab 键：接受 AI 建议
# 2. Cmd+Shift+I: 打开 AI 面板
# 3. 自然的语言指令

# 示例：Windsurf 生成的代码
# 用户描述："创建一个处理用户认证的模块"
# Windsurf 生成：
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional

class AuthManager:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.token_expiry = timedelta(hours=24)
    
    def hash_password(self, password: str) -> str:
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            self.secret_key.encode(),
            100000
        ).hex()
    
    def verify_password(self, password: str, hashed: str) -> bool:
        return self.hash_password(password) == hashed
    
    def create_token(self, user_id: int) -> str:
        payload = f"{user_id}:{datetime.utcnow()}"
        return secrets.token_urlsafe(32)
```
- **关联术语**: Codeium, AI 编程, VS Code

---

## Trae

**英文原名**: Trae | **中文译名**: Trae（字节跳动 AI 编程助手）

- **定义**: 字节跳动推出的 AI 编程助手，支持智能代码生成、补全和项目级任务。
- **使用场景**: AI 辅助开发、代码补全、国产 AI 工具选择。
- **代码示例**:
```python
# Trae 使用方式
# 1. 智能补全：自动补全代码
# 2. 聊天功能：解释代码、生成代码
# 3. 上下文理解：理解整个项目结构

# 示例：Trae 生成的 Web 服务
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
```
- **关联术语**: AI 编程, 字节跳动, LLM

---

## Copilot

**英文原名**: GitHub Copilot | **中文译名**: Copilot（GitHub AI 编程助手）

- **定义**: GitHub 与 OpenAI 合作推出的 AI 代码补全工具，基于 Codex 模型。
- **使用场景**: 代码补全、函数生成、注释转代码、测试生成。
- **代码示例**:
```python
# Copilot 使用方式
# 1. 注释触发：编写注释，Copilot 生成代码
# 2. Tab 接受：按 Tab 接受建议
# 3. 多行生成：生成完整函数

# 示例：注释触发 Copilot 生成
# 输入：
def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number using recursion"""
    
# Copilot 生成的代码：
def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number using recursion"""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

# 测试生成
def test_calculate_fibonacci():
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1
    assert calculate_fibonacci(10) == 55
    assert calculate_fibonacci(20) == 6765
```
- **关联术语**: GitHub, Codex, AI 编程, VS Code

---

## Opencode

**英文原名**: Opencode | **中文译名**: Opencode（开源 AI 编程助手）

- **定义**: 开源的 AI 编程助手项目，提供可自托管的代码补全和生成能力。
- **使用场景**: 私有化部署、自托管 AI 编程、开源爱好者。
- **代码示例**:
```bash
# 安装 Opencode
git clone https://github.com/your-repo/opencode.git
cd opencode
pip install -r requirements.txt

# 配置
# 编辑 config.yaml
llm:
  provider: "openai"  # 或 ollama, anthropic
  model: "gpt-4"
  api_key: "your-key"

# 运行
opencode --config config.yaml

# 使用
# 在编辑器中编写代码，Opencode 提供补全建议
```
- **关联术语**: AI 编程, 开源, LLM, 自托管

---

### 3.5 向量数据库

## Pinecone

**英文原名**: Pinecone | **中文译名**: Pinecone（云向量数据库）

- **定义**: 云原生的向量数据库服务，提供高效的向量存储和相似性搜索。
- **使用场景**: RAG、知识库搜索、推荐系统、语义检索。
- **代码示例**:
```python
from pinecone import Pinecone

# 初始化
pc = Pinecone(api_key="your-api-key")
index = pc.Index("my-index")

# 向量存储
vectors = [
    {"id": "vec1", "values": [0.1, 0.2, 0.3], "metadata": {"text": "文档1"}},
    {"id": "vec2", "values": [0.4, 0.5, 0.6], "metadata": {"text": "文档2"}}
]
index.upsert(vectors)

# 相似性搜索
query_vector = [0.1, 0.2, 0.3]
results = index.query(
    vector=query_vector,
    top_k=3,
    include_metadata=True
)

for match in results.matches:
    print(f"ID: {match.id}, Score: {match.score}, Text: {match.metadata['text']}")
```
- **关联术语**: Vector Database, RAG, LangChain, 云服务

---

## Weaviate

**英文原名**: Weaviate | **中文译名**: Weaviate（开源向量数据库）

- **定义**: 开源的向量搜索引擎，支持 GraphQL API，提供多种嵌入模型集成。
- **使用场景**: RAG、知识图谱、语义搜索、多模态搜索。
- **代码示例**:
```python
import weaviate
from weaviate import EmbeddedOptions

# 连接本地 Weaviate
client = weaviate.Client(
    embedded_options=EmbeddedOptions()
)

# 定义 schema
schema = {
    "class": "Article",
    "vectorizer": "text2vec-transformers",
    "moduleConfig": {
        "text2vec-transformers": {
            "vectorizeClassName": False
        }
    },
    "properties": [
        {"name": "title", "dataType": ["text"]},
        {"name": "content", "dataType": ["text"]}
    ]
}
client.schema.create_class(schema)

# 添加数据
client.data_object.create(
    class_name="Article",
    data_object={
        "title": "机器学习入门",
        "content": "机器学习是人工智能的一个分支..."
    }
)

# 搜索
results = client.query.get(
    "Article",
    ["title", "content"]
).with_near_text({
    "concepts": ["什么是机器学习"]
}).with_limit(3).do()

print(results)
```
- **关联术语**: Vector Database, RAG, GraphQL, Docker

---

## Milvus

**英文原名**: Milvus | **中文译名**: Milvus（开源向量数据库）

- **定义**: Linux 基金会下的开源向量数据库，支持大规模向量数据存储和检索。
- **使用场景**: 大规模向量检索、RAG、图像/视频搜索、推荐系统。
- **代码示例**:
```python
from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType, utility

# 连接
connections.connect(host='localhost', port='19530')

# 定义 schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=500)
]
schema = CollectionSchema(fields, description="文档集合")
collection = Collection("documents", schema)

# 添加索引
index_params = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128}
}
collection.create_index("embedding", index_params)

# 插入数据
import numpy as np
data = [
    [1, 2],  # ids
    [[np.random.rand(128).tolist() for _ in range(2)]],  # embeddings
    ["文档1", "文档2"]  # texts
]
collection.insert(data)

# 搜索
search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
results = collection.search(
    data=[[np.random.rand(128).tolist()]],
    anns_field="embedding",
    param=search_params,
    limit=3,
    output_fields=["text"]
)
```
- **关联术语**: Vector Database, RAG, Docker, 大规模检索

---

## 4. 云原生与 DevOps

### 4.1 云平台

## AWS

**英文原名**: Amazon Web Services | **中文译名**: AWS（亚马逊云服务）

- **定义**: Amazon 提供的全球最大云计算平台，提供计算、存储、数据库、机器学习等服务。
- **使用场景**: 企业级应用部署、云原生架构、机器学习、大数据处理。
- **代码示例**:
```python
# 使用 Boto3 操作 AWS
import boto3

# S3 操作
s3 = boto3.client('s3')
s3.upload_file('local.txt', 'my-bucket', 'remote.txt')
s3.download_file('my-bucket', 'remote.txt', 'local.txt')

# Lambda 函数
lambda_client = boto3.client('lambda')
response = lambda_client.invoke(
    FunctionName='my-function',
    InvocationType='RequestResponse',
    Payload=b'{"key": "value"}'
)

# DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')
table.put_item(Item={'user_id': '1', 'name': '张三'})
response = table.get_item(Key={'user_id': '1'})
```
- **关联术语**: EC2, S3, Lambda, Docker, Kubernetes

---

## GCP

**英文原名**: Google Cloud Platform | **中文译名**: GCP（谷歌云平台）

- **定义**: Google 提供的云计算平台，以大数据和机器学习能力著称。
- **使用场景**: 数据分析、机器学习、Google 生态集成、Kubernetes 起源。
- **代码示例**:
```python
# 使用 Google Cloud 客户端库
from google.cloud import storage, bigquery, pubsub

# Cloud Storage
client = storage.Client()
bucket = client.bucket('my-bucket')
blob = bucket.blob('remote.txt')
blob.upload_from_filename('local.txt')

# BigQuery
bq_client = bigquery.Client()
query = """
    SELECT name, COUNT(*) as count
    FROM `my-project.dataset.users`
    GROUP BY name
"""
results = bq_client.query(query)
for row in results:
    print(f"{row.name}: {row.count}")

# Pub/Sub
publisher = pubsub.PublisherClient()
topic_path = publisher.topic_path('my-project', 'my-topic')
publisher.publish(topic_path, b'消息内容'.encode())
```
- **关联术语**: Kubernetes, BigQuery, Cloud Storage, Docker

---

## Azure

**英文原名**: Microsoft Azure | **中文译名**: Azure（微软云平台）

- **定义**: Microsoft 提供的云计算平台，与 Windows/Office 生态深度集成。
- **使用场景**: 企业应用、.NET 开发、混合云、微软生态集成。
- **代码示例**:
```python
# 使用 Azure SDK
from azure.storage.blob import BlobServiceClient
from azure.cosmosdb import cosmos_client

# Blob Storage
connection_string = "DefaultEndpointsProtocol=https;AccountName=..."
blob_service = BlobServiceClient.from_connection_string(connection_string)
container = blob_service.get_container_client("my-container")
container.upload_blob("remote.txt", open("local.txt", "rb"))

# Cosmos DB
cosmos_client = cosmos_client.CosmosClient(
    url="https://my-account.documents.azure.com",
    credential="my-key"
)
database = cosmos_client.get_database_client("my-db")
container = database.get_container_client("my-container")
```
- **关联术语**: .NET, Docker, Kubernetes, Visual Studio

---

## Vercel

**英文原名**: Vercel | **中文译名**: Vercel（前 Next.js 公司）

- **定义**: 面向前端框架的云平台，专注于 Next.js 部署，提供全球 CDN 和边缘计算。
- **使用场景**: Next.js 应用部署、静态网站、Jamstack 架构、Serverless 函数。
- **代码示例**:
```bash
# Vercel CLI
npm i -g vercel

# 部署
vercel

# 或在项目中使用
# vercel.json 配置
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "outputDirectory": ".next"
}
```
```javascript
// Next.js API 路由自动部署为 Serverless
// pages/api/hello.ts
export default function handler(req, res) {
  res.status(200).json({ 
    message: 'Hello from Vercel!',
    region: process.env.VERCEL_REGION 
  });
}
```
- **关联术语**: Next.js, Serverless, CDN, Edge Functions

---

## Netlify

**英文原名**: Netlify | **中文译名**: Netlify（静态网站托管平台）

- **定义**: 面向现代 Web 的托管平台，支持静态网站、Serverless 函数、CI/CD。
- **使用场景**: 静态网站托管、Jamstack 应用、简单后端服务、自动部署。
- **代码示例**:
```toml
# netlify.toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[functions]
  directory = "functions"

# Serverless 函数
# functions/hello.js
exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({ message: "Hello from Netlify!" })
  };
};
```
- **关联术语**: 静态网站, Serverless, Jamstack, Git

---

## Cloudflare

**英文原名**: Cloudflare | **中文译名**: Cloudflare（CDN 与安全平台）

- **定义**: 全球 CDN 和网络安全公司，提供 DNS、CDN、WAF、Workers 等服务。
- **使用场景**: CDN 加速、DDoS 防护、Serverless（Workers）、域名解析。
- **代码示例**:
```javascript
// Cloudflare Workers
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const url = new URL(request.url)
  
  if (url.pathname === '/api/hello') {
    return new Response(JSON.stringify({
      message: 'Hello from Cloudflare Workers!',
      country: request.cf.country
    }), {
      headers: { 'Content-Type': 'application/json' }
    })
  }
  
  return new Response('Not Found', { status: 404 })
}
```
```bash
# Wrangler CLI 部署
npm install -g @cloudflare/wrangler
wrangler deploy
```
- **关联术语**: CDN, DNS, Serverless, Workers

---

## Railway

**英文原名**: Railway | **中文译名**: Railway（开发者云平台）

- **定义**: 面向开发者的云平台，提供一键部署、自动扩缩容、数据库集成。
- **使用场景**: 快速部署 Web 应用、原型开发、小型项目、Node.js/Go/Python 项目。
- **代码示例**:
```yaml
# railway.json
{
  "$schema": "https://railway.app/schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "numReplicas": 1,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}

# 使用 Railway CLI
railway login
railway init
railway up
railway open
```
- **关联术语**: Docker, PostgreSQL, Redis, Node.js

---

## Render

**英文原名**: Render | **中文译名**: Render（云托管平台）

- **定义**: 提供托管服务的云平台，支持 Web 服务、数据库、cron 任务等。
- **使用场景**: Web 应用托管、数据库服务、定时任务、私有服务。
- **代码示例**:
```yaml
# render.yaml
services:
  - type: web
    name: my-app
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
    envVars:
      - key: NODE_ENV
        value: production

databases:
  - name: my-db
    type: postgresql
    plan: free
```
- **关联术语**: Docker, PostgreSQL, Web 服务

---

### 4.2 容器与编排

## Docker

**英文原名**: Docker | **中文译名**: Docker（容器化平台）

- **定义**: 轻量级容器化技术，将应用及其依赖打包为可移植的容器镜像。
- **使用场景**: 应用容器化、微服务部署、开发环境标准化、CI/CD。
- **代码示例**:
```dockerfile
# Dockerfile 示例
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```
```bash
# Docker 命令
docker build -t my-app .
docker run -d -p 3000:3000 --name my-app my-app
docker ps
docker logs my-app
docker exec -it my-app sh
docker-compose up -d
```
- **关联术语**: 容器, Dockerfile, Docker Compose, Kubernetes

---

## Kubernetes (K8s)

**英文原名**: Kubernetes | **中文译名**: Kubernetes（容器编排系统）

- **定义**: Google 主导的容器编排系统，用于自动化容器化应用的部署、扩缩容和管理。
- **使用场景**: 生产级容器编排、微服务管理、多容器应用、弹性伸缩。
- **代码示例**:
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        ports:
        - containerPort: 8080
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
          requests:
            memory: "64Mi"
            cpu: "250m"
---
apiVersion: v1
kind: Service
metadata:
  name: my-app
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
```
```bash
# kubectl 命令
kubectl apply -f deployment.yaml
kubectl get pods
kubectl get services
kubectl logs -f deployment/my-app
kubectl scale deployment my-app --replicas=5
```
- **关联术语**: Docker, 容器编排, Helm, 云原生

---

### 4.3 CI/CD

## GitHub Actions

**英文原名**: GitHub Actions | **中文译名**: GitHub Actions（CI/CD 平台）

- **定义**: GitHub 原生的 CI/CD 平台，通过 YAML 配置自动化工作流。
- **使用场景**: 自动化测试、持续集成、持续部署、自动化任务。
- **代码示例**:
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
    
    - name: Build
      run: npm run build
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v4
      with:
        name: build-artifacts
        path: dist/
```
- **关联术语**: CI/CD, Git, Docker, npm

---

## Jenkins

**英文原名**: Jenkins | **中文译名**: Jenkins（开源 CI/CD）

- **定义**: 最流行的开源 CI/CD 工具，通过插件扩展功能，支持复杂构建流程。
- **使用场景**: 企业 CI/CD、复杂构建流程、自动化部署、历史项目维护。
- **代码示例**:
```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'my-app'
        REGISTRY = 'docker.io'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test -- --coverage'
            }
        }
        
        stage('Docker Build') {
            steps {
                script {
                    def image = docker.build("${REGISTRY}/${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    kubectl set image deployment/my-app \
                    my-app=${REGISTRY}/${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
```
- **关联术语**: CI/CD, Docker, Kubernetes, Groovy

---

## GitLab CI

**英文原名**: GitLab CI | **中文译名**: GitLab CI（GitLab CI/CD）

- **定义**: GitLab 内置的 CI/CD 功能，通过 .gitlab-ci.yml 配置自动化流程。
- **使用场景**: GitLab 项目 CI/CD、一体化 DevOps、私有化部署。
- **代码示例**:
```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE

test:unit:
  stage: test
  image: node:20
  script:
    - npm ci
    - npm run test:unit
  coverage: '/Coverage: \d+\.\d+%/'

test:e2e:
  stage: test
  image: node:20
  services:
    - postgres:15
  variables:
    POSTGRES_DB: test
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
  script:
    - npm ci
    - npm run test:e2e

deploy:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl set image deployment/my-app my-app=$DOCKER_IMAGE
    - kubectl rollout status deployment/my-app
  only:
    - main
```
- **关联术语**: CI/CD, GitLab, Docker, Kubernetes

---

### 4.4 基础设施

## Terraform

**英文原名**: Terraform | **中文译名**: Terraform（基础设施即代码）

- **定义**: HashiCorp 的基础设施即代码工具，通过声明式配置管理云资源。
- **使用场景**: 多云基础设施管理、基础设施自动化、基础设施版本控制。
- **代码示例**:
```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# 创建 VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "main-vpc"
  }
}

# 创建子网
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
  
  tags = {
    Name = "public-subnet"
  }
}

# 创建 EC2
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.public.id
  
  tags = {
    Name = "web-server"
  }
}

# 输出
output "instance_ip" {
  value = aws_instance.web.public_ip
}
```
```bash
# Terraform 命令
terraform init
terraform plan
terraform apply
terraform destroy
terraform output
```
- **关联术语**: IaC, AWS, GCP, 云原生

---

### 4.5 Serverless

## Serverless

**英文原名**: Serverless | **中文译名**: Serverless（无服务器计算）

- **定义**: 云原生架构模式，由云服务商管理服务器基础设施，按需付费。
- **使用场景**: 事件驱动应用、突发流量、降低成本、快速开发、无状态函数。
- **代码示例**:
```javascript
// AWS Lambda
exports.handler = async (event) => {
  const response = {
    statusCode: 200,
    body: JSON.stringify({
      message: 'Hello from Lambda!',
      timestamp: new Date().toISOString()
    })
  };
  return response;
};

// Azure Functions
module.exports = async function (context, req) {
  context.log('JavaScript HTTP trigger function processed a request.');
  
  context.res = {
    status: 200,
    body: { message: 'Hello from Azure Functions!' }
  };
};

// Vercel Serverless
export default function handler(req, res) {
  res.status(200).json({
    message: 'Hello from Vercel Serverless!',
    method: req.method
  });
}
```
```yaml
# Serverless Framework 配置
service: my-service

provider:
  name: aws
  runtime: nodejs20.x
  memorySize: 128
  timeout: 30

functions:
  hello:
    handler: handler.hello
    events:
      - http:
          path: hello
          method: get
      - schedule: rate(1 hour)
```
- **关联术语**: Lambda, 云函数, FaaS, Vercel

---

## 5. API 与协议

### 5.1 API 风格

## GraphQL

**英文原名**: GraphQL | **中文译名**: GraphQL（API 查询语言）

- **定义**: Facebook 开发的 API 查询语言，允许客户端精确请求需要的数据。
- **使用场景**: 移动端 API、复杂数据需求、前后端分离、微服务聚合。
- **代码示例**:
```graphql
# Schema 定义
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  comments: [Comment!]!
}

type Query {
  user(id: ID!): User
  users(limit: Int): [User!]!
}

type Mutation {
  createUser(input: CreateUserInput!): User!
  updateUser(id: ID!, input: UpdateUserInput!): User!
  deleteUser(id: ID!): Boolean!
}

# 客户端查询
query GetUserWithPosts {
  user(id: "1") {
    name
    email
    posts {
      title
      comments {
        content
      }
    }
  }
}

# 变量查询
query GetUser($userId: ID!) {
  user(id: $userId) {
    name
    posts(limit: 5) {
      title
    }
  }
}
```
```javascript
// Apollo Server
const { ApolloServer, gql } = require('@apollo/server');

const typeDefs = gql`
  type Query {
    hello: String
  }
`;

const resolvers = {
  Query: {
    hello: () => 'Hello World!',
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
await server.start();
```
- **关联术语**: REST, API, Apollo, TypeScript

---

## gRPC

**英文原名**: gRPC | **中文译名**: gRPC（高性能 RPC 框架）

- **定义**: Google 开发的高性能 RPC 框架，使用 Protocol Buffers 作为接口定义和序列化工具。
- **使用场景**: 微服务通信、高性能需求、移动端、实时流处理。
- **代码示例**:
```protobuf
// user.proto
syntax = "proto3";

package user;

service UserService {
  rpc GetUser (GetUserRequest) returns (User);
  rpc CreateUser (CreateUserRequest) returns (User);
  rpc StreamUsers (StreamRequest) returns (stream User);
}

message User {
  string id = 1;
  string name = 2;
  string email = 3;
}

message GetUserRequest {
  string id = 1;
}

message CreateUserRequest {
  string name = 1;
  string email = 2;
}
```
```go
// Go gRPC 服务端
package main

import (
    "context"
    "net"
    "google.golang.org/grpc"
    pb "./user"
)

type server struct {
    pb.UnimplementedUserServiceServer
}

func (s *server) GetUser(ctx context.Context, req *pb.GetUserRequest) (*pb.User, error) {
    return &pb.User{
        Id:    req.GetId(),
        Name:  "张三",
        Email: "zhangsan@example.com",
    }, nil
}

func main() {
    lis, _ := net.Listen("tcp", ":50051")
    grpcServer := grpc.NewServer()
    pb.RegisterUserServiceServer(grpcServer, &server{})
    grpcServer.Serve(lis)
}
```
- **关联术语**: Protocol Buffers, REST, 微服务, HTTP/2

---

## REST

**英文原名**: Representational State Transfer | **中文译名**: REST（RESTful API）

- **定义**: Roy Fielding 提出的架构风格，使用 HTTP 动词和资源路径设计 API。
- **使用场景**: Web API 设计、微服务接口、公开 API、移动端后端。
- **代码示例**:
```javascript
// RESTful API 设计
// 资源：users
// GET    /api/users          - 获取用户列表
// GET    /api/users/:id      - 获取单个用户
// POST   /api/users          - 创建用户
// PUT    /api/users/:id      - 更新用户（完整）
// PATCH  /api/users/:id      - 更新用户（部分）
// DELETE /api/users/:id      - 删除用户

// Express 实现
const express = require('express');
const app = express();

app.use(express.json());

// 获取用户列表
app.get('/api/users', async (req, res) => {
  const { page = 1, limit = 10 } = req.query;
  const users = await User.find()
    .limit(limit * 1)
    .skip((page - 1) * limit);
  res.json(users);
});

// 获取单个用户
app.get('/api/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);
  if (!user) {
    return res.status(404).json({ error: '用户不存在' });
  }
  res.json(user);
});

// 创建用户
app.post('/api/users', async (req, res) => {
  const user = new User(req.body);
  await user.save();
  res.status(201).json(user);
});
```
- **关联术语**: HTTP, JSON, API, GraphQL

---

## OpenAPI

**英文原名**: OpenAPI Specification | **中文译名**: OpenAPI（开放 API 规范）

- **定义**: 描述 REST API 的标准规范，前身为 Swagger 规范，用于 API 文档生成。
- **使用场景**: API 文档、代码生成、API 测试、API 治理。
- **代码示例**:
```yaml
# openapi.yaml
openapi: 3.0.3
info:
  title: 用户管理 API
  version: 1.0.0
  description: 用户管理服务的 RESTful API

servers:
  - url: https://api.example.com/v1
    description: 生产服务器
  - url: http://localhost:3000/v1
    description: 开发服务器

paths:
  /users:
    get:
      summary: 获取用户列表
      operationId: listUsers
      tags:
        - users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 10
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
    post:
      summary: 创建用户
      operationId: createUser
      tags:
        - users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: 创建成功

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        email:
          type: string
    CreateUserRequest:
      type: object
      required:
        - name
        - email
      properties:
        name:
          type: string
        email:
          type: string
```
- **关联术语**: REST, Swagger, API 文档

---

## Swagger

**英文原名**: Swagger | **中文译名**: Swagger（API 工具套件）

- **定义**: API 文档和工具套件，现在规范部分发展为 OpenAPI 标准。
- **使用场景**: API 文档编写、API 测试、客户端代码生成。
- **代码示例**:
```javascript
// 使用 swagger-jsdoc 生成文档
const swaggerJsdoc = require('swagger-jsdoc');

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: '用户 API',
      version: '1.0.0',
    },
  },
  apis: ['./routes/*.js'], // 路由文件路径
};

const swaggerSpec = swaggerJsdoc(options);

// 使用 swagger-ui-express
const swaggerUi = require('swagger-ui-express');
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));
```
- **关联术语**: OpenAPI, REST, API 文档

---

### 5.2 认证与授权

## OAuth 2.0

**英文原名**: OAuth 2.0 | **中文译名**: OAuth 2.0（开放授权协议）

- **定义**: 开放授权标准，允许第三方应用获取用户授权而无需获取密码。
- **使用场景**: 第三方登录、API 授权、社交登录、SSO。
- **代码示例**:
```javascript
// OAuth 2.0 授权流程

// 1. 重定向用户到授权服务器
const authUrl = new URL('https://authorization-server.com/authorize');
authUrl.searchParams.set('client_id', 'your-client-id');
authUrl.searchParams.set('redirect_uri', 'https://your-app.com/callback');
authUrl.searchParams.set('response_type', 'code');
authUrl.searchParams.set('scope', 'read:user write:repos');
authUrl.searchParams.set('state', 'random-state-string');

// 用户授权后回调
// GET /callback?code=AUTH_CODE&state=random-state-string

// 2. 用授权码换取访问令牌
async function exchangeCodeForToken(code) {
  const response = await fetch('https://authorization-server.com/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      grant_type: 'authorization_code',
      code: code,
      client_id: 'your-client-id',
      client_secret: 'your-client-secret',
      redirect_uri: 'https://your-app.com/callback',
    }),
  });
  
  return response.json();
  // { access_token: "...", token_type: "Bearer", expires_in: 3600 }
}

// 3. 使用访问令牌调用 API
async function getUserData(accessToken) {
  const response = await fetch('https://api.example.com/user', {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  return response.json();
}
```
- **关联术语**: JWT, 认证, 授权, OpenID Connect

---

## JWT

**英文原名**: JSON Web Token | **中文译名**: JWT（JSON Web 令牌）

- **定义**: 紧凑的 URL 安全方式在各方之间传输 JSON 声明，用于身份验证和信息交换。
- **使用场景**: 用户认证、API 授权、令牌无状态验证、跨域认证。
- **代码示例**:
```javascript
const jwt = require('jsonwebtoken');

// 生成 JWT
function generateToken(user) {
  const payload = {
    id: user.id,
    name: user.name,
    email: user.email,
    role: user.role
  };
  
  return jwt.sign(payload, process.env.JWT_SECRET, {
    expiresIn: '7d',        // 过期时间
    issuer: 'my-app',       // 签发者
    subject: user.email     // 主题
  });
}

// 验证 JWT
function verifyToken(token) {
  try {
    return jwt.verify(token, process.env.JWT_SECRET, {
      issuer: 'my-app',
      subject: 'user@example.com'
    });
  } catch (error) {
    return null;
  }
}

// Express 中间件
function authMiddleware(req, res, next) {
  const authHeader = req.headers.authorization;
  
  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: '未提供令牌' });
  }
  
  const token = authHeader.substring(7);
  const decoded = verifyToken(token);
  
  if (!decoded) {
    return res.status(401).json({ error: '无效的令牌' });
  }
  
  req.user = decoded;
  next();
}

// JWT 结构
// header.payload.signature
// eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtZSI6IuW8qOS4iSJ9.signature
```
- **关联术语**: OAuth 2.0, 认证, 授权, Token

---

### 5.3 实时通信

## WebSocket

**英文原名**: WebSocket | **中文译名**: WebSocket（全双工通信协议）

- **定义**: HTML5 提供的全双工通信协议，客户端与服务端可双向实时通信。
- **使用场景**: 实时聊天、实时协作、实时通知、游戏、股票行情。
- **代码示例**:
```javascript
// 服务端（Node.js + ws）
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  console.log('客户端连接');
  
  // 接收消息
  ws.on('message', (message) => {
    console.log('收到:', message.toString());
    
    // 广播给所有客户端
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(`服务器回复: ${message}`);
      }
    });
  });
  
  // 发送消息
  ws.send('欢迎连接!');
  
  // 定时发送
  const interval = setInterval(() => {
    ws.send(JSON.stringify({ time: new Date() }));
  }, 5000);
  
  ws.on('close', () => clearInterval(interval));
});
```
```javascript
// 客户端
const ws = new WebSocket('ws://localhost:8080');

ws.onopen = () => {
  console.log('连接成功');
  ws.send('Hello Server');
};

ws.onmessage = (event) => {
  console.log('收到:', event.data);
};

ws.onerror = (error) => {
  console.error('错误:', error);
};

ws.onclose = () => {
  console.log('连接关闭');
};
```
- **关联术语**: HTTP, 实时通信, Socket.io

---

## SSE

**英文原名**: Server-Sent Events | **中文译名**: SSE（服务器推送事件）

- **定义**: 服务器向浏览器推送事件的技术，基于 HTTP 单向通信，适合简单实时场景。
- **使用场景**: 实时通知、股票行情、新闻推送、社交媒体更新。
- **代码示例**:
```javascript
// 服务端（Express）
app.get('/stream', (req, res) => {
  // 设置 SSE 响应头
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  
  // 每秒发送消息
  const interval = setInterval(() => {
    const data = JSON.stringify({
      time: new Date().toISOString(),
      message: '服务器时间更新'
    });
    res.write(`data: ${data}\n\n`);
  }, 1000);
  
  // 清理
  req.on('close', () => {
    clearInterval(interval);
    res.end();
  });
});
```
```javascript
// 客户端
const eventSource = new EventSource('/stream');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('收到:', data);
};

eventSource.onerror = (error) => {
  console.error('SSE 错误:', error);
  eventSource.close();
};

// 命名事件
// 服务端: res.write('event: custom\ndata: {}\n\n');
// 客户端: eventSource.addEventListener('custom', (e) => {})
```
- **关联术语**: HTTP, 实时通信, WebSocket

---

## 6. 移动端开发

## React Native

**英文原名**: React Native | **中文译名**: React Native（跨平台移动开发框架）

- **定义**: Facebook 开发的跨平台移动开发框架，使用 JavaScript/React 构建原生 iOS/Android 应用。
- **使用场景**: 跨平台移动应用、需要原生性能的应用、React 开发者。
- **代码示例**:
```jsx
import React, { useState } from 'react';
import { 
  View, 
  Text, 
  TextInput, 
  TouchableOpacity, 
  FlatList,
  StyleSheet 
} from 'react-native';

function App() {
  const [text, setText] = useState('');
  const [items, setItems] = useState([]);
  
  const addItem = () => {
    if (text.trim()) {
      setItems([...items, { key: Date.now().toString(), text }]);
      setText('');
    }
  };
  
  return (
    <View style={styles.container}>
      <Text style={styles.title}>待办事项</Text>
      <View style={styles.inputRow}>
        <TextInput
          style={styles.input}
          value={text}
          onChangeText={setText}
          placeholder="添加新事项..."
        />
        <TouchableOpacity style={styles.button} onPress={addItem}>
          <Text style={styles.buttonText}>添加</Text>
        </TouchableOpacity>
      </View>
      <FlatList
        data={items}
        renderItem={({ item }) => (
          <Text style={styles.item}>{item.text}</Text>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, paddingTop: 50 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  inputRow: { flexDirection: 'row', marginBottom: 20 },
  input: { flex: 1, borderWidth: 1, padding: 10, marginRight: 10 },
  button: { backgroundColor: '#007AFF', padding: 10 },
  buttonText: { color: 'white' },
  item: { padding: 10, borderBottomWidth: 1 }
});

export default App;
```
- **关联术语**: JavaScript, React, TypeScript, Expo

---

## Flutter

**英文原名**: Flutter | **中文译名**: Flutter（Google 跨平台框架）

- **定义**: Google 开发的跨平台 UI 框架，使用 Dart 语言，渲染性能优秀。
- **使用场景**: 跨平台应用、高性能 UI、需要自定义动画的应用。
- **代码示例**:
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final List<String> _items = [];
  final TextEditingController _controller = TextEditingController();

  void _addItem() {
    if (_controller.text.isNotEmpty) {
      setState(() {
        _items.add(_controller.text);
        _controller.clear();
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('待办事项')),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: const InputDecoration(
                      hintText: '添加新事项',
                      border: OutlineInputBorder(),
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                ElevatedButton(
                  onPressed: _addItem,
                  child: const Text('添加'),
                ),
              ],
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: _items.length,
              itemBuilder: (context, index) {
                return ListTile(title: Text(_items[index]));
              },
            ),
          ),
        ],
      ),
    );
  }
}
```
- **关联术语**: Dart, 跨平台, Material Design, iOS, Android

---

## SwiftUI

**英文原名**: SwiftUI | **中文译名**: SwiftUI（Apple 声明式 UI 框架）

- **定义**: Apple 2019 年推出的声明式 UI 框架，用于构建 iOS/macOS/watchOS/tvOS 应用。
- **使用场景**: Apple 平台原生开发、需要现代声明式语法、快速原型。
- **代码示例**:
```swift
import SwiftUI

struct ContentView: View {
    @State private var items: [String] = []
    @State private var newItem: String = ""
    
    var body: some View {
        NavigationView {
            VStack {
                HStack {
                    TextField("添加新事项", text: $newItem)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    Button(action: addItem) {
                        Image(systemName: "plus.circle.fill")
                    }
                }
                .padding()
                
                List {
                    ForEach(items, id: \.self) { item in
                        Text(item)
                    }
                    .onDelete(perform: deleteItems)
                }
            }
            .navigationTitle("待办事项")
        }
    }
    
    func addItem() {
        guard !newItem.isEmpty else { return }
        items.append(newItem)
        newItem = ""
    }
    
    func deleteItems(at offsets: IndexSet) {
        items.remove(atOffsets: offsets)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
```
- **关联术语**: Swift, iOS, macOS, Apple, UIKit

---

## 7. 开发工具

### 7.1 编辑器与 IDE

## VS Code

**英文原名**: Visual Studio Code | **中文译名**: VS Code（代码编辑器）

- **定义**: Microsoft 开发的免费开源代码编辑器，支持丰富的扩展生态。
- **使用场景**: 通用代码开发、Web 开发、Python/TypeScript 开发、远程开发。
- **代码示例**:
```json
// .vscode/launch.json - 调试配置
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "启动程序",
      "skipFiles": ["<node_internals>/**"],
      "program": "${workspaceFolder}/src/index.js"
    },
    {
      "type": "python",
      "request": "launch",
      "name": "Python: 当前文件",
      "program": "${file}",
      "pythonPath": "${config:python.pythonPath}"
    }
  ]
}
```
```json
// .vscode/settings.json - 工作区设置
{
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "files.autoSave": "afterDelay",
  "files.exclude": {
    "**/node_modules": true,
    "**/.git": true
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black",
    "editor.formatOnSave": true
  }
}
```
- **关联术语**: TypeScript, Python, Git, 扩展

---

## IntelliJ IDEA

**英文原名**: IntelliJ IDEA | **中文译名**: IntelliJ IDEA（Java IDE）

- **定义**: JetBrains 开发的 Java/Kotlin 集成开发环境，有社区版和终极版。
- **使用场景**: Java 开发、Kotlin 开发、企业级项目、大型代码库。
- **代码示例**:
```java
// IntelliJ IDEA 快捷键
// Ctrl + Shift + F10: 运行当前文件
// Ctrl + Shift + F9: 调试当前文件
// Ctrl + Alt + L: 格式化代码
// Ctrl + Alt + O: 优化导入
// Ctrl + N: 搜索类
// Shift + Shift: 搜索所有

// 实时模板 (Live Templates)
// sout -> System.out.println();
// psvm -> public static void main(String[] args) {}
// fori -> for (int i = 0; i < ; i++) {}

// 插件推荐
// - Lombok
// - Maven Helper
// - GitToolBox
// - Key Promoter X
```
- **关联术语**: Java, Kotlin, Maven, Gradle

---

### 7.2 包管理器

## npm

**英文原名**: Node Package Manager | **中文译名**: npm（Node.js 包管理器）

- **定义**: Node.js 默认的包管理器，全球最大的 JavaScript 包仓库。
- **使用场景**: JavaScript/Node.js 项目依赖管理、前端开发、发布包。
- **代码示例**:
```bash
# 初始化项目
npm init -y

# 安装依赖
npm install lodash              # 生产依赖
npm install -D typescript       # 开发依赖
npm install express@4.18.2      # 指定版本
npm install                     # 根据 package.json 安装

# 运行脚本
npm run dev
npm run build
npm test

# 包管理
npm outdated                    # 检查过期包
npm update                      # 更新包
npm uninstall lodash            # 卸载
npm publish                     # 发布包

# 查看信息
npm view lodash                 # 查看包信息
npm ls                          # 列出已安装包
```
- **关联术语**: Node.js, JavaScript, package.json, yarn

---

## yarn

**英文原名**: Yarn | **中文译名**: Yarn（Facebook 包管理器）

- **定义**: Facebook 开发的 JavaScript 包管理器，比 npm 更快、更可靠。
- **使用场景**: 大型项目、需要更快安装速度、离线缓存。
- **代码示例**:
```bash
# 初始化
yarn init

# 安装依赖
yarn add lodash                 # 生产依赖
yarn add -D typescript          # 开发依赖
yarn install                    # 根据 yarn.lock 安装

# 运行脚本
yarn dev
yarn build
yarn test

# 包管理
yarn outdated                   # 检查过期
yarn upgrade                    # 升级
yarn remove lodash              # 移除

# 特性
yarn.lock                       # 锁定版本
yarn workspaces                 # 工作区
```
- **关联术语**: npm, Node.js, JavaScript, package.json

---

## pnpm

**英文原名**: pnpm | **中文译名**: pnpm（高性能包管理器）

- **定义**: 高性能的 JavaScript 包管理器，使用硬链接节省磁盘空间。
- **使用场景**: 大型项目、磁盘空间优化、需要更快安装速度。
- **代码示例**:
```bash
# 安装
npm install -g pnpm

# 使用
pnpm install
pnpm add lodash
pnpm add -D typescript
pnpm remove lodash

# 特性
# 1. 硬链接节省空间
# 2. node_modules 结构更清晰
# 3. 严格依赖校验
# 4. 支持 monorepo

# pnpm-workspace.yaml
packages:
  - 'packages/*'
```
- **关联术语**: npm, yarn, Node.js, monorepo

---

## pip

**英文原名**: pip | **中文译名**: pip（Python 包管理器）

- **定义**: Python 的包管理工具，用于安装和管理 Python 包。
- **使用场景**: Python 项目依赖管理、机器学习、数据科学。
- **代码示例**:
```bash
# 安装包
pip install requests
pip install requests==2.28.0
pip install "requests>=2.28.0"
pip install -r requirements.txt

# 虚拟环境
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows
pip install flask

# 导出依赖
pip freeze > requirements.txt

# 常用命令
pip list                    # 列出已安装
pip show requests           # 查看包信息
pip uninstall requests      # 卸载
pip search "web framework"  # 搜索（已禁用）
```
- **关联术语**: Python, virtualenv, requirements.txt, conda

---

## conda

**英文原名**: Conda | **中文译名**: Conda（Python 环境管理器）

- **定义**: Anaconda 的包和环境管理器，支持 Python、R 等多语言。
- **使用场景**: 数据科学、机器学习、需要多版本 Python 环境管理。
- **代码示例**:
```bash
# 环境管理
conda create -n myenv python=3.11
conda activate myenv
conda deactivate

# 包管理
conda install numpy pandas
conda install -c conda-forge scikit-learn
conda remove numpy

# 环境导出
conda env export > environment.yml
conda env create -f environment.yml

# 查看
conda env list
conda list

# 常用命令
conda update conda
conda update --all
```
- **关联术语**: Python, Anaconda, pip, virtualenv

---

## cargo

**英文原名**: Cargo | **中文译名**: Cargo（Rust 包管理器）

- **定义**: Rust 的包管理器和构建工具，负责依赖管理和编译。
- **使用场景**: Rust 项目开发、 crates.io 包使用、Rust 生态。
- **代码示例**:
```bash
# 创建项目
cargo new my_project
cargo init

# 构建
cargo build                  # 调试构建
cargo build --release        # 发布构建
cargo run                    # 运行
cargo run --release          # 发布运行

# 测试
cargo test
cargo test --release

# 依赖管理
# Cargo.toml
[dependencies]
serde = "1.0"
serde_json = "1.0"
tokio = { version = "1", features = ["full"] }

[dev-dependencies]
criterion = "0.5"

# 安装依赖
cargo fetch
cargo update

# 其他
cargo doc --open             # 生成文档
cargo clippy                 # 代码检查
cargo fmt                    # 代码格式化
```
- **关联术语**: Rust, crates.io, Cargo.toml, rustc

---

## 8. 工程化概念

## Loop-engineering

**英文原名**: Loop-engineering | **中文译名**: Loop-engineering（循环工程）

- **定义**: AI 编程中的核心范式，通过人机协作循环（思考→编码→验证→迭代）完成任务。
- **使用场景**: AI 辅助编程、复杂问题求解、迭代式开发。
- **代码示例**:
```python
# AI Loop-engineering 流程示例
async def loop_engineering_task(problem: str, max_iterations: int = 5):
    """
    循环工程流程：
    1. 分析问题 (Analyze)
    2. 生成方案 (Plan)
    3. 编写代码 (Code)
    4. 验证结果 (Verify)
    5. 迭代优化 (Iterate)
    """
    context = {"problem": problem, "iterations": 0}
    
    for i in range(max_iterations):
        context["iterations"] = i + 1
        
        # 思考阶段
        analysis = await ai_analyze(context)
        
        # 编码阶段
        code = await ai_generate_code(analysis)
        
        # 验证阶段
        result = await verify_code(code)
        
        if result["success"]:
            return {"code": code, "iterations": i + 1}
        
        # 迭代优化
        context["feedback"] = result["feedback"]
        context["code"] = code
    
    return {"error": "达到最大迭代次数", "context": context}
```
- **关联术语**: AI 编程, Agent, Prompt Engineering, Claude Code

---

## Graph Engineering

**英文原名**: Graph Engineering | **中文译名**: Graph Engineering（图工程）

- **定义**: 在 AI 应用中构建有向无环图（DAG）来组织复杂的工作流程和任务依赖。
- **使用场景**: 复杂 AI 工作流、多步骤数据处理、任务编排。
- **代码示例**:
```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

# 定义状态
class GraphState(TypedDict):
    input: str
    documents: list
    answer: str

# 创建图
workflow = StateGraph(GraphState)

# 添加节点
workflow.add_node("retrieve", retrieve_documents)
workflow.add_node("generate", generate_answer)
workflow.add_node("validate", validate_answer)

# 添加边
workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "validate")

# 条件边
workflow.add_conditional_edges(
    "validate",
    should_retry,
    {
        "retry": "retrieve",
        "end": END
    }
)

# 编译
graph = workflow.compile()

# 执行
result = graph.invoke({"input": "什么是机器学习？"})
```
- **关联术语**: LangChain, Chain, Agent, DAG, 工作流

---

## Compact

**英文原名**: Compact | **中文译名**: Compact（精简指令模式）

- **定义**: AI 编程中的一种提示词模式，通过精简的指令实现高效沟通。
- **使用场景**: 快速开发、简洁沟通、减少 token 消耗。
- **代码示例**:
```python
# Compact 模式示例
# 传统模式（冗长）
compact_prompt = """
你是一位专业的 Python 开发者。
请帮我编写一个函数，该函数需要：
1. 接受一个列表作为输入
2. 对列表中的每个元素进行平方计算
3. 返回计算后的新列表
请确保代码简洁、效率高。
"""

# Compact 模式（精简）
compact_prompt = """
写一个函数：输入列表，返回每个元素平方的新列表
"""

# 更紧凑的变体
# 使用分隔符和结构化
compact_prompt = """
任务：平方列表
输入：[1,2,3]
输出：[1,4,9]
代码：
"""

# 实际应用
def compact_code(prompt: str) -> str:
    """Compact 模式生成代码"""
    return f"""# 任务：{prompt}\n# 实现："""
```
- **关联术语**: Prompt Engineering, AI 编程, Token 优化

---

## Skill

**英文原名**: Skill | **中文译名**: Skill（技能定义）

- **定义**: AI 系统中定义的能力单元，包含工具、提示词和执行逻辑。
- **使用场景**: AI Agent 能力扩展、工具封装、模块化 AI 功能。
- **代码示例**:
```typescript
// Skill 定义示例
interface Skill {
  name: string;
  description: string;
  parameters: z.ZodType;
  execute: (params: any) => Promise<any>;
  examples?: Example[];
}

// 文件读取 Skill
const readFileSkill: Skill = {
  name: "read_file",
  description: "读取文件内容",
  parameters: z.object({
    path: z.string().describe("文件路径"),
    startLine: z.number().optional().describe("起始行号"),
    endLine: z.number().optional().describe("结束行号"),
  }),
  execute: async ({ path, startLine, endLine }) => {
    const content = await fs.promises.readFile(path, 'utf-8');
    const lines = content.split('\n');
    return lines.slice(startLine - 1, endLine).join('\n');
  },
  examples: [
    { input: { path: "src/index.ts" }, output: "..." },
  ],
};

// Skill 注册
const skillRegistry = new Map<string, Skill>();
skillRegistry.set("read_file", readFileSkill);
```
- **关联术语**: MCP, Agent, Tool Use, Function Calling

---

## Harness

**英文原名**: Harness | **中文译名**: Harness（测试/评估框架）

- **定义**: 用于测试和评估 AI 系统能力的框架，提供标准化的测试用例和评估指标。
- **使用场景**: AI 模型评估、提示词优化、模型对比、基准测试。
- **代码示例**:
```python
# Harness 评估框架示例
from dataclasses import dataclass
from typing import List, Dict, Any
import asyncio

@dataclass
class TestCase:
    input: str
    expected: str
    evaluation: str  # 评估指标

@dataclass  
class EvaluationResult:
    test_case: TestCase
    actual_output: str
    passed: bool
    score: float
    feedback: str

class AIHarness:
    def __init__(self, model: Any):
        self.model = model
        self.results: List[EvaluationResult] = []
    
    async def run_test(self, test_case: TestCase) -> EvaluationResult:
        # 执行
        output = await self.model.predict(test_case.input)
        
        # 评估
        passed, score, feedback = self.evaluate(
            test_case.expected, 
            output,
            test_case.evaluation
        )
        
        return EvaluationResult(
            test_case=test_case,
            actual_output=output,
            passed=passed,
            score=score,
            feedback=feedback
        )
    
    async def run_suite(self, test_suite: List[TestCase]) -> Dict[str, Any]:
        results = await asyncio.gather(*[
            self.run_test(tc) for tc in test_suite
        ])
        
        return {
            "total": len(results),
            "passed": sum(1 for r in results if r.passed),
            "failed": sum(1 for r in results if not r.passed),
            "avg_score": sum(r.score for r in results) / len(results),
            "results": results
        }

# 使用示例
harness = AIHarness(gpt4_model)
test_suite = [
    TestCase("1+1=?", "2", "exact_match"),
    TestCase("写一首诗", "诗", "contains_keyword"),
]
results = await harness.run_suite(test_suite)
```
- **关联术语**: AI 编程, 测试, 评估, 基准

---

## 附录：术语索引

| 分类 | 术语数量 |
|------|----------|
| 前端开发 | 24 |
| 后端开发 | 23 |
| AI 与大模型 | 24 |
| 云原生与 DevOps | 17 |
| API 与协议 | 11 |
| 移动端开发 | 3 |
| 开发工具 | 7 |
| 工程化概念 | 5 |
| **总计** | **114** |

