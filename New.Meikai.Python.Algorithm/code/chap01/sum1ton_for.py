# 求1和n之间所有整数之和（for语句）

print('求1和n之间所有整数之和。')
n = int(input('n的值：'))

sum = 0
for i in range(1, n + 1):
    sum += i   # 给sum加i

print(f'1和{n}之间所有整数之和为{sum}。')
