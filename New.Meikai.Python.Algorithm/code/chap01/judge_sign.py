# 显示所读取的整数是正数、负数还是0

n = int(input('整数：'))

if n > 0:
    print('其值为正。')
elif n < 0:
    print('其值为负。')
else:
    print('其值为零。')
