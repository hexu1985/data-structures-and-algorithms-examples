# 求数组元素的最大值并输出（元组、字符串和字符串列表）

from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}的最大值为{max_of(t)}。')
print(f'{s}的最大值为{max_of(s)}。')
print(f'{a}的最大值为{max_of(a)}。')
