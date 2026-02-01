# 输入3个整数，计算并显示最大值

print('求3个整数中的最大值。')
a = int(input('整数a的值：'))
b = int(input('整数b的值：'))
c = int(input('整数c的值：'))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'最大值为{maximum}。')
