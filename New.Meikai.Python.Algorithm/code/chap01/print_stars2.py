# 输出n个*，并在每输出w个后换行（其二）

print('输出*。')
n = int(input('符号总数：'))
w = int(input('每隔多少个换行：'))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)
