# 读取任意个数的值，元素个数为n的数组中只保存最后读取的n个元素

n = int(input('可以存储多少个整数？：'))
a = [None] * n # 用于存储读取的值的数组

cnt = 0         # 读取的元素个数
while True:
    a[cnt % n] = int(input((f'第{cnt + 1}个整数：')))
    cnt += 1

    retry = input(f'是否继续？（Y…Yes／N…No）：')
    if retry in {'N', 'n'}:
        break

i = cnt - n
if i < 0: i = 0

while i < cnt:
    print(f'第{i + 1}个＝{a[i % n]}')
    i += 1
