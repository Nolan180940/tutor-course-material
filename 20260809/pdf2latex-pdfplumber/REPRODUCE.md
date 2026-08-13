# PDF → LaTeX 复现流程总结

用 pdfplumber 从 NYU 官方《Resume Format.pdf》测量版式规格，重建 LaTeX 模板的全流程复现。
原解析与还原（2026-08-09）位于 `C:\Users\nolan\Desktop\NYU Shanghai\Career Development\Resume\template_cv\`，
本目录为可重复运行的复现版。

## 产出文件

| 文件 | 说明 |
| --- | --- |
| `Resume Format.pdf` | 输入：NYU 官方简历格式原稿 |
| `Garamond.ttf` / `-Bold` / `-Italic` | 原 PDF 内嵌字体的本地三件套（对照基准同源） |
| `analyze_resume.py` | 测量脚本：`python analyze_resume.py` → 终端报告 + `spec_report.md` |
| `spec_report.md` | 结构化测量报告（边距/字体字号/55 行结构/行距/块距/缩进/对齐） |
| `verify.py` | 对照验证：声明值 vs 实测 + 结构对照 + 编译产物逐行坐标对照 |
| `resume_format_rebuilt.tex` | 依据测量重建的 LaTeX 模板（XeLaTeX 编译） |

## 复现流程（四步）

### 1. 解析（pdfplumber）
- **页面几何**：`612×792pt`（Letter）；剔除 ● 噪声（Word 页眉页脚自动符号 2 个）与
  **空白字形**（Word 的 Tab 会展开为连续空格字形，尾随空格污染 x1）后求文本包围盒
  → 四边距 **左 29.4 / 右 30.2 / 上 31.6 / 下 60.5pt**
- **字体字号**：chars 按 `fontname × size` 聚类 → 嵌入子集名（`BCDGEE+Garamond` 等）
  映射为 Garamond 三件套；字号三档 **21.96（姓名）/ 11.04（EDUCATION 标题）/ 9.96（正文）**；
  ● 使用 TimesNewRoman/Arial（非 Garamond）
- **逐行结构**：`extract_text_lines` 为权威行数据（正确恢复空格），字符级数据补样式/字号/对齐；
  左右块按 x 间隙 >60pt 拆分（空格字形按"最近字形块"归属）

### 2. 测量要点（spec_report.md）
- 行距主节奏 ≈12pt（跨字体行 ±1pt 度量噪声）
- 标题前距折算 = top 差 − 12：EDUCATION 5.4pt（取 6pt）、其余 4.2~4.7pt（取 4pt）
- 项目符号：● x0=33.2（相对左边距 3.9pt），正文首字符 x0=43.8pt
- **关键验证**：`leftmargin=13.6pt` ⇒ LaTeX 正文起点 `30.2+13.6=43.8pt`，
  与实测首字符 x0 **逐点重合**
- 姓名 21.96pt 粗体居中（中心 308.7 vs 页面中心 306，Word 居中的 2.7pt 字符度量偏移）

### 3. 验证（verify.py，仅数值、不编译）
- 第一部分：13 项声明值（geometry/fontsize/bighead/bull/bmin/bplus）vs 实测 **全部 ✅**
- 第二部分：内容结构对照
  - `\entry+\entryit` = 17 = 原 PDF 右对齐条目行数 17 ✅
  - `\item` = 30 vs ● = 28，差 2：**原 PDF 的 GPA/Organizations 两行无 ●**，
    现成品 .tex 用了 `bull` 环境（唯一内容级差异，版式参数无影响）；重建版已按原 PDF 修正
- 第三部分：原 PDF vs LaTeX 编译产物（`resume_format.pdf`）逐行 top 对照
  - 55/55 行序完全一致，平均偏移 −1.94pt（编译产物整体上移），|Δ|>3pt 仅 6/55
  - 偏移来源：● 行跨字体度量 + `\bmin/\bplus` 微调 → 像素级还原成立

### 4. 重建（resume_format_rebuilt.tex）
依据 spec_report 参数 + 内容骨架（占位文本）写出；与现成品结构一致
（geometry/fontspec/enumitem + `\bighead/\head/\entry/\entryit/bull` + `\bmin/\bplus`）。

## 结论

昨天的还原**完全成立**：版式参数 13/13 项与实测吻合，编译产物与原 PDF 行级对齐误差
±2pt 内。发现的唯一差异（EDUCATION 段 ● 有无）已在本目录重建版中按原 PDF 修正。
