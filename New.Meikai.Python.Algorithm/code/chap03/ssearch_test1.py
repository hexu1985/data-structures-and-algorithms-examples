# 调用seq_search函数进行线性查找的示例（其一）

from ssearch_while import seq_search

print('查找实数。')
print('备注：输入"End"结束输入。')

number = 0
x = []                  # 空列表

while True:
    s = input(f'x[{number}]：')
    if s == 'End':
        break
    x.append(float(s))  # 添加到末尾
    number += 1

ky = float(input('目标值：'))   # 读取关键字ky

idx = seq_search(x, ky)         # 在x中查找与ky相等的元素
if idx == -1:
    print('不存在与该值相等的元素。')
else:
    print(f'元素下标为x[{idx}]。')
