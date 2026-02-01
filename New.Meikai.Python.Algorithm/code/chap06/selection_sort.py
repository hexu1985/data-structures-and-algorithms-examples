# 直接选择排序

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    """直接选择排序"""
    n = len(a)
    for i in range(n - 1):
        min = i                         # 无序区的最小元素的下标
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]     # 将无序区的第1个元素和最小元素进行交换

if __name__ == '__main__':
    print('直接选择排序')
    num = int(input('要素数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    selection_sort(x)   # 对数组x进行直接选择排序

    print('已按升序排序。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
