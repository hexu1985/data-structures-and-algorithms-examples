# 交替显示+和-（其一）

print('交替显示+和-。')
n = int(input('符号总数：'))

for i in range(n):
    if i % 2:               # 奇数
        print('-', end='')
    else:                   # 偶数
        print('+', end='')
print()
