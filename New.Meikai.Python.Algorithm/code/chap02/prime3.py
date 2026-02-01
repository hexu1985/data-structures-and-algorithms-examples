# 枚举1000以内的质数（第3版）

counter = 0             # 乘法运算和除法运算的次数
ptr = 0                 # 得到的质数的个数
prime = [None] * 500    # 存储质数的数组

prime[ptr] = 2          # 2是质数
ptr += 1
prime[ptr] = 3          # 3是质数
ptr += 1

for n in range(5, 1001, 2):       # 只针对奇数
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:     # 如果能整除，则不是质数
            break                 # 不需要继续循环
        i += 1
    else:                         # 直到最后都无法整除
        prime[ptr] = n            # 则作为质数存储到数组中
        ptr += 1
        counter += 1

for i in range(ptr):              # 输出得到的ptr个质数
    print(prime[i])
print(f'执行乘法运算和除法运算的次数：{counter}')
