# 从1循环执行到12，不过要跳过8（其二）

for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')
print()
