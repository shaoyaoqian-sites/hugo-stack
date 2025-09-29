import json

def json_to_timeline():
    # 读取 JSON 文件
    # 读取两个 JSON 文件
    with open('timeline.json', 'r', encoding='utf-8') as f1:
    # , \
        #  open('holiday_scotland.json', 'r', encoding='utf-8') as f2, \
        #  open('glasgow.json', 'r', encoding='utf-8') as f3:
        items1 = json.load(f1)
        # items2 = json.load(f2)
        # items3 = json.load(f3)

    # 合并并以 title 和 start 去重
    all_items = items1
    # + items2 + items3
    unique_items = {}
    for item in all_items:
        title = item.get('title', '')
        start = item.get('start', '')
        key = (title, start)
        if key not in unique_items:
            unique_items[key] = item

    # 按 start 排序
    items = sorted(unique_items.values(), key=lambda x: x.get('start', ''))


    # 生成 timelineitem 块
    lines = []
    lines.append('{{< timeline >}}')

    for item in items:
        title = item.get('title', '')
        start = item.get('start', '')
        end = item.get('end', '')
        href = item.get('href', '')
        note = item.get('note', '')
        target = item.get('target', '_self')

        # 构造 timelineitem shortcode
        block = '  {{< timelineitem\n'
        block += f'      title="{title}"\n'
        block += f'      start="{start}"\n'
        if end:
            block += f'      end="{end}"\n'
        block += f'      href="{href}"\n'
        block += f'      note="{note}"\n'
        block += f'      target="{target}"\n'
        block += '  >}}'
        lines.append(block)

    lines.append('{{< /timeline >}}')
    return lines



# 示例用法
if __name__ == "__main__":
    print("Generating timeline...")
    a = json_to_timeline()
    
    # 写入输出文件
    with open("a.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(a))

    print(f"✅ Timeline 已生成到: a.txt")