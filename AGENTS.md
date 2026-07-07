# AGENTS.md — 项目约定

## PowerShell 执行 Python

- ❌ 禁止用 `python -c "..."` 内联代码（`|`、`{`、`"`、`$` 会被 PowerShell 劫持）
- ✅ 必须用 **PowerShell here-string**：`python -c @'...'@`

## 终端编码

- 每条 bash 命令最前面加：`chcp 65001 >$null; $env:PYTHONIOENCODING='utf-8'`
- 避免 GBK 导致的 Unicode 报错

## 示例

```powershell
chcp 65001 >$null; $env:PYTHONIOENCODING='utf-8'; python -c @'
import json
# 想写什么写什么，零转义
print("a", "b", sep="|")
'@
```
