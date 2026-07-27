# LaTeX 语法速查

参考：[algony-tony.github.io/latex-cheatsheet](https://algony-tony.github.io/latex-cheatsheet/)

---

## 公式模式

| 类型 | 语法 |
|------|------|
| 行内公式 | `$...$` |
| 独行公式 | `$$...$$` |

---

## 希腊字母表

| 小写 | 代码 | 大写 | 代码 | 变形 | 代码 |
|------|------|------|------|------|------|
| $\alpha$ | `\alpha` | $A$ | `A` | | |
| $\beta$ | `\beta` | $B$ | `B` | | |
| $\gamma$ | `\gamma` | $\Gamma$ | `\Gamma` | | |
| $\delta$ | `\delta` | $\Delta$ | `\Delta` | | |
| $\epsilon$ | `\epsilon` | $E$ | `E` | $\varepsilon$ | `\varepsilon` |
| $\zeta$ | `\zeta` | $Z$ | `Z` | | |
| $\eta$ | `\eta` | $H$ | `H` | | |
| $\theta$ | `\theta` | $\Theta$ | `\Theta` | $\vartheta$ | `\vartheta` |
| $\iota$ | `\iota` | $I$ | `I` | | |
| $\kappa$ | `\kappa` | $K$ | `K` | $\varkappa$ | `\varkappa` |
| $\lambda$ | `\lambda` | $\Lambda$ | `\Lambda` | | |
| $\mu$ | `\mu` | $M$ | `M` | | |
| $\nu$ | `\nu` | $N$ | `N` | | |
| $\xi$ | `\xi` | $\Xi$ | `\Xi` | | |
| $o$ | `o` | $O$ | `O` | | |
| $\pi$ | `\pi` | $\Pi$ | `\Pi` | $\varpi$ | `\varpi` |
| $\rho$ | `\rho` | $P$ | `P` | $\varrho$ | `\varrho` |
| $\sigma$ | `\sigma` | $\Sigma$ | `\Sigma` | $\varsigma$ | `\varsigma` |
| $\tau$ | `\tau` | $T$ | `T` | | |
| $\upsilon$ | `\upsilon` | $\Upsilon$ | `\Upsilon` | | |
| $\phi$ | `\phi` | $\Phi$ | `\Phi` | $\varphi$ | `\varphi` |
| $\chi$ | `\chi` | $X$ | `X` | | |
| $\psi$ | `\psi` | $\Psi$ | `\Psi` | | |
| $\omega$ | `\omega` | $\Omega$ | `\Omega` | | |

---

## 比较符号

| 代码 | 显示 | 代码 | 显示 | 代码 | 显示 |
|------|------|------|------|------|------|
| `<` | $<$ | `>` | $>$ | `=` | $=$ |
| `\leq` | $\leq$ | `\geq` | $\geq$ | `\equiv` | $\equiv$ |
| `\gg` | $\gg$ | `\ggg` | $\ggg$ | `\ll` | $\ll$ |
| `\subset` | $\subset$ | `\supset` | $\supset$ | `\sim` | $\sim$ |
| `\subseteq` | $\subseteq$ | `\supseteq` | $\supseteq$ | `\simeq` | $\simeq$ |
| `\in` | $\in$ | `\ni` | $\ni$ | `\approx` | $\approx$ |
| `\mid` | $\mid$ | `\parallel` | $\parallel$ | `\cong` | $\cong$ |
| `\neq` | $\neq$ | `\propto` | $\propto$ | `\doteq` | $\doteq$ |

---

## 箭头

| 代码 | 显示 | 代码 | 显示 | 代码 | 显示 |
|------|------|------|------|------|------|
| `\leftarrow` | $\leftarrow$ | `\rightarrow` | $\rightarrow$ | `\uparrow` | $\uparrow$ |
| `\longleftarrow` | $\longleftarrow$ | `\longrightarrow` | $\longrightarrow$ | `\downarrow` | $\downarrow$ |
| `\Leftarrow` | $\Leftarrow$ | `\Rightarrow` | $\Rightarrow$ | `\Uparrow` | $\Uparrow$ |
| `\Longleftarrow` | $\Longleftarrow$ | `\Longrightarrow` | $\Longrightarrow$ | `\Downarrow` | $\Downarrow$ |
| `\leftrightarrow` | $\leftrightarrow$ | `\Leftrightarrow` | $\Leftrightarrow$ | `\updownarrow` | $\updownarrow$ |
| `\longleftrightarrow` | $\longleftrightarrow$ | `\Longleftrightarrow` | $\Longleftrightarrow$ | `\Updownarrow` | $\Updownarrow$ |
| `\mapsto` | $\mapsto$ | `\longmapsto` | $\longmapsto$ | `\nearrow` | $\nearrow$ |
| `\searrow` | $\searrow$ | `\swarrow` | $\swarrow$ | `\nwarrow` | $\nwarrow$ |

---

## 结构符号

| 代码 | 显示 | 代码 | 显示 | 代码 | 显示 |
|------|------|------|------|------|------|
| `\frac{abc}{xyz}` | $\frac{abc}{xyz}$ | `\overline{abc}` | $\overline{abc}$ | `\overrightarrow{abc}` | $\overrightarrow{abc}$ |
| `f'` | $f'$ | `\underline{abc}` | $\underline{abc}$ | `\overleftarrow{abc}` | $\overleftarrow{abc}$ |
| `\sqrt{abc}` | $\sqrt{abc}$ | `\widehat{abc}` | $\widehat{abc}$ | `\overbrace{abc}` | $\overbrace{abc}$ |
| `\sqrt[n]{abc}` | $\sqrt[n]{abc}$ | `\widetilde{abc}` | $\widetilde{abc}$ | `\underbrace{abc}` | $\underbrace{abc}$ |
| `\acute{a}` | $\acute{a}$ | `\bar{a}` | $\bar{a}$ | `\hat{a}` | $\hat{a}$ |
| `\dot{a}` | $\dot{a}$ | `\ddot{a}` | $\ddot{a}$ | `\grave{a}` | $\grave{a}$ |
| `\breve{a}` | $\breve{a}$ | `\vec{a}` | $\vec{a}$ | `\tilde{a}` | $\tilde{a}$ |
| `\binom{a}{b}` | $\binom{a}{b}$ | | | | |

---

## 函数名

| 代码 | 显示 | 代码 | 显示 | 代码 | 显示 |
|------|------|------|------|------|------|
| `\lim_{h\to 0}` | $\lim_{h\to 0}$ | `\ln` | $\ln$ | `\sin` | $\sin$ |
| `\exp` | $\exp$ | `\max` | $\max$ | `\inf` | $\inf$ |
| `\limsup` | $\limsup$ | `\liminf` | $\liminf$ | `\gcd` | $\gcd$ |

---

## 其他常用符号

| 代码 | 显示 | 代码 | 显示 | 代码 | 显示 |
|------|------|------|------|------|------|
| `\cdots` | $\cdots$ | `\vdots` | $\vdots$ | `\ldots` | $\ldots$ |
| `\infty` | $\infty$ | `\forall` | $\forall$ | `\exists` | $\exists$ |
| `\nabla` | $\nabla$ | `\partial` | $\partial$ | `\nexists` | $\nexists$ |
| `\emptyset` | $\emptyset$ | `\varnothing` | $\varnothing$ | `\square` | $\square$ |
| `\clubsuit` | $\clubsuit$ | `\diamondsuit` | $\diamondsuit$ | `\heartsuit` | $\heartsuit$ |
| `\spadesuit` | $\spadesuit$ | `\triangle` | $\triangle$ | `\triangledown` | $\triangledown$ |
| `\int` | $\int$ | `\iint` | $\iint$ | `\oint` | $\oint$ |
| `\cdot` | $\cdot$ | `\ast` | $\ast$ | `\star` | $\star$ |
| `\circ` | $\circ$ | `\bullet` | $\bullet$ | `\bigcirc` | $\bigcirc$ |
| `\times` | $\times$ | `\div` | $\div$ | `\odot` | $\odot$ |
| `\ominus` | $\ominus$ | `\oplus` | $\oplus$ | `\otimes` | $\otimes$ |
| `\sum` | $\sum$ | `\prod` | $\prod$ | `\coprod` | $\coprod$ |
| `\bigcap` | $\bigcap$ | `\bigcup` | $\bigcup$ | `\bigotimes` | $\bigotimes$ |

---

## 数学字体

```latex
\mathcal{A}    → $\mathcal{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}$
\mathbb{A}     → $\mathbb{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}$
\mathfrak{A}   → $\mathfrak{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}$
\mathsf{A}     → $\mathsf{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}$
\mathbf{A}     → $\mathbf{A B C D E F G H I J K L M N O P Q R S T U V W X Y Z}$
```

---

## 矩阵

使用 `array` 环境：

```
\begin{array}{cols}
row1 \\
row2 \\
... \\
rowm
\end{array}
```

- `cols` 参数：`l` 左对齐、`c` 居中、`r` 右对齐，可加 `|` 画竖线
- 行内用 `&` 分隔列，`\\` 换行
- `\hline` 加横线

示例 1：

```latex
\left(
    \begin{array}{cc}
     2\tau & 7\phi-\frac5{12} \\
        3\psi & \frac{\pi}8
    \end{array}
\right)
\left( \begin{array}{c} x \\ y \end{array} \right)
\quad \text{and} \quad
\left[
    \begin{array}{cc|r}
    3 & 4 & 5 \\
    1 & 3 & 729
    \end{array}
\right]
```

$$
\left(
    \begin{array}{cc}
     2\tau & 7\phi-\frac5{12} \\
        3\psi & \frac{\pi}8
    \end{array}
\right)
\left( \begin{array}{c} x \\ y \end{array} \right)
\quad \text{and} \quad
\left[
    \begin{array}{cc|r}
    3 & 4 & 5 \\
    1 & 3 & 729
    \end{array}
\right]
$$

示例 2（分段函数）：

```latex
f(z) =
\left\{
    \begin{array}{rcl}
        \overline{\overline{z^2}+\cos z} & \text{for} & |z|<3 \\
        0 & \text{for} & 3\leq|z|\leq5 \\
        \sin\overline{z} & \text{for} & |z|>5
    \end{array}
\right.
```

$$
f(z) =
\left\{
    \begin{array}{rcl}
        \overline{\overline{z^2}+\cos z} & \text{for} & |z|<3 \\
        0 & \text{for} & 3\leq|z|\leq5 \\
        \sin\overline{z} & \text{for} & |z|>5
    \end{array}
\right.
$$

---

## 多行公式对齐（align 环境）

```latex
\begin{align}
  \frac{d}{dx} \ln x &= \lim_{h\to 0} \frac{\ln(x+h) - \ln x}{h} \\
  &= \ln e^{1/x} &&\text{How this follows is left as an exercise.}\\
  &= \frac{1}{x} &&\text{Using the definition of ln as inverse function}
\end{align}
```

$$
\begin{align}
  \frac{d}{dx} \ln x &= \lim_{h\to 0} \frac{\ln(x+h) - \ln x}{h} \\
  &= \ln e^{1/x} &&\text{How this follows is left as an exercise.}\\
  &= \frac{1}{x} &&\text{Using the definition of ln as inverse function}
\end{align}
$$

---

## 上标与下标

```latex
x^2      x^{a+b}
x_1      x_{ij}
x^2_1    \hat{x}  \bar{x}  \tilde{x}
```

---

## 定界符

```latex
\left(  \right)  \left[  \right]  \left\{  \right\}
\left|  \right|  \left\langle  \right\rangle
```

`\left` 和 `\right` 自动调整括号大小。单边括号用 `\right.` 或 `\left.` 结束。

---

## 空格

```latex
a\,b     % 小空格
a\;b     % 中等空格
a\quad b % 大空格（一个em）
a\qquad b% 两倍大空格
a\;b     % 厚空格
a\!b     % 负空格（向左缩进）
```

---

## 文本在公式中

```latex
\text{文本内容}
\mbox{文本内容}
```

---

## 参考链接

- [LaTeX 数学符号参考文档 (PDF)](https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf)
- [CTAN LaTeX 符号全列表 (PDF)](https://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf)
- [MathJax basic tutorial and quick reference](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)
- [Greek Letters in LaTeX](https://www.geeksforgeeks.org/greek-letters-in-latex/)
