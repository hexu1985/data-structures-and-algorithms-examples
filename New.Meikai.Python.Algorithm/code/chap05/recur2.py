# 真正递归函数（反向调用）

def recur(n: int) -> int:
    """真正递归函数recur"""
    if n > 0:
        recur(n - 2)
        print(n)
        recur(n - 1)

x = int(input('请输入一个整数：'))

recur(x)
