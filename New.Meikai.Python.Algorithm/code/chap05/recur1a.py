# 真正递归函数（消除尾递归）

def recur(n: int) -> int:
    """消除尾递归后的recur函数"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2

x = int(input('请输入一个整数：'))

recur(x)
