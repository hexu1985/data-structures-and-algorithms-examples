# 求a和b之间所有整数之和（for语句）

print('求a和b之间所有整数之和。')
a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    sum += i   # 给sum加i

print(f'{a}和{b}之间所有整数之和为{sum}。')
