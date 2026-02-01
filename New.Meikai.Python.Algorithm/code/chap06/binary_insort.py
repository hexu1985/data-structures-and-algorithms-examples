# 二分插入排序（利用bisect.insort）

from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """二分插入排序（利用bisect.insort）"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)

if __name__ == '__main__':
    print('二分插入排序')
    num = int(input('元素个数：'))
    x = [None] * num            # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    binary_insertion_sort(x)    # 对数组x进行二分插入排序

    print('已按升序排序。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
