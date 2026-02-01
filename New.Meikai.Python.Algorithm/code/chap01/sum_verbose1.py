# 求a和b之间所有整数之和（显示求和过程中的式子：其一）

print('求a和b之间所有整数之和。')
a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    if i < b:       # 中间
        print(f'{i} + ', end='')
    else:           # 最后
        print(f'{i} = ', end='')
    sum += i        # 给sum加i

print(sum)
