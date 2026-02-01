# 交替显示+和-（其二：for语句的起始值变为1）

print('交替显示+和-。')
n = int(input('符号总数：'))

for _ in range(1, n // 2 + 1):
    print('+-', end='')

if n % 2:
    print('+', end='')
print()
