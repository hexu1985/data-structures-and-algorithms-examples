# 数组分组

from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    """对数组分组并显示"""
    n = len(a)
    pl = 0          # 左游标
    pr = n - 1      # 右游标
    x = a[n // 2]   # 枢轴（中间元素）

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'枢轴的值为{x}。')

    print('小于等于枢轴的组')
    print(*a[0 : pl])                       # a[0] ～ a[pl - 1]

    if pl > pr + 1:
        print('等于枢轴的组')
        print(*a[pr + 1 : pl])              # a[pr + 1] ～ a[pl - 1]

    print('大于等于枢轴的组')
    print(*a[pr + 1 : n])                   # a[pr + 1] ～ a[n - 1]

if __name__ == '__main__':
    print('对数组进行分组。')
    num = int(input('元素个数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    partition(x)        # 对数组x分组并显示
