# 真正递归函数

def recur(n: int) -> int:
    """真正递归函数recur"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('请输入一个整数：'))

recur(x)
