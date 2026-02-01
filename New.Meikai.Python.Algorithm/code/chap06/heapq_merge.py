# 有序数组的归并（使用heap.merege）

import heapq

a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(heapq.merge(a, b))              # 将数组a和b归并后存入c

print('已将数组a和b归并并存入数组c。')
print(f'数组a：{a}')
print(f'数组b：{b}')
print(f'数组c：{c}')
