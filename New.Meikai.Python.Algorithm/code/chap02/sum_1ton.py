# 用于求1和n之间所有整数之和的程序

def sum_1ton(n):
    """求1和n之间所有整数之和"""
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('x的值：'))
print(f'1和{x}之间所有整数之和为{sum_1ton(x)}。')
