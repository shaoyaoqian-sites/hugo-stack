import http.client

# 创建与服务器的连接
conn = http.client.HTTPConnection("localhost:5232")

# 定义 token 和 headers
token = "eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoibWFwZW5nZmVpIiwiaXNzIjoibWVtb3MiLCJzdWIiOiIxIiwiYXVkIjpbInVzZXIuYWNjZXNzLXRva2VuIl0sImlhdCI6MTcyNzMxOTI3MX0.agv_uKgNKU8v6PC4q5Lsxn1XPtoW3wrOLZuD3INOF-o"
# eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiIiwiaXNzIjoibWVtb3MiLCJzdWIiOiI1IiwiYXVkIjpbInVzZXIuYWNjZXNzLXRva2VuIl0sImV4cCI6NDg4MDY3MjY1NiwiaWF0IjoxNzI3MDcyNjU2fQ.EGa5pxbKXNyoceHNdmejWVs6YoK-pAOO49967sk5Kic"  # 替换为你的实际 token
headers = {
    "Authorization": f"Bearer {token}",  # 添加 Authorization 头
}

# /api/v1/{name}
# https://memos.xaox.cc/api/v1/memo?creator=mapfi&limit=10
# https://memos.xaox.cc/api/v1/memo?creatorId=1&limit=10
# 发送请求时加入 headers
# http://localhost:5232/api/v1/mapengfei
# https://memos.thatcoder.cn/api/v1/users/1
conn.request("GET", "/api/v1/users/1", headers=headers)
# conn.request("GET", "/api/v1/memo?limit=10", headers=headers)

# 获取响应
res = conn.getresponse()
data = res.read()

# 将响应数据写入文件
with open("a.html", "w") as f:
    print(data.decode("utf-8"), file=f)
