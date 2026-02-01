# 从1循环执行到12，不过要跳过8（其一）

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
print()
