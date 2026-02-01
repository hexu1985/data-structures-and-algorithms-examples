# 读取3个整数，计算并输出中值

def med3(a, b, c):
    """计算a、b、c的中值并返回（其他解）"""
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

print('计算3个整数的中值。')
a = int(input('整数a的值：'))
b = int(input('整数b的值：'))
c = int(input('整数c的值：'))

print(f'中值为{med3(a, b, c)}。')
