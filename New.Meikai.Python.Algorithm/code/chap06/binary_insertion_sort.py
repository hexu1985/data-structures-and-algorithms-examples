# 二分插入排序

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    """二分插入排序"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0 # 查找范围内第一个元素的下标
        pr = i - 1 # 查找范围内最后一个元素的下标

        while True:
            pc = (pl + pr) // 2     # 查找范围内中间元素的下标
            if a[pc] == key:        # 查找成功
               break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        # 应插入位置的下标
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

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
