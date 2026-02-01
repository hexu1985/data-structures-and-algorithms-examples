# 求1和n之间所有整数之和（高斯方法）

print('求1和n之间所有整数之和。')
n = int(input('n的值：'))

sum = n * (n + 1) // 2

print(f'1和{n}之间所有整数之和为{sum}。')
