# 求1和n之间所有整数之和（while语句）

print('求1和n之间所有整数之和。')
n = int(input('n的值：'))

sum = 0
i = 1

while i <= n:   # 如果i小于等于n，则重复执行
    sum += i    # 给sum加1
    i += 1      # 给i加1
print(f'1和{n}之间所有整数之和为{sum}。')
print(f'i的值为{i}。')

