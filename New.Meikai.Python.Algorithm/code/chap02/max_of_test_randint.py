# 求数组中元素的最大值并输出（使用随机数给数组元素赋值）

import random
from max import max_of

print('求随机数的最大值。')
num = int(input('随机数的个数：'))
lo = int(input('随机数下限：'))
hi = int(input('随机数上限：'))
x = [None] * num  # 创建一个包含num个元素的列表

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'最大值为{max_of(x)}。')
