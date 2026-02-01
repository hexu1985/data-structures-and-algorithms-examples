# 真正递归函数（消除递归）

from stack import Stack

def recur(n: int) -> int:
    """消除递归后的recur函数"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)               # 让n值入栈
            n = n - 1
            continue
        if not s.is_empty():        # 如果栈不为空
            n = s.pop()             # 则让保存的值出栈，然后将其传递给n
            print(n)
            n = n - 2
            continue
        break
x = int(input('请输入一个整数：'))

recur(x)
