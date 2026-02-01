# 希尔排序（第2版：h = …, 40, 13, 4, 1））

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    """希尔排序（第2版）"""
    n = len(a)
    h = 1

    while (h < n // 9):
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3

if __name__ == '__main__':
    print('希尔排序（第2版）')
    num = int(input('元素个数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    shell_sort(x)       # 对数组x进行希尔排序

    print('已按升序排序。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
