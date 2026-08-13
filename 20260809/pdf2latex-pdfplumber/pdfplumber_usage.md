# pdfplumber 使用说明（基于本项目实战）

本项目 `analyze_resume.py` 与 `verify.py` 用 pdfplumber 测量《Resume Format.pdf》的版式规格。
本文按本项目实际用到的 API 讲解用法。

## 1. 安装与打开

```python
import pdfplumber

with pdfplumber.open("Resume Format.pdf") as pdf:   # 上下文管理器，自动关闭文件
    page = pdf.pages[0]                             # pages: Page 对象列表，[0] 取第 1 页
```

- `pdf.pages`：所有页，`len(pdf.pages)` 得页数
- 页面尺寸：`page.width` × `page.height`（pt 为单位，Letter 为 612×792）
- 其他可探测对象：`page.lines`（直线）、`page.rects`（矩形）、`page.curves`（曲线）
- 本项目断言单页：`assert len(pdf.pages) == 1`

## 2. 两个核心数据源（互补使用）

| 数据源 | 返回 | 优点 | 缺点 | 用途 |
| --- | --- | --- | --- | --- |
| `page.chars` | 每个**字符**一个 dict | 带字体名、字号、坐标 | 空格会丢（Word 的空格/页眉符号可能是其他字体） | 字号聚类、边距、样式、● 识别 |
| `page.extract_text_lines()` | 每**行**一个 dict | 文本完整（正确恢复空格） | 无字体/字号信息 | 行文本、行距、标题定位 |

```python
chars = page.chars   # 逐字符
# 字段: c["text"]  c["fontname"]  c["size"]  c["x0"]  c["x1"]  c["top"]  c["bottom"]

ext = page.extract_text_lines()   # 逐行
# 字段: line["text"]  line["top"]  line["bottom"]  line["x0"]  line["x1"]
```

两种数据按 y 坐标互相挂接（用字符 top 匹配所在行）：

```python
row_chars = [c for c in chars if abs(c["top"] - line["top"]) < 4.0]   # analyze_resume.py:84
```

## 3. 常用测量技巧（抄了就能用）

### 3.1 页面几何与边距

```python
text_chars = [c for c in chars if 是正文且非空白]
xs0  = min(c["x0"] for c in text_chars)        # → 左边距
xs1  = max(c["x1"] for c in text_chars)        # → 右边距 = page.width - xs1
tops = min(c["top"] for c in text_chars)       # → 上边距
bots = max(c["bottom"] for c in text_chars)    # → 下边距 = page.height - bots
```

**踩坑**：Word 的 Tab 会渲染成连续空格字形（本项目每行 ~22 个），尾随空格会污染
右边缘 x1，统计边距前必须剔除空白字形，否则 30.2pt 会测成 27.8pt。

### 3.2 字体与字号聚类

```python
from collections import Counter
fs = Counter((c["fontname"], round(c["size"], 2)) for c in page.chars)
# → {('BCDGEE+Garamond', 9.96): 1554, ('BCDFEE+Garamond-Bold', 9.96): 991, ...}
```

- 嵌入字体名带子集前缀（`BCDGEE+Garamond`），判断字体族用 `"Garamond" in fontname`
- 多个字号说明有大字标题/小字正文，本项目测出三档：21.96（姓名）/ 11.04（标题）/ 9.96（正文）

### 3.3 逐行结构与左右分块

```python
# 1) 按 top 容差把字符归行；行内按 x0 排序
# 2) 行内相邻字形 x 间隙 > 60pt → 拆成左右两个块（如左: 正文标题，右: 对齐的日期）
# 3) 空格字形永远并入最近块，不参与间隙判定
# 4) 对齐判定: |中心 - 306| < 6 → 居中；x1 > 570 → 右对齐；否则左对齐
```

### 3.4 行距节奏

```python
tlist = [l["top"] for l in ext]
diffs = [round(b - a, 1) for a, b in zip(tlist, tlist[1:])]
Counter(diffs).most_common(3)   # → 主节奏 12pt，≈16pt 是标题前距
```

### 3.5 特定字符识别

```python
# ● 项目符号: 原 PDF 用 TimesNewRoman/Arial 字体渲染，不是 Garamond
n_bullet = sum(1 for c in page.chars if c["text"] == "\u25cf")
# 带 ● 的行文本: line["text"].lstrip().startswith("\u25cf")
```

## 4. 本项目验证脚本的用法（verify.py）

```python
# 同时打开两个 PDF 逐行对比（原稿 vs LaTeX 编译产物）
with pdfplumber.open(SRC_PDF) as pdf, pdfplumber.open(OUT_PDF) as pdf2:
    ext1 = pdf.pages[0].extract_text_lines()
    ext2 = pdf2.pages[0].extract_text_lines()
    for l1, l2 in zip(ext1, ext2):
        delta = l2["top"] - l1["top"]     # 逐行 top 偏差 → 量化还原精度
```

## 5. 为什么不用其他方法

| 方法 | 为什么不适用 |
| --- | --- |
| `extract_text()` | 只给纯文本，无坐标/字体，无法量版式 |
| `extract_table()` | 简历是自由版式（无表格线），表提取无用 |
| `extract_words()` | 词级粒度太粗，行距/缩进需要字符级坐标 |

本项目要还原的是"像素级"版式（边距、行距、缩进、字距），只有 `chars` 的字符级
坐标能做到。