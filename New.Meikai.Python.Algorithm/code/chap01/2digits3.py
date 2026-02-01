# 读取两位数的正整数（10～99）（其三）

print('请输入一个两位数的正整数。')

while True:
    no = int(input('值为：'))
    if not(no < 10 or no > 99):
        break
print(f'读取的是{no}。')
