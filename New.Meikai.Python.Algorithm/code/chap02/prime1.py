# 枚举1000以内的质数（第1版）

counter = 0         # 除法运算的次数

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0:  # 如果能整除，则不是质数
            break       # 不需要继续循环
    else:           # 直到最后都无法整除
        print(n)
print(f'执行除法运算的次数：{counter}')
