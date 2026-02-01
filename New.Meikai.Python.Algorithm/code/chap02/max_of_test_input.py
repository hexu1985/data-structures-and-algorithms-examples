# 求数组中元素的最大值并输出（读取元素值）

from max import max_of

print('求数组的最大值。')
print('备注：收到"End"后结束输入。')

number = 0
x = []                  # 空列表

while True:
    s = input(f'x[{number}]：')
    if s == 'End':
        break
    x.append(int(s))    # 添加到末尾
    number += 1

print(f'已读取{number}个元素。')
print(f'最大值为{max_of(x)}。')
