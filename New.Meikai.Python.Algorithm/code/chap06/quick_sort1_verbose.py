# 快速排序（数组的分组过程可视化）

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """对a[left] ～ a[right]进行快速排序（数组的分组过程可视化）"""
    pl = left                   # 左游标
    pr = right                  # 右游标
    x = a[(left + right) // 2]  # 枢轴（中间元素）

    print(f'a[{left}]～a[{right}]：', *a[left : right + 1])

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:  qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """快速排序"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('快速排序（数组的分组过程可视化）')
    num = int(input('元素个数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    quick_sort(x)       # 对数组x进行快速排序

    print('已按升序排序。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
