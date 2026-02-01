# 使用辗转相除法求最大公约数

def gcd(x: int, y: int) -> int:
    """求整数x和y的最大公约数并返回"""
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('求两个整数的最大公约数。')
    x = int(input('整数：'))
    y = int(input('整数：'))

    print(f'最大公约数为{gcd(x, y)}。')
