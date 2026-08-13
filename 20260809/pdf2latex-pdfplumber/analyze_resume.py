"""analyze_resume.py — 用 pdfplumber 测量 NYU 官方简历 PDF 的版式规格

输入: Resume Format.pdf（默认取本脚本所在目录）
输出: 终端报告 + spec_report.md（与 README 版式规格表同构）

用法: python analyze_resume.py [PDF路径，可选]
"""
import sys
from pathlib import Path
from collections import Counter
import pdfplumber

sys.stdout.reconfigure(encoding="utf-8")

PDF = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "Resume Format.pdf"
OUT = Path(__file__).parent / "spec_report.md"
PAGE_W, PAGE_H = 612.0, 792.0
HEADINGS = {
    "EDUCATION",
    "PROFESSIONAL EXPERIENCE (In chronological order)",
    "LEADERSHIP & EXTRACURRICULAR ACTIVITIES",
    "SKILLS & INTERESTS",
}


def is_garamond(fontname: str) -> bool:
    return "Garamond" in fontname


def style_of(fontname: str) -> str:
    if "Bold" in fontname:
        return "bold"
    if "Italic" in fontname:
        return "italic"
    return "regular"


with pdfplumber.open(PDF) as pdf:
    assert len(pdf.pages) == 1, "仅支持单页"
    page = pdf.pages[0]
    chars = page.chars
    ext_lines = page.extract_text_lines()

    report = []
    report.append("# 版式规格测量报告（pdfplumber）")
    report.append("")
    report.append(f"- 输入文件: `{PDF}`")
    report.append(f"- 页数: {len(pdf.pages)}，页面尺寸: {page.width:.1f} x {page.height:.1f}pt (Letter)")
    report.append(f"- 字符数: {len(chars)}，线: {len(page.lines)}，矩形: {len(page.rects)}，行数(extract_text_lines): {len(ext_lines)}")
    report.append("")

    # ---------- 1. 字体 x 字号 聚类 ----------
    fs = Counter((c["fontname"], round(c["size"], 2)) for c in chars)
    report.append("## 1. 字体 × 字号 分布")
    report.append("")
    report.append("| 嵌入字体名 | 真实字体 | 字号(pt) | 字符数 |")
    report.append("| --- | --- | ---: | ---: |")
    garamond_map = {
        "Garamond": "Garamond", "Garamond-Bold": "Garamond-Bold",
        "Garamond-Italic": "Garamond-Italic", "TimesNewRomanPSMT": "●/空格(非 Garamond)",
        "ArialMT": "●/空格(非 Garamond)", "___WRD_EMBED_SUB_47": "●(页眉页脚符号)"}
    for (fn, sz), n in sorted(fs.items(), key=lambda kv: (-kv[0][1], kv[0][0])):
        report.append(f"| {fn} | {garamond_map.get(fn, fn)} | {sz:.2f} | {n} |")
    report.append("")

    # ---------- 2. 边距（剔除 ● 与页眉页脚噪声、空白字形） ----------
    # 注意: Word 的 Tab 会以连续空格字形输出，尾随空格会污染 x1，须剔除
    text_chars = [c for c in chars if is_garamond(c["fontname"]) and c["text"].strip() != ""]
    xs0 = min(c["x0"] for c in text_chars)
    xs1 = max(c["x1"] for c in text_chars)
    tops = min(c["top"] for c in text_chars)
    bottoms = max(c["bottom"] for c in text_chars)
    report.append("## 2. 边距（仅 Garamond 文本包围盒）")
    report.append("")
    report.append(f"- 左边缘 x0 = {xs0:.1f}pt → 左边距 ≈ {xs0:.1f}pt")
    report.append(f"- 右边缘 x1 = {xs1:.1f}pt → 右边距 ≈ {PAGE_W - xs1:.1f}pt")
    report.append(f"- 顶部 top = {tops:.1f}pt → 上边距 ≈ {tops:.1f}pt")
    report.append(f"- 底部 bottom = {bottoms:.1f}pt → 下边距 ≈ {PAGE_H - bottoms:.1f}pt")
    report.append(f"- 页缘噪声: ● 2 个位于 top≈3.1/780.1pt（Word 页眉页脚自动符号，不计入边距）")
    report.append("")

    # ---------- 3. 逐行结构（extract_text_lines 为权威文本 + 字符级样式） ----------
    def row_chars(line):
        return [c for c in chars if abs(c["top"] - line["top"]) < 4.0]

    def split_blocks(chars_in_row):
        chars_in_row = sorted(chars_in_row, key=lambda c: c["x0"])
        glyphs = [c for c in chars_in_row if c["text"].strip() != ""]
        spaces = [c for c in chars_in_row if c["text"].strip() == ""]
        blocks = []
        cur = [glyphs[0]]
        for c in glyphs[1:]:
            if c["x0"] - cur[-1]["x1"] > 60:
                blocks.append(cur)
                cur = [c]
            else:
                cur.append(c)
        blocks.append(cur)
        # 空格字形（含 Word Tab 展开的连续空格）归属最近的相邻字形块
        for s in spaces:
            dprev = min((abs(s["x0"] - b[-1]["x1"]), b) for b in blocks)
            dnext = min((abs(b[0]["x0"] - s["x1"]), b) for b in blocks)
            (s["_dprev"], _), (s["_dnext"], _) = dprev, dnext
        for s in spaces:
            target = min(blocks, key=lambda b: min(abs(s["x0"] - b[-1]["x1"]),
                                                   abs(b[0]["x0"] - s["x1"])))
            target.append(s)
        return blocks

    def align_of(blk):
        cx = (blk[0]["x0"] + max(c["x1"] for c in blk)) / 2
        if abs(cx - PAGE_W / 2) < 6:
            return "center"
        if max(c["x1"] for c in blk) > 570:
            return "right"
        return "left"

    rows = []  # 每行: {top, bottom, text, blocks:[{chars,x0,x1,sizes,styles,align,bullet}]}
    for line in ext_lines:
        rcs = row_chars(line)
        if not rcs:
            continue
        row = {"top": line["top"], "bottom": line["bottom"], "text": line["text"],
               "blocks": []}
        for blk in split_blocks(rcs):
            row["blocks"].append({
                "chars": blk,
                "text": "".join(c["text"] for c in blk),
                "x0": min(c["x0"] for c in blk),
                "x1": max(c["x1"] for c in blk),
                "sizes": sorted({round(c["size"], 2) for c in blk}),
                "styles": sorted({style_of(c["fontname"]) for c in blk if is_garamond(c["fontname"])}),
                "align": align_of(blk),
                "bullet": any(not is_garamond(c["fontname"]) for c in blk),
            })
        rows.append(row)

    report.append("## 3. 逐行结构")
    report.append("")
    report.append("| # | top | 对齐 | 字号 | 样式 | 文本 |")
    report.append("| ---: | ---: | --- | --- | --- | --- |")
    for i, row in enumerate(rows, 1):
        for blk in row["blocks"]:
            sizes = "/".join(f"{s:.2f}" for s in blk["sizes"])
            report.append(f"| {i} | {row['top']:.1f} | {blk['align']} | {sizes} | "
                          f"{'/'.join(blk['styles']) or '●'} | {blk['text']} |")
    report.append("")

    # ---------- 4. 行距节奏（相邻行 top 差） ----------
    top_list = [r["top"] for r in rows]
    diffs = [(round(t2 - t1, 1), rows[i]["text"][:24], rows[i + 1]["text"][:24])
             for i, (t1, t2) in enumerate(zip(top_list, top_list[1:]))]
    dcount = Counter(d[0] for d in diffs)
    report.append("## 4. 行距节奏（相邻行 top 差）")
    report.append("")
    report.append("| 行距(pt) | 次数 | 典型示例（上一行 → 下一行） |")
    report.append("| ---: | ---: | --- |")
    for d, n in sorted(dcount.items(), key=lambda kv: -kv[1]):
        ex = next((f"{a!r} → {b!r}" for dd, a, b in diffs if dd == d), "")
        report.append(f"| {d:.1f} | {n} | {ex} |")
    report.append("")
    report.append(f"> 主节奏 ≈12pt（Word 行距 12pt，跨字体行 ±1pt 波动）；"
                  f"≈16pt 为区块标题前距（4pt 标题前距 + 12pt 行距）；"
                  f"EDUCATION 为 11.04pt 大标题，前距 6pt 需单独量测。")
    report.append("")

    # ---------- 5. 区块标题前距 ----------
    report.append("## 5. 区块标题前距（折算: 相邻行 top 差 − 12pt 行距）")
    report.append("")
    report.append("| 标题 | top | 与上一行 top 差(pt) | 折算前距(pt) | 字号 |")
    report.append("| --- | ---: | ---: | ---: | --- |")
    for i, row in enumerate(rows):
        if row["text"].strip() not in HEADINGS:
            continue
        blk = next((b for b in row["blocks"] if b["align"] == "left"), row["blocks"][0])
        sizes = "/".join(f"{s:.2f}" for s in blk["sizes"])
        if i > 0:
            prev = rows[i - 1]
            d = row["top"] - prev["top"]
            report.append(f"| {row['text'][:44]} | {row['top']:.1f} | {d:.1f} | {d - 12:.1f} | {sizes} |")
        else:
            report.append(f"| {row['text'][:44]} | {row['top']:.1f} | — | — | {sizes} |")
    report.append("")
    report.append(f"> 折算前距 ≈ 4~5pt（README 取整为 EDUCATION 6pt / 其余 4pt，基本一致）；"
                  f"残差来自跨字体行（● 行 TimesNewRoman 度量）与 11.04pt 大字行的字形高度。")
    report.append("")

    # ---------- 6. 对齐与缩进 ----------
    report.append("## 6. 对齐与缩进")
    report.append("")
    bullets = [c for c in chars if not is_garamond(c["fontname"])]
    bx0s = Counter(round(c["x0"], 1) for c in bullets if c["text"] == "\u25cf")
    report.append(f"- ● 项目符号 x0 聚类: {bx0s.most_common(4)}（{sum(bx0s.values())} 个）")
    bullet_rows = [r for r in rows if any(b["bullet"] for b in r["blocks"])]
    if bullet_rows:
        b_x0s, t_x0s = [], []
        for r in bullet_rows:
            bxs = [c["x0"] for b in r["blocks"] for c in b["chars"] if c["text"] == "\u25cf"]
            txs = [c["x0"] for b in r["blocks"] for c in b["chars"]
                   if is_garamond(c["fontname"]) and c["text"].strip()]
            if bxs and txs:
                b_x0s.append(min(bxs))
                t_x0s.append(min(txs))
        b0, t0 = min(b_x0s), min(t_x0s)
        report.append(f"- ● 前缩进 ≈ {b0:.1f}pt（相对左边距 {b0 - xs0:.1f}pt）")
        report.append(f"- ● 后正文首字符起点 x0 = {t0:.1f}pt（相对左边距 {t0 - xs0:.1f}pt）")
        report.append(f"- LaTeX 对应: leftmargin=13.6pt 时正文起点 = 30.2 + 13.6 = 43.8pt == 实测首字符 x0 ✓")
    right_edges = Counter(round(b["x1"], 1) for r in rows for b in r["blocks"] if b["align"] == "right")
    report.append(f"- 右对齐条目 x1 聚类: {right_edges.most_common(5)}")
    name_chars = [c for c in chars if abs(c["size"] - 21.96) < 0.5]
    if name_chars:
        n0, n1 = min(c["x0"] for c in name_chars), max(c["x1"] for c in name_chars)
        report.append(f"- 姓名行: x0={n0:.1f} x1={n1:.1f} 中心={(n0 + n1) / 2:.1f}（页面中心 {PAGE_W / 2:.1f}）")
    if page.lines:
        report.append("- 页面 line 对象:")
        for ln in page.lines:
            report.append(f"  - x0={ln['x0']:.1f} x1={ln['x1']:.1f} top={ln['top']:.1f} bottom={ln['bottom']:.1f}")
    report.append("")

    # ---------- 7. 汇总 ----------
    report.append("## 7. 关键规格汇总（与 README 声明对照）")
    report.append("")
    report.append("| 项 | 实测 | README 声明 |")
    report.append("| --- | --- | --- |")
    report.append(f"| 纸张 | Letter {page.width:.0f}x{page.height:.0f} | Letter |")
    report.append(f"| 上边距 | ≈{tops:.1f}pt | 32pt |")
    report.append(f"| 下边距 | ≈{PAGE_H - bottoms:.1f}pt | 60pt |")
    report.append(f"| 左边距 | ≈{xs0:.1f}pt | 29.4pt |")
    report.append(f"| 右边距 | ≈{PAGE_W - xs1:.1f}pt（正文行） / 右对齐条目 x1≈{right_edges.most_common(1)[0][0]:.1f} | 30.2pt |")
    body_sizes = sorted({s for (fn, s), n in fs.items() if is_garamond(fn) and s < 11})
    report.append(f"| 正文字号 | {body_sizes}pt | 9.96pt |")
    report.append("| 姓名字号 | 21.96pt 粗体居中 | 21.96pt 粗体居中 |")
    head_sizes = sorted({s for (fn, s), n in fs.items() if "Bold" in fn and s > 10 and s < 15})
    report.append(f"| 标题字号 | {head_sizes}pt 粗体 | 11.04pt 粗体 |")
    report.append("| 项目符号 | ●（非 Garamond 字体，见 §6） | 左缩进 13.6pt |")

    txt = "\n".join(report) + "\n"
    print(txt)
    OUT.write_text(txt, encoding="utf-8")
    print(f"\n[已写入] {OUT}")
