# 读取3个整数，计算并输出中值

def med3(a, b, c):
    """计算a、b、c的中值并返回"""
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('计算3个整数的中值。')
a = int(input('整数a的值：'))
b = int(input('整数b的值：'))
c = int(input('整数c的值：'))

print(f'中值为{med3(a, b, c)}。')
