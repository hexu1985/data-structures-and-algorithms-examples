# 求非负整数的阶乘（如果n为负数，则抛出ValueError异常）

def factorial(n: int) -> int:
    """求非负整数的阶乘（如果n为负数，则抛出ValueError异常）"""
    if n > 0:
        return n * factorial(n - 1)
    elif n == 0:
        return 1
    else:
        raise ValueError

if __name__ == '__main__':
    n = int(input('几的阶乘？：'))
    try:
        print(f'{n}的阶乘为{factorial(n)}。')
    except ValueError:
        print(f'{n}没有阶乘。')
