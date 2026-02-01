# 枚举1000以内的质数（第3版的其他解：不事先确定数组prime中的元素个数）

counter = 0             # 乘法运算和除法运算的次数
prime = [2, 3]          # 存储质数的数组

for n in range(5, 1001, 2):       # 判断对象只有奇数
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:     # 如果能整除，则不是质数
            break                 # 不需要继续循环
        i += 1
    else:                         # 直到最后都无法整除
        prime += [n]              # 则作为质数存储在数组中
        counter += 1

for i in prime:                   # 输出得到的质数
    print(i)
print(f'执行乘法运算和除法运算的次数：{counter}')
