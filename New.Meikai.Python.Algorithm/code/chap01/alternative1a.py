# 交替显示+和-（其一：for语句的起始值变为1）

print('交替显示+和-。')
n = int(input('符号总数：'))

for i in range(1, n + 1):
    if i % 2:               # 奇数
        print('+', end='')
    else:                   # 偶数
        print('-', end='')
print()
