import requests  # 用于发送 HTTP 请求
import json      # 用于处理 JSON 数据
from pathlib import Path  # 用于处理文件路径

# --- 1. 定义你的查询 ---

# 你的 FastAPI 服务器正在运行的 URL
FASTAPI_SERVER_URL = "http://localhost:8000/graphql"

# 你要发送的 GraphQL 查询语句。
# 使用三重引号 (""") 可以让你方便地编写多行字符串。
GRAPHQL_QUERY = """
query MyQuery {
  pools(first: 1) { 
    id
    liquidationCallHistory(first: 5) {
      borrowAssetPriceUSD
      collateralAmount
      collateralAssetPriceUSD
      liquidator 
      principalAmount
      user {
        id 
      }
      principalReserve {
        name 
      }
    }
  }
}
"""

# 构建要发送的 JSON 负载 (payload)
# 这等同于 PowerShell 中的 '-Body'
payload = {
    "query": GRAPHQL_QUERY
}

# --- 2. 定义输出路径 ---

# Path(__file__) 会获取当前脚本 (query.py) 的完整路径
# .parent 会获取该脚本所在的目录 (F:\...\test\query)
CURRENT_DIR = Path(__file__).parent

# 在该目录下定义你的输出文件名
OUTPUT_FILE_PATH = CURRENT_DIR / "protocols_data.json"


# --- 3. 执行主函数 ---

def main():
    print(f"正在向 {FASTAPI_SERVER_URL} 发送查询...")

    try:
        # 发送 HTTP POST 请求
        # requests.post 会自动将 Python 字典 (payload) 转换为 JSON 字符串
        # 我们设置一个超时时间（例如 10 秒）是一个好习惯
        response = requests.post(FASTAPI_SERVER_URL, json=payload, timeout=10)

        # 检查服务器是否返回了错误 (如 404, 500)
        # 如果状态码不是 2xx，这里会引发一个异常
        response.raise_for_status()

        # 将返回的 JSON 响应解析为 Python 字典
        data = response.json()

        # 检查 The Graph 是否在返回的数据中包含了 "errors"
        if "errors" in data:
            print("GraphQL 查询返回了错误：")
            print(json.dumps(data, indent=2))
        
        # 如果没有 "errors" 并且有 "data"，说明成功
        elif "data" in data:
            print("成功获取数据！")

            # 将数据写入到输出文件
            # 'w' 表示写入模式 (会覆盖旧文件)
            # encoding='utf-8' 确保正确处理所有字符
            # indent=4 使 JSON 文件格式优美、易读
            with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            print(f"数据已成功保存到: {OUTPUT_FILE_PATH}")

        else:
            print("收到了未知的响应格式：")
            print(data)

    except requests.exceptions.ConnectionError:
        print(f"错误：无法连接到 {FASTAPI_SERVER_URL}")
        print("请确保你的 FastAPI 服务器 (uvicorn) 正在运行！")
    
    except requests.exceptions.RequestException as e:
        # 捕获所有其他的 requests 错误 (如超时, HTTP 错误等)
        print(f"请求过程中发生错误: {e}")

# Python 的标准入口点
if __name__ == "__main__":
    main()