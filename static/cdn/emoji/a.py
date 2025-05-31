    
# 进入blobcat文件夹，读取所有文件名，生成下面这样的格式的json数据
    
# {
#     "name": "blobcat",
#     "type": "image",
#     "items": [
#         { "key": "blobcat", "val": "/lujing/a.png" },
#         { "key": "blobcat2", "val": "/lujing/a2.png" },
#         { "key": "blobcat3", "val": "/lujing/a3.png" }
#     ]
# },


import os,json
def generate_blobcat_json(folder_path, base_url="https://www.pengfeima.cn/cdn/emoji/blobcat/"):
    # 获取文件夹中所有文件的列表
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # 构建items列表
    items = []
    for i, filename in enumerate(files, 1):
        # 提取文件名不带扩展名
        name_without_ext = os.path.splitext(filename)[0]
        # 构建key和val
        key = f"blobcat{i}" if i > 1 else "blobcat"
        val = f"{base_url}{filename}"
        items.append({"key": key, "val": val})
    
    # 构建完整JSON结构
    result = {
        "name": "blobcat",
        "type": "image",
        "items": items
    }
    
    return result

# 使用示例
folder_path = "blobcat"  # 替换为你的实际文件夹路径
json_data = generate_blobcat_json(folder_path)

# 打印JSON结果
# print(json.dumps(json_data, indent=4))

# 如果需要保存到文件
with open('blobcat_data.json', 'w') as f:
    json.dump(json_data, f, indent=4)