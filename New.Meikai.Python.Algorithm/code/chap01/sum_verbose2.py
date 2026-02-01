# 求a和b之间所有整数之和（显示求和过程中的式子：其二）

print('求a和b之间所有整数之和。')
a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i        # 给sum加i

print(f'{b} = ', end='')
sum += b            # 给sum加b

print(sum)
