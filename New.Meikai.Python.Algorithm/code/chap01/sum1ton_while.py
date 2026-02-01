# 求1和n之间所有整数之和（while语句）

print('求1和n之间所有整数之和。')
n = int(input('n的值：'))

sum = 0
i = 1

while i <= n:   # iがn以下のあいだ繰り返す
    sum += i    # 给sum加i
    i += 1      # 给i加1
print(f'1和{n}之间所有整数之和为{sum}。')
