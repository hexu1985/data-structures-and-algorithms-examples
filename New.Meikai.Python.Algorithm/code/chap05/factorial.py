# 求非负整数的阶乘

def factorial(n: int) -> int:
    """以递归的方式求非负整数n的阶乘"""
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('几的阶乘？：'))
    print(f'{n}的阶乘为{factorial(n)}。')
