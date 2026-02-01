# 直接交换排序（第3版：限制遍历范围）

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """直接交换排序（第3版：限制遍历范围）"""
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last

if __name__ == '__main__':
    print('直接交换排序（冒泡排序）')
    num = int(input('元素个数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    bubble_sort(x)      # 对数组x进行直接交换排序

    print('已按升序排序。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
