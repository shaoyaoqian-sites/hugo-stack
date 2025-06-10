import os
import re

# 指定要处理的文件夹路径
folder_path = '.'

# 递归遍历文件夹中的所有 .md 文件
for root, _, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith('.md'):
            file_path = os.path.join(root, filename)
            # print(file_path)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 替换图片链接
            # 会重复替换，需要修改正则表达式
            updated_content = re.sub(
                r'https://githubimages\.pengfeima\.cn/images/(.*?)(\.png|\.jpg|\.jpeg|\.JPG)',
                r'https://githubimages.pengfeima.cn/images/compressed/\1.webp',
                content
            )
            print(updated_content)

            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

print("替换完成！")