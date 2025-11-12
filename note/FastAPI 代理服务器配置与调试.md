好的，这是一个精简版的开发日志，专门记录从“Python 环境和依赖已全部就绪”之后开始的**服务器配置**和**问题排查**步骤。

-----

## 开发日志：FastAPI 代理服务器配置与调试

**前提：** Conda 环境 `(aave)` 已激活（使用 `Python 3.10`），且 `requirements.txt` 和 `requests` 库均已成功安装。

### 阶段一：配置并启动服务器

**1. 配置 API 密钥**

  * **操作：** 复制 `.env.example` 模板文件到 `.env`。
  * **命令（Windows）：** `copy .\.env.example .\.env`
  * **细节：** 打开 `.env` 文件，粘贴从 Subgraph Studio 获取的 API 密钥。
  * **格式：** 确保格式为 `API_KEY=key...`，等号前后无空格，密钥本身无引号。

**2. 启动服务器**

  * **操作：** 在第一个终端窗口中启动 Uvicorn 服务器。
  * **命令：** `python -m uvicorn main:app --reload`
  * **日志：**
    ```
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ...
    INFO:     Application startup complete.
    ```

### 阶段二：解决 Windows 终端的 `curl` 兼容性问题

**3. 首次测试 (使用 `cmd.exe` `curl`)**

  * **操作：** 打开**第二个** `cmd.exe` 终端，运行 `curl` 命令。
  * **遇到的问题：** `curl` 本身报错。服务器日志（第一个终端）显示 `422 Unprocessable Entity` 错误，并提示 `Input should be a valid dictionary`。
  * **原因分析：** Windows 的 `cmd.exe` 终端无法正确解析 `curl` 命令中用于封装 JSON 数据的**单引号 (`'`)**，导致一个破损的 JSON 片段被发送到服务器。
  * **解决方案：** 放弃 `cmd.exe`，切换到 `PowerShell` 终端，它能更稳定地处理 JSON 字符串。
  * **PowerShell 切换命令：** `powershell`
  * **PowerShell 测试命令：**
    ```powershell
    Invoke-RestMethod -Uri http://localhost:8000/graphql -Method Post -ContentType 'application/json' -Body '{"query": "{ protocols(first: 5) ... }"}'
    ```

### 阶段三：解决 API 密钥加载问题

**4. `malformed API key` 错误**

  * **操作：** 运行 `Invoke-RestMethod` (PowerShell) 命令。
  * **遇到的问题：** PowerShell 返回一个 `errors` 块，内容为：`@{message=auth error: malformed API key}`。
  * **原因分析：**
    1.  （安全问题）API 密钥在交流中泄露，必须立即作废。
    2.  （技术原因）`.env` 文件很可能是在 `uvicorn` 服务器**启动后**才被正确修改的。`uvicorn --reload` 标志**不会**监视 `.env` 文件的变化。因此，服务器内存中仍然是旧的、无效的（或空的）API密钥。
  * **解决方案（关键）：**
    1.  **安全：** 登录 Subgraph Studio，**删除**泄露的 API 密钥，**创建**一个新密钥。
    2.  **停止：** **停止** `uvicorn` 服务器（在第一个终端按 `CTRL+C`）。
    3.  **更新：** 将**新**密钥正确填入 `.env` 文件。
    4.  **重启：** **重新启动** `uvicorn` (`python -m uvicorn main:app --reload`)。这个新进程会强制在启动时加载新的 `.env` 文件。

### 阶段四：解决 GraphQL 端点（Endpoint）路由错误

**5. `Type Query has no field protocols` 错误**

  * **操作：** API 密钥验证通过后，再次运行 `Invoke-RestMethod` 查询 `protocols`。
  * **遇到的问题：** 收到一个 GraphQL 错误：`Type Query has no field protocols`。
  * **原因分析：**
    1.  通过检查 `main.py` 文件的代码，发现它\*\*硬编码（Hard-code）\*\*了一个 `subgraph_url` 变量。
    2.  这意味着 FastAPI 服务器会**忽略**我们发送的任何 `variables`（比如 `id`），并**固定**将所有查询都转发到那个写死的 URL。
    3.  这个硬编码的 URL (`.../DZz4k...` 或其他）指向的子图并不包含 `protocols` 字段，导致查询失败。
  * **解决方案：**
    1.  从 The Graph 官网文档中找到了一个使用 `protocols` 查询的**官方 `curl` 示例**。
    2.  从该示例中提取了**正确**的 Subgraph URL：`https://gateway.thegraph.com/api/subgraphs/id/GQFbb95cE6d8mV989mL5figjaGaKCQB3xqYrr1bRyXqF`
    3.  **停止** `uvicorn` 服务器 (`CTRL+C`)。
    4.  **编辑** `main.py` 文件，将 `subgraph_url` 变量的值替换为这个正确的 URL。
    5.  **重启** `uvicorn` 服务器。

### 阶段五：成功（解决 PowerShell 显示问题）

**6. 成功，但数据显示异常**

  * **操作：** 服务器指向正确 URL 后，再次运行 `Invoke-RestMethod` 命令。
  * **日志 (PowerShell)：**
    ```powershell
    data
    ----
    @{contractToPoolMappings=System.Object[]; protocols=System.Object[]}
    ```
  * **遇到的问题：** 成功返回了 `data` 块（无 `errors`），但数据显示为 `System.Object[]`，看似是空的。
  * **原因分析：** 这**是**成功的标志。`Invoke-RestMethod` 默认只显示 PowerShell 对象的顶层键和类型（`System.Object[]` 即“数组”），而不显示嵌套的 JSON 内容。
  * **解决方案（验证数据）：** 使用 `| ConvertTo-Json -Depth 99` 管道命令，强制 PowerShell 将完整的、深度嵌套的 JSON 响应打印到屏幕上。
  * **最终验证命令：**
    ```powershell
    Invoke-RestMethod -Uri http://localhost:8000/graphql -Method Post -ContentType 'application/json' -Body '{"query": "{ protocols(first: 5) { id pools { id } } contractToPoolMappings(first: 5) { id pool { id } } }"}' | ConvertTo-Json -Depth 99
    ```
  * **结果：** 终端成功打印出包含所有 `id` 和 `pool` 数据的完整 JSON 结构。**部署与调试完成。**