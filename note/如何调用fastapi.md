这是一个分步指南，用于指导你如何运行这个 `python-fastapi` 示例项目。

这个项目的目标是运行一个 Python FastAPI 服务器，该服务器充当一个“中间人”，它会接收你的请求，然后（使用你的 API 密钥）去查询 The Graph 协议的 "subgraph studio"，最后将结果返回给你。

-----

### 准备工作：检查你的工具

在开始之前，请确保你的电脑上安装了以下工具：

1.  **Git:** 用于下载代码。在终端输入 `git --version` 检查。
2.  **Python 3:** 用于运行程序。在终端输入 `python3 --version` 检查。
3.  **pip3:** Python 的包管理器，用于安装依赖。在终端输入 `pip3 --version` 检查。
4.  **curl:** (可选) 用于测试。macOS 和 Linux 通常自带。

-----

### 第 1 步：下载代码 (Clone Repo)

这一步是将 GitHub 上的代码库复制到你的本地电脑上。

**指令：**

```bash
git clone git@github.com:graphprotocol/query-examples.git
```

**💡 重要提示 (常见问题):**
你提供的命令 `git@github.com:...` 使用的是 **SSH 协议**。这需要你提前在电脑上设置好 SSH 密钥并将其添加到了你的 GitHub 账户。

**如果上述命令失败或卡住（询问密码）**，我强烈建议你使用 **HTTPS 协议**，它更简单，不需要设置密钥：

```bash
# 推荐使用这个 HTTPS 链接，更简单
git clone https://github.com/graphprotocol/query-examples.git
```

它下载到了你当前运行命令的目录下，并创建了一个名为 query-examples 的新文件夹。

根据你的提示符 (aave) C:\Users\10158>，你当时位于 C:\Users\10158 这个目录。

所以，下载完成后的完整路径是：

C:\Users\10158\query-examples

-----

### 第 2 步：进入项目目录 (CD)

下载完成后，你需要进入到这个 `python-fastapi` 示例的特定文件夹中。

**指令：**

```bash
cd ./query-examples/examples/python-fastapi
```

*(注意：你提供的原始路径 `cd ./examples/python-fastapi` 是假设你已经在 `query-examples` 目录里了，为保险起见，我用了完整路径)*

-----

### 第 3 步：安装 Python 依赖 (Install Deps)

这个项目依赖于一些 Python 库（如 `fastapi`, `uvicorn` 等）。`requirements.txt` 文件列出了所有需要的库。

**(推荐) 创建虚拟环境:**
为了不污染你系统的 Python 环境，最好先创建一个虚拟环境：

```bash
# 1. 创建一个名为 venv 的虚拟环境
python3 -m venv venv
# 2. 激活它
source venv/bin/activate 
# (在 Windows 上，你可能需要使用 `venv\Scripts\activate`)
```

**安装指令：**
现在，安装所有依赖：

```bash
pip3 install -r requirements.txt
```

-----

### 第 4 步：创建并配置 API 密钥 (Create Env)

你需要一个 API 密钥才能从 "Subgraph Studio" 获取数据。

1.  **复制模板文件:**
    `cp ./.env.example ./.env`

      * 这会创建一个名为 `.env` 的新文件。这个 `.env` 文件是你的私密配置文件（它在 `.gitignore` 中，不会被上传到 GitHub）。

2.  **获取你的 API 密钥:**

      * 你需要访问 **"Subgraph Studio"** (这是 The Graph 协议的一个服务)。
      * 登录并创建一个 API Key。

3.  **编辑 `.env` 文件:**

      * 用你的代码编辑器（如 VS Code）打开你刚刚创建的 `.env` 文件。
      * 你会看到类似这样的内容：
        ```
        API_KEY=
        ```
      * **将你从 Subgraph Studio 复制的 API 密钥粘贴到等号后面**。
      * 保存并关闭文件。

-----

### 第 5 步：运行服务器 (Run)

现在，一切准备就绪，可以启动 FastAPI Web 服务器了。

**指令：**

```bash
python3 -m uvicorn main:app --reload
```

  * `uvicorn`: 是一个 ASGI 服务器，用于运行 FastAPI 应用。
  * `main:app`: 告诉 uvicorn 去 `main.py` 文件里查找一个名为 `app` 的 FastAPI 实例。
  * `--reload`: 这是一个开发模式。当你修改代码时，服务器会自动重启。

**如果一切顺利**，你的终端会显示类似下面的信息，表示服务器正在运行：

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [...]
INFO:     Started server process [...]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**不要关闭这个终端！** 服务器需要它来保持运行。

-----

### 第 6 步：测试服务器 (Query the Subgraph)

最后一步是测试你的服务器是否工作正常。

**打开一个新的终端窗口**（保持上一步的服务器终端运行）。

**指令：**
复制并粘贴以下 `curl` 命令到新终端中：

```bash
curl http://localhost:8000/graphql -X POST -H 'Content-Type: application/json' -d '{"query": "query Subgraph($id: Bytes!) { subgraph(id: $id) {id nftID metadata { displayName }} }","variables":{"id":"8SxuHUYYBLHs1UkgFFYNaS7MgrEiAMbDyt5YzwZsSa6R"}}'
```

**这是在做什么？**

  * `curl`: 是一个向服务器发送 HTTP 请求的工具。
  * `http://localhost:8000/graphql`: 目标 URL，正是你本地运行的 FastAPI 服务器的 `/graphql` 路径。
  * `-X POST`: 使用 POST 方法（GraphQL 通常使用 POST）。
  * `-H 'Content-Type: application/json'`: 告诉服务器我们发送的是 JSON 数据。
  * `-d '...'`: 我们发送的数据 (Body)，它包含一个 GraphQL 查询语句和相应的变量。

**预期结果：**
如果你的 API 密钥正确并且服务器运行正常，你应该会收到一串 JSON 格式的返回数据，内容是关于那个 subgraph 的信息（例如 `nftID`, `displayName` 等）。

-----

### 总结

你已经成功地：

1.  下载了代码。
2.  安装了依赖。
3.  配置了你的私密 API 密钥。
4.  启动了本地 FastAPI 服务器。
5.  通过 `curl` 向你的服务器发送了一个 GraphQL 查询，服务器代理了这个查询到 Subgraph Studio 并返回了结果。