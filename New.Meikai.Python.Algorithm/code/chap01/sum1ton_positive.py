# 求1和n之间所有整数之和（输入的n是正数）

print('求1和n之间所有整数之和。')

while True:
    n = int(input('n的值：'))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i   # 给sum加i
    i += 1     # 给i加1
print(f'1和{n}之间所有整数之和为{sum}。')
