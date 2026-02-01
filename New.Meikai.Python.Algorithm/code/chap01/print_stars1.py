# 输出n个*，并在每输出w个后换行（其一）

print('输出*。')
n = int(input('符号总数：'))
w = int(input('每隔多少个换行：'))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()        # 改行

if n % w:
    print()            # 改行
t
