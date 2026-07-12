# 🖥️ Windows 终端命令行基础

> 一份面向零基础初学者的命令行入门指南。覆盖 PowerShell、命令提示符（CMD）和 Linux Bash 三种终端环境。

---

## 目录

- [一、什么是命令行？](#一什么是命令行)
- [二、PowerShell](#二powershell)
- [三、命令提示符 CMD](#三命令提示符-cmd)
- [四、Linux Bash（WSL / Git Bash）](#四linux-bashwsl--git-bash)
- [五、三终端命令对照表](#五三终端命令对照表)
- [六、总结与学习建议](#六总结与学习建议)

---

## 一、什么是命令行？

**命令行**（Command Line）是一种通过键盘输入文字指令来操控电脑的方式。与图形界面（鼠标点击图标）不同，命令行要求你**输入命令 → 按回车 → 看结果**。

### 为什么要学命令行？

| 场景 | 图形界面 | 命令行 |
|:---|:---|:---|
| 把 100 个 `.txt` 文件改成 `.md` | 逐个右键 → 重命名（累死） | 一行命令搞定 |
| 在 10GB 日志中找 "ERROR" | 用记事本打开 → 卡死 | `grep "ERROR" log.txt` 秒出 |
| 远程管理服务器 | 需要远程桌面 | `ssh` 一行连接 |
| 自动化重复任务 | 手动做 | 写脚本自动跑 |

### 三种终端简介

Windows 上有三种主流的命令行环境：

| 终端 | 启动方式 | 特点 |
|:---|:---|:---|
| **PowerShell** | 开始菜单搜索 "PowerShell" | 微软现代终端，功能最强大 |
| **CMD（命令提示符）** | Win+R → 输入 `cmd` → 回车 | Windows 经典终端，语法最简单 |
| **Bash** | 安装 Git 后右键 → "Git Bash Here" | Linux 风格，跨平台开发首选 |

> 💡 三者可以共存。日常推荐 **PowerShell** 或 **Bash**。

---

## 二、PowerShell

### 2.1 启动方法

- **方法一**：按 `Win` 键，搜索 "PowerShell"，点击打开。
- **方法二**：在任意文件夹地址栏输入 `powershell` 后回车。
- **方法三**：按 `Win + R`，输入 `powershell`，回车。

启动后你会看到类似这样的提示符：

```
PS C:\Users\你的用户名>
```

`PS` 表示 PowerShell，`C:\Users\...` 是你当前所在的位置（路径）。

---

### 2.2 基本命令与示例

> 每个示例中，`PS> ` 后面的内容是**你输入的命令**，下一行是**电脑的输出结果**。

#### 1. 查看当前目录的内容（列出文件）

```powershell
// PowerShell
PS> Get-ChildItem

    目录: C:\Users\nolan

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/7/12     14:30                Desktop
d-----        2026/7/11      9:15                Documents
-a----        2026/7/10     16:00           1234 readme.txt
```

> **解释**：`Get-ChildItem` 列出当前位置的所有文件和文件夹。`d-----` 开头的是目录（文件夹），`-a----` 开头的是文件。

**常用别名**：`ls` 和 `dir` 也能用，效果相同。

```powershell
// PowerShell
PS> ls

    目录: C:\Users\nolan

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/7/12     14:30                Desktop
d-----        2026/7/11      9:15                Documents
-a----        2026/7/10     16:00           1234 readme.txt
```

#### 2. 切换目录（进入文件夹）

```powershell
// PowerShell
PS> Set-Location C:\Users\nolan\Documents
PS> Get-Location

Path
----
C:\Users\nolan\Documents
```

> **解释**：`Set-Location`（别名 `cd`）用于切换当前目录。`Get-Location`（别名 `pwd`）显示当前所在位置。

```powershell
// PowerShell
PS> cd ..                // 返回上一级目录
PS> cd ~                 // 回到用户主目录
PS> cd Documents         // 进入当前目录下的 Documents 文件夹
```

#### 3. 创建新文件夹

```powershell
// PowerShell
PS> New-Item -ItemType Directory -Name 我的文件夹

    目录: C:\Users\nolan

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/7/13     10:00                我的文件夹
```

> **解释**：`New-Item -ItemType Directory` 创建一个新文件夹。`-Name` 指定文件夹名称。

**简写方式**（用别名 `mkdir`）：

```powershell
// PowerShell
PS> mkdir 测试目录

    目录: C:\Users\nolan

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/7/13     10:01                测试目录
```

#### 4. 创建新文件

```powershell
// PowerShell
PS> New-Item -ItemType File -Name hello.txt

    目录: C:\Users\nolan

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2026/7/13     10:02              0 hello.txt
```

> **解释**：`-ItemType File` 表示创建文件。刚创建的文件大小为 0 字节（空的）。

#### 5. 向文件写入内容

```powershell
// PowerShell
PS> Set-Content -Path hello.txt -Value "你好，世界！"
PS> Get-Content hello.txt

你好，世界！
```

> **解释**：`Set-Content` 向文件写入内容（会覆盖原有内容）。`Get-Content` 查看文件内容。

#### 6. 追加内容到文件

```powershell
// PowerShell
PS> Add-Content -Path hello.txt -Value "这是第二行。"
PS> Get-Content hello.txt

你好，世界！
这是第二行。
```

> **解释**：`Add-Content` 在文件末尾追加新内容（不覆盖原有内容）。

#### 7. 复制文件

```powershell
// PowerShell
PS> Copy-Item hello.txt hello_backup.txt
PS> Get-ChildItem hello*

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2026/7/13     10:05             18 hello.txt
-a----        2026/7/13     10:05             18 hello_backup.txt
```

> **解释**：`Copy-Item 源文件 目标文件` 复制文件。`hello*` 是通配符，匹配所有以 "hello" 开头的文件。

#### 8. 重命名 / 移动文件

```powershell
// PowerShell
PS> Move-Item hello_backup.txt hello_old.txt
PS> Get-ChildItem hello*

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2026/7/13     10:06             18 hello_old.txt
-a----        2026/7/13     10:02             18 hello.txt
```

> **解释**：`Move-Item` 既可移动文件到其他目录，也可用于重命名（移动到"同一目录下的新名字"= 重命名）。

#### 9. 删除文件

```powershell
// PowerShell
PS> Remove-Item hello_old.txt
PS> Get-ChildItem hello*

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2026/7/13     10:02             18 hello.txt
```

> **解释**：`Remove-Item` 删除文件。⚠️ 删除后**不进回收站**，无法恢复！

#### 10. 清屏

```powershell
// PowerShell
PS> Clear-Host

（屏幕内容被清空，光标回到左上角）
```

> **解释**：`Clear-Host`（别名 `cls`）清空终端屏幕，方便重新开始。

#### 11. 查看命令帮助

```powershell
// PowerShell
PS> Get-Help Get-ChildItem

名称
    Get-ChildItem

语法
    Get-ChildItem [[-Path] <string[]>] [[-Filter] <string>] [<CommonParameters>]
    Get-ChildItem [[-Filter] <string>] -LiteralPath <string[]> [<CommonParameters>]

别名
    gci
    ls
    dir

备注
    此 cmdlet 获取一个或多个指定位置中的项。
```

> **解释**：`Get-Help 命令名` 查看任何命令的详细说明。遇到不认识的命令时，这是第一求助途径。

#### 12. 查看正在运行的程序（进程）

```powershell
// PowerShell
PS> Get-Process | Select-Object -First 5

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    150      10     2500       8000       0.50   1234   1 chrome
     80       6     1200       4000       0.20   5678   1 notepad
    200      15     8000      20000       2.00   9012   1 explorer
     50       5      800       3000       0.10   3456   1 cmd
    120       8     3000      10000       1.50   7890   1 powershell
```

> **解释**：`Get-Process` 列出所有正在运行的程序。`|` 是管道（把左边命令的输出传给右边）。`Select-Object -First 5` 只取前 5 条。

#### 13. 管道（Pipeline）— 筛选数据

```powershell
// PowerShell
PS> Get-Process | Where-Object {$_.WorkingSet -gt 100MB}

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    200      15     8000     150000       2.00   9012   1 explorer
    300      20    12000     200000       5.00   1111   1 chrome
```

> **解释**：`Where-Object` 过滤数据。`$_` 代表管道传来的每个对象，`.WorkingSet` 是内存使用量。这条命令的意思是"列出内存占用超过 100MB 的进程"。

#### 14. 管道 — 排序

```powershell
// PowerShell
PS> Get-ChildItem | Sort-Object Length -Descending | Select-Object -First 5

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2026/7/10     16:00          50000 大文件.zip
-a----        2026/7/12     10:30          12345 报告.docx
-a----        2026/7/11     14:00           2048  照片.png
-a----        2026/7/13     10:02             18  hello.txt
-a----        2026/7/12      9:00              0  empty.txt
```

> **解释**：`Sort-Object Length -Descending` 按文件大小从大到小排列。三个命令用 `|` 串联：列文件 → 排序 → 取前5。

#### 15. 输出重定向（把结果保存到文件）

```powershell
// PowerShell
PS> Get-ChildItem > 文件列表.txt
PS> Get-Content 文件列表.txt

    目录: C:\Users\nolan

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/7/12     14:30                Desktop
d-----        2026/7/11      9:15                Documents
-a----        2026/7/13     10:02             18 hello.txt
-a----        2026/7/13     10:10            500 文件列表.txt
```

> **解释**：`>` 把命令的输出保存到文件中（覆盖原内容）。`>>` 则追加到文件末尾。

#### 16. 查看日期和时间

```powershell
// PowerShell
PS> Get-Date

2026年7月13日 10:15:30
```

```powershell
// PowerShell
PS> Get-Date -Format "yyyy-MM-dd"

2026-07-13
```

> **解释**：`Get-Date` 获取当前日期时间。`-Format` 参数可以自定义显示格式。

#### 17. 查看网络配置

```powershell
// PowerShell
PS> Get-NetIPAddress | Where-Object {$_.AddressFamily -eq "IPv4"} | Select-Object IPAddress

IPAddress
---------
192.168.1.100
127.0.0.1
```

> **解释**：`Get-NetIPAddress` 查看本机 IP 地址。通过管道筛选 IPv4 地址。

---

## 三、命令提示符 CMD

### 3.1 启动方法

- **方法一**：按 `Win + R`，输入 `cmd`，回车。
- **方法二**：开始菜单搜索 "命令提示符" 或 "cmd"。
- **方法三**：在文件夹地址栏输入 `cmd`，回车（会在该目录下打开）。

启动后你会看到：

```
Microsoft Windows [版本 10.0.xxxxx]
(c) Microsoft Corporation。保留所有权利。

C:\Users\你的用户名>
```

`>` 是 CMD 的提示符，光标闪烁处等待你输入命令。

---

### 3.2 基本命令与示例

#### 1. 查看当前目录的内容

```cmd
// CMD
C:\Users\nolan> dir

 驱动器 C 中的卷是 Windows
 卷的序列号是 XXXX-XXXX

 C:\Users\nolan 的目录

2026/07/12  14:30    <DIR>          Desktop
2026/07/11  09:15    <DIR>          Documents
2026/07/10  16:00             1,234 readme.txt
               1 个文件          1,234 字节
               2 个目录  50,000,000,000 可用字节
```

> **解释**：`dir` 列出当前目录的所有文件和文件夹。`<DIR>` 标记的是文件夹。

**常用参数**：

```cmd
// CMD
C:\Users\nolan> dir /b          // /b：简洁模式（只显示文件名）

Desktop
Documents
readme.txt
```

#### 2. 切换目录

```cmd
// CMD
C:\Users\nolan> cd Documents

C:\Users\nolan\Documents>
```

> **解释**：`cd 文件夹名` 进入该文件夹。提示符会随之改变，显示当前路径。

```cmd
// CMD
C:\Users\nolan\Documents> cd ..          // 返回上一级

C:\Users\nolan>

C:\Users\nolan\Documents> cd \           // 回到根目录

C:\>
```

> **解释**：`..` 代表上一级目录，`\` 代表当前驱动器的根目录（最顶层）。

#### 3. 查看当前路径

```cmd
// CMD
C:\Users\nolan\Documents> cd

C:\Users\nolan\Documents
```

> **解释**：在 CMD 中，不加参数直接输入 `cd` 就显示当前路径。

#### 4. 创建文件夹

```cmd
// CMD
C:\Users\nolan> md 我的文件夹

C:\Users\nolan> dir /b

Desktop
Documents
readme.txt
我的文件夹
```

> **解释**：`md`（或 `mkdir`）创建新文件夹。

#### 5. 创建文件

CMD 没有直接的"创建空文件"命令，但可以用 `echo` 间接实现：

```cmd
// CMD
C:\Users\nolan> echo 你好 > hello.txt

C:\Users\nolan> type hello.txt
你好
```

> **解释**：`echo 文本 > 文件名` 把文本写入文件。`>` 是重定向符号。如果文件不存在，会自动创建。

#### 6. 查看文件内容

```cmd
// CMD
C:\Users\nolan> type hello.txt

你好
```

> **解释**：`type` 显示文本文件的内容。

#### 7. 追加内容到文件

```cmd
// CMD
C:\Users\nolan> echo 这是第二行 >> hello.txt

C:\Users\nolan> type hello.txt
你好
这是第二行
```

> **解释**：`>>` 把内容**追加**到文件末尾。`>` 是覆盖，`>>` 是追加。

#### 8. 复制文件

```cmd
// CMD
C:\Users\nolan> copy hello.txt hello_copy.txt
已复制         1 个文件。

C:\Users\nolan> dir /b hello*
hello.txt
hello_copy.txt
```

> **解释**：`copy 源文件 目标文件` 复制文件。CMD 会提示复制结果。

#### 9. 重命名 / 移动文件

```cmd
// CMD
C:\Users\nolan> move hello_copy.txt hello_old.txt
移动了         1 个文件。

C:\Users\nolan> dir /b hello*
hello.txt
hello_old.txt
```

> **解释**：`move` 可以移动文件到其他目录，也可以重命名文件。

#### 10. 删除文件

```cmd
// CMD
C:\Users\nolan> del hello_old.txt

C:\Users\nolan> dir /b hello*
hello.txt
```

> **解释**：`del` 删除文件。⚠️ 不会进入回收站，删除后无法恢复！

#### 11. 删除文件夹

```cmd
// CMD
C:\Users\nolan> rd /s /q 测试目录

C:\Users\nolan> dir /b
（测试目录已消失）
```

> **解释**：`rd`（Remove Directory）删除文件夹。`/s` 表示删除其中所有内容，`/q` 表示静默模式（不确认）。

#### 12. 清屏

```cmd
// CMD
C:\Users\nolan> cls

（屏幕被清空）
```

> **解释**：`cls`（Clear Screen）清空终端屏幕。

#### 13. 查看命令帮助

```cmd
// CMD
C:\Users\nolan> help dir

显示目录中的文件和子目录列表。

DIR [drive:][path][filename] [/A[[:]attributes]] [/B] [/C] [/D] [/L] [/N]
    [/O[[:]sortorder]] [/P] [/Q] [/R] [/S] [/T[[:]timefield]] [/W] [/X] [/4]

  /B          使用空格式(没有标题信息或摘要)。
  /S          显示指定目录和所有子目录中的文件。
  ...
```

> **解释**：`help 命令名` 查看该命令的详细用法。也可以用 `命令名 /?`（如 `dir /?`）。

#### 14. 查看正在运行的程序

```cmd
// CMD
C:\Users\nolan> tasklist | more

映像名称                       PID 会话名              会话#       内存使用
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0      2,500 K
chrome.exe                    1234 Console                    1    150,000 K
notepad.exe                   5678 Console                    1      5,000 K
cmd.exe                       9012 Console                    1      3,500 K
```

> **解释**：`tasklist` 列出所有正在运行的程序。`| more` 表示分页显示（按任意键翻页）。

#### 15. 管道 — 搜索文本

```cmd
// CMD
C:\Users\nolan> tasklist | findstr "chrome"

chrome.exe                    1234 Console                    1    150,000 K
chrome.exe                    1111 Console                    1    120,000 K
```

> **解释**：`findstr` 在输出中搜索指定文字。这里从进程列表中筛选出包含 "chrome" 的行。

#### 16. 输出重定向

```cmd
// CMD
C:\Users\nolan> dir > 目录列表.txt

C:\Users\nolan> type 目录列表.txt

 驱动器 C 中的卷是 Windows
 卷的序列号是 XXXX-XXXX

 C:\Users\nolan 的目录

2026/07/12  14:30    <DIR>          Desktop
2026/07/11  09:15    <DIR>          Documents
2026/07/13  10:10               500 目录列表.txt
...
```

> **解释**：`>` 把命令输出保存到文件。`>>` 追加到文件末尾。

#### 17. 查看日期

```cmd
// CMD
C:\Users\nolan> date /t

2026/07/13 周一
```

```cmd
// CMD
C:\Users\nolan> time /t

10:15
```

> **解释**：`date /t` 显示当前日期，`time /t` 显示当前时间。

---

## 四、Linux Bash（WSL / Git Bash）

### 4.1 启动方法

**WSL（Windows Subsystem for Linux）**：
- 开始菜单搜索 "WSL" 或 "Ubuntu" 等 Linux 发行版名称。
- 首次使用需要在 PowerShell 中运行 `wsl --install`。

**Git Bash**（安装 Git 时自带）：
- 在任意文件夹空白处**右键** → "Git Bash Here"。
- 或在开始菜单搜索 "Git Bash"。

启动后你会看到：

```bash
nolan@DESKTOP MINGW64 ~
$
```

`$` 是 Bash 的提示符（普通用户），`~` 表示当前在用户主目录。

---

### 4.2 基本命令与示例

#### 1. 查看当前目录内容

```bash
// Bash
$ ls

Desktop/  Documents/  hello.txt  readme.txt
```

> **解释**：`ls`（List）列出当前目录的文件和文件夹。末尾带 `/` 的是目录。

**详细模式**：

```bash
// Bash
$ ls -la

total 20
drwxr-xr-x 1 nolan 197609    0 Jul 13 10:00 ./
drwxr-xr-x 1 nolan 197609    0 Jul 10 09:00 ../
drwxr-xr-x 1 nolan 197609    0 Jul 12 14:30 Desktop/
drwxr-xr-x 1 nolan 197609    0 Jul 11 09:15 Documents/
-rw-r--r-- 1 nolan 197609   18 Jul 13 10:02 hello.txt
-rw-r--r-- 1 nolan 197609 1234 Jul 10 16:00 readme.txt
```

> **解释**：`-l` 显示详细信息（权限、大小、日期），`-a` 显示隐藏文件（以 `.` 开头的文件）。

#### 2. 切换目录

```bash
// Bash
$ cd Documents
$ pwd
/c/Users/nolan/Documents
```

> **解释**：`cd`（Change Directory）切换目录，`pwd`（Print Working Directory）显示当前路径。

```bash
// Bash
$ cd ..               // 返回上一级
$ cd ~                // 回到主目录
$ cd /c/              // 进入 C 盘根目录（Git Bash 中的路径写法）
```

> ⚠️ Git Bash 中，Windows 的 `C:\` 写作 `/c/`，`D:\` 写作 `/d/`。

#### 3. 创建文件夹

```bash
// Bash
$ mkdir 我的文件夹

$ ls
Desktop/  Documents/  hello.txt  readme.txt  我的文件夹/
```

> **解释**：`mkdir`（Make Directory）创建新文件夹。

**一次创建多层目录**：

```bash
// Bash
$ mkdir -p project/src/components

$ ls project/
src/

$ ls project/src/
components/
```

> **解释**：`-p` 参数会自动创建路径中所有不存在的父目录。

#### 4. 创建空文件

```bash
// Bash
$ touch newfile.txt

$ ls -l newfile.txt
-rw-r--r-- 1 nolan 197609 0 Jul 13 10:30 newfile.txt
```

> **解释**：`touch` 创建一个空的文件。如果文件已存在，则更新其"最后修改时间"。

#### 5. 查看文件内容

```bash
// Bash
$ cat hello.txt

你好，世界！
这是第二行。
```

> **解释**：`cat`（Concatenate）显示文件内容。

**带行号显示**：

```bash
// Bash
$ cat -n hello.txt

     1  你好，世界！
     2  这是第二行。
```

#### 6. 向文件写入 / 追加内容

```bash
// Bash
$ echo "Hello World" > greet.txt      // 覆盖写入
$ cat greet.txt
Hello World

$ echo "你好 Bash" >> greet.txt       // 追加写入
$ cat greet.txt
Hello World
你好 Bash
```

> **解释**：`echo` 输出文本，`>` 覆盖写入文件，`>>` 追加到文件末尾。

#### 7. 复制文件

```bash
// Bash
$ cp hello.txt hello_backup.txt

$ ls hello*
hello.txt  hello_backup.txt
```

> **解释**：`cp`（Copy）复制文件。`*` 是通配符，匹配任意字符。

**复制整个文件夹**：

```bash
// Bash
$ cp -r project/ project_backup/

$ ls
project/  project_backup/
```

> **解释**：`-r`（recursive，递归）参数用于复制文件夹及其所有内容。

#### 8. 移动 / 重命名文件

```bash
// Bash
$ mv hello_backup.txt hello_old.txt

$ ls hello*
hello.txt  hello_old.txt
```

> **解释**：`mv`（Move）可移动文件到其他目录，也可用于重命名。

#### 9. 删除文件

```bash
// Bash
$ rm hello_old.txt

$ ls hello*
hello.txt
```

> **解释**：`rm`（Remove）删除文件。⚠️ 不可恢复！

**删除文件夹**：

```bash
// Bash
$ rm -rf project_backup/

$ ls
Desktop/  Documents/  hello.txt  readme.txt
```

> **解释**：`-r` 递归删除文件夹内容，`-f` 强制删除（不询问确认）。⚠️ `rm -rf` 非常危险，务必确认路径正确！

#### 10. 清屏

```bash
// Bash
$ clear

（屏幕被清空）
```

> **解释**：`clear` 清空终端屏幕。也可以用快捷键 `Ctrl + L`。

#### 11. 查看命令帮助

```bash
// Bash
$ ls --help

Usage: /usr/bin/ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -l                         use a long listing format
  -h, --human-readable       with -l, print sizes in human readable format
  ...
```

> **解释**：大多数 Bash 命令支持 `--help` 查看用法。也可以用 `man 命令名`（如 `man ls`）查看更详细的说明书。

#### 12. 查看正在运行的程序

```bash
// Bash
$ ps aux | head -5

USER     PID %CPU %MEM    VSZ   RSS TTY   STAT START   TIME COMMAND
nolan   1234  2.5  8.0 500000 150000 ?    Sl   10:00   0:30 /usr/bin/chrome
nolan   5678  0.1  1.0 100000  20000 ?    Ss   10:05   0:01 /usr/bin/bash
nolan   9012  0.0  0.5  50000  10000 pts/0 R+   10:15   0:00 ps aux
```

> **解释**：`ps aux` 列出所有进程的详细信息。`|` 是管道。`head -5` 只显示前 5 行。

#### 13. 管道 — 搜索文本（grep）

```bash
// Bash
$ ps aux | grep bash

nolan   5678  0.1  1.0 100000  20000 ?    Ss   10:05   0:01 /usr/bin/bash
nolan   9015  0.0  0.1   5000   2000 pts/0 S+   10:16   0:00 grep --color=auto bash
```

> **解释**：`grep` 是最强大的文本搜索工具。这里从进程列表中筛选含 "bash" 的行。

**在文件中搜索**：

```bash
// Bash
$ grep "ERROR" app.log           // 搜索含 ERROR 的行
$ grep -n "ERROR" app.log        // -n 显示行号
$ grep -i "error" app.log        // -i 忽略大小写
$ grep -c "ERROR" app.log        // -c 统计匹配行数
```

#### 14. 管道 — 排序

```bash
// Bash
$ cat scores.txt
张三 85
李四 92
王五 78

$ sort -k2 -n scores.txt
王五 78
张三 85
李四 92
```

> **解释**：`sort -k2 -n` 按第 2 列数字从小到大排序。`-k` 指定列，`-n` 按数字排序（而非字母）。

```bash
// Bash
$ sort -k2 -nr scores.txt        // -r 反向（从大到小）
李四 92
张三 85
王五 78
```

#### 15. 管道 — 统计行数 / 字数

```bash
// Bash
$ wc -l hello.txt                // 统计行数
2 hello.txt

$ wc -w hello.txt                // 统计单词数
5 hello.txt

$ wc -c hello.txt                // 统计字符数（字节数）
18 hello.txt
```

> **解释**：`wc`（Word Count）统计文本。`-l` 行数，`-w` 单词数，`-c` 字符数。

#### 16. 输出重定向与管道组合

```bash
// Bash
$ ls -l | grep ".txt" > txt_files.txt

$ cat txt_files.txt
-rw-r--r-- 1 nolan 197609   18 Jul 13 10:02 hello.txt
-rw-r--r-- 1 nolan 197609 1234 Jul 10 16:00 readme.txt
-rw-r--r-- 1 nolan 197609    0 Jul 13 10:35 txt_files.txt
```

> **解释**：这是一条组合命令——`ls -l` 列出所有文件 → `grep ".txt"` 筛选含 .txt 的行 → `>` 把结果保存到 `txt_files.txt`。

#### 17. 查看日期

```bash
// Bash
$ date
2026年 07月 13日 星期一 10:15:30 CST

$ date "+%Y-%m-%d %H:%M:%S"
2026-07-13 10:15:30
```

> **解释**：`date` 显示当前日期时间。`+` 后面可以自定义格式。

---

## 五、三终端命令对照表

> 下表汇总同一操作在三种终端中分别怎么写。**加粗**的命令是最推荐的写法。

| 操作 | PowerShell | CMD | Bash |
|:---|:---|:---|:---|
| **列出文件** | `Get-ChildItem` 或 `ls` | `dir` | `ls` |
| **详细列表** | `ls` | `dir` | `ls -l` |
| **含隐藏文件** | `ls -Force` | `dir /a` | `ls -a` |
| **切换目录** | `Set-Location` 或 `cd` | `cd` | `cd` |
| **当前路径** | `Get-Location` 或 `pwd` | `cd`（无参数） | `pwd` |
| **返回上级** | `cd ..` | `cd ..` | `cd ..` |
| **创建文件夹** | `mkdir` 或 `New-Item -Type Dir` | `md` 或 `mkdir` | `mkdir` |
| **创建文件** | `New-Item -Type File` | `echo > 文件名` | `touch` |
| **删除文件** | `Remove-Item` 或 `rm` | `del` | `rm` |
| **删除文件夹** | `Remove-Item -Recurse` | `rd /s` | `rm -rf` |
| **复制文件** | `Copy-Item` 或 `cp` | `copy` | `cp` |
| **复制文件夹** | `Copy-Item -Recurse` | `xcopy /s` | `cp -r` |
| **移动/重命名** | `Move-Item` 或 `mv` | `move` | `mv` |
| **查看文件内容** | `Get-Content` 或 `cat` | `type` | `cat` |
| **输出文本** | `Write-Output` 或 `echo` | `echo` | `echo` |
| **清屏** | `Clear-Host` 或 `cls` | `cls` | `clear` |
| **帮助** | `Get-Help 命令` | `help 命令` 或 `命令 /?` | `命令 --help` 或 `man 命令` |
| **查看进程** | `Get-Process` 或 `ps` | `tasklist` | `ps aux` |
| **搜索文本** | `Select-String` | `findstr` | `grep` |
| **排序** | `Sort-Object` | `sort` | `sort` |
| **统计行数** | `(Get-Content).Count` | `find /c /v ""` | `wc -l` |
| **管道** | `\|` | `\|` | `\|` |
| **覆盖写入** | `>` 或 `Out-File` | `>` | `>` |
| **追加写入** | `>>` 或 `Add-Content` | `>>` | `>>` |
| **显示日期** | `Get-Date` | `date /t` | `date` |

---

## 六、总结与学习建议

### 我应该用哪个？

| 你的需求 | 推荐终端 |
|:---|:---|
| 刚开始学命令行 | **PowerShell** — 同时兼容 `ls`/`dir`/`cd`，报错信息最友好 |
| 做 Windows 系统管理 | **PowerShell** — 原生功能最强大 |
| 学编程 / 做开发 | **Bash（Git Bash）** — 和 Linux/macOS 一致，开源工具最全 |
| 快速执行简单的文件操作 | 三者都可以，挑你最熟悉的 |

### 学习路径建议

1. **第一周**：只练 5 个命令 — `ls`/`dir`、`cd`、`mkdir`、`echo`、`cat`/`type`。在文件夹之间自由穿行。
2. **第二周**：加上 `cp`/`copy`、`mv`/`move`、`rm`/`del`。试着创建、复制、移动、删除文件。
3. **第三周**：学习**管道** `|` 和**重定向** `>` `>>`。这是命令行的真正威力所在。
4. **第四周**：学习 `grep`/`findstr`/`Select-String` 搜索文本。找一个大日志文件练手。

### 最重要的原则

> 🎯 **不要试图背命令。** 忘了就敲 `--help`、`/?` 或 `Get-Help`。用多了自然记住。

> 🎯 **分步来。** 复杂的管道先拆开，一个命令一个命令测试，确认每步输出正确再串起来。

> 🎯 **先在测试目录练。** 别在你的重要文件夹里试 `rm -rf` 或 `del`！建一个 `test/` 文件夹随便折腾。

---

*本教程共包含 **51 个命令示例**（PowerShell 17 个 + CMD 17 个 + Bash 17 个），覆盖日常高频操作。*
