# 工程方向题目：开发简易版Make工具(minimake)（C语言实现）

## 前言

### 1. 操作系统要求
- **推荐使用 Linux 操作系统**，推荐发行版 **Ubuntu**，方便上手。
- 可以考虑 **WSL（适用于 Linux 的 Windows 子系统）**：
  - [官方文档](https://code.visualstudio.com/docs/cpp/config-wsl)
  - [安装指南](https://learn.microsoft.com/zh-cn/windows/wsl/install)
- **开发环境搭建参考**：
  - [VSCode 配置 Linux 开发环境](https://code.visualstudio.com/docs/cpp/config-linux)
- **云主机选择**（例如华为云，有免费额度可临时使用）：  
  - [华为云开发者空间](https://developer.huaweicloud.com/space/devportal/desktop)

### 2. 代码提交与编译要求
- 我们希望你的工程可以通过 **gcc 等工具一键编译、运行**，有明显的构建入口。
- **尽量减少使用第三方库**，优先使用标准库和 POSIX 标准库。

### 3. 学习态度与文档要求
- 完成度并非唯一考察标准，我们更看重你的 **学习态度与能力**。
- 你需要提交一份 **学习文档**，记录学习过程中的重点与疑点。
- **确保文档内容你完全理解**，该文档会作为答辩提问的来源之一。

### 4. 自动化测试
- 我们编写了自动化测试程序，会以程序的一些输出作为 **检查点**。
- **部分测试样例将开源**，供大家参考。

### 5. 代码组织
- **请采用多文件开发**，实现模块化组织，不要把所有函数放在一个文件里。

---

## 项目背景

理解构建工具的核心原理是提升系统编程能力的重要环节。  
通过实现 **简化版 Make 工具**，你将掌握：
- **命令行工具开发范式**
- **构建规则解析与执行**
- **时间戳比较算法**
- **文件依赖关系管理**

### 终极目标
**实现构建系统的自举**。

### 任务注意事项
**请按顺序完成任务**，前置任务也是重要的考核点。

---

## 阶段 -1：版本控制工具 Git

### 版本控制的重要性
Git 作为目前最常用的代码版本控制工具，可以：
- 记录代码的所有修改历史
- 便于高效协作
- 自动跟踪文件变更（内容、时间、修改者）
- 支持回退到任意历史版本，防止工作成果丢失

**要求：**
- **使用 Git 管理本次考核的代码**
- **提交记录应体现代码的迭代过程**

### 任务列表
- [ ] 自行查阅资料，学习 Git 的基本用法
- [ ] 建立远程仓库（Gitee 或 GitHub），同步并管理代码
- [ ] 任务提交时要有完整的 Git 历史记录

---

## 阶段 0：知识准备

### 目标
1. 理解 **Make** 工具的核心功能
2. 掌握基础 **Makefile 语法**
   ```makefile
   app: main.c utils.c  # 目标: app，依赖: main.c utils.c
       gcc -o app main.c utils.c  # 编译命令
   ```

1. 学习 **make 工具的使用方法**
2. 了解 **C 语言编译流程（4 个阶段）**
3. 熟悉 **C 语言多文件开发方法**

------

## 阶段 1：基础框架搭建（难度：★）

### 目标

创建程序的基本结构，实现 **命令行交互** 与 **简单命令执行**。

### 任务 1：命令行参数解析

**要求：**

- 学习使用 `argc` 和 `argv` 解析用户输入
- 实现 **`--help` 帮助信息**
- 处理 **参数缺失、格式错误等异常情况**

#### 检查点

1. **识别 `--help`**，输出包含 `"Usage"` 或 `"用法"`
2. **处理非法参数**，如 `--invalidparameter`

------

### 任务 2：预处理与文件读取

**要求：**

- 使用 `fopen()` 和 `fgets()` **逐行读取 `Makefile`**
- 预处理流程：
  - **过滤空行**
  - **去除行尾空格**
  - **去除注释（# 之后的内容）**
  - **支持 `-v` 或 `--verbose` 输出清理后的 Makefile**

#### 检查点

1. **文件是否存在**
2. **预处理输出符合要求**

------

### 任务 3：静态语法检查

**支持的 Makefile 语法：**

```makefile
app: main.c utils.c
    gcc -o app main.c utils.c
    git apply xxx.patch
    echo "success build app"
```

**验证规则：**

- 目标行必须包含 `:` 分隔符（如 `target: dependencies`）

- 命令 **必须** 以 **Tab** 开头

- 需要 

  输出带行号的错误信息

  - 示例错误

    ```makefile
    app main.c utils.c
        gcc -o app main.c utils.c
    ```

    报错：

    ```
    Line 1: Missing colon in target definition
    ```

------

## 阶段 2：解析器开发（难度：★★）

### 任务 1：规则解析、存储与检查

**要求：**

- **识别** 目标 (`target`)、依赖 (`dependencies`)、命令 (`commands`)
- **存储解析结果**（数据结构）
- 检查规则：
  - **禁止重复定义目标**
  - **确保依赖文件存在**

#### 检查点

- 目标重复定义

  ```makefile
  app: main.c utils.c
      gcc -o app main.c utils.c
  
  app: main.c utils.c
      gcc -o app main.c utils.c
  ```

  报错：

  ```
  Line 4: Duplicate target definition 'app'
  ```

- 依赖文件不存在

  ```makefile
  app: main.c utils.c missing.c
      gcc -o app main.c utils.c missing.c
  ```

  报错：

  ```
  Line 1: Invalid dependency 'missing.c'
  ```

------

### 任务 2：进行第一次编译

- 编写 `Makefile`

  ```makefile
  app: main.c utils.c
      gcc -o app main.c utils.c
  ```

- 运行命令

  ```sh
  minimake app
  ```

- **确保 `minimake` 能正确执行 `Makefile`**

------

## 阶段 3：依赖关系排序（难度：★★★）

### 目标

- 构建 **依赖关系图**
- 实现 **拓扑排序**（防止循环依赖）

**参考算法：**

- **LeetCode 题目**：[课程表](https://leetcode.cn/problems/course-schedule/description/)
- igraph 库
  - [官方文档](https://igraph.org/2024/11/06/igraph-0.10.15-c.html)

### 任务 1：依赖图构建

- **存储** 目标 (`target`) 与 依赖 (`dependency`)
- **实现** 依赖排序，保证正确的编译顺序

------

## 总结

- **按照任务顺序推进**
- **实现 `minimake`，掌握构建系统核心**
- **重点关注 Git 版本管理、Makefile 解析与依赖处理**