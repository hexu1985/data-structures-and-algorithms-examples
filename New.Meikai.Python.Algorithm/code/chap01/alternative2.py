# 交替显示+和-（其二）

print('交替显示+和-。')
n = int(input('符号总数：'))

for _ in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')
print()
