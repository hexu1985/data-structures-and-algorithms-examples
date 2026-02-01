# 反转可变序列中元素的顺序（不使用变量n）

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """反转可变序列a中元素的顺序"""
    for i in range(len(a) // 2):
         a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]

if __name__ == '__main__':
    print('反转数组中元素的顺序。')
    nx = int(input('元素个数：'))
    x = [None] * nx    # 创建一个包含nx个元素的列表

    for i in range(nx):
        x[i] = int(input(f'x[{i}]：'))

    reverse_array(x)   # 反转x中元素的顺序

    print('已反转数组中元素的顺序。')
    for i in range(nx):
        print(f'x[{i}]＝{x[i]}')
