# 调用seq_search函数进行线性查找的示例（其二）

from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}中的元素5.6的下标为{seq_search(t, 5.6)}。')
print(f'{s}中的元素"n"的下标为{seq_search(s, "n")}。')
print(f'{a}中的元素"DTS"的下标为{{seq_search(a, "DTS")}。')
