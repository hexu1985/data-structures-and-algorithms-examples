# 归并排序

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    """归并排序"""

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """对a[left] ～ a[right]递归地进行归并排序"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)        # 对前半部分进行归并排序
            _merge_sort(a, center + 1, right)   # 对后半部分进行归并排序

            p = j = 0
            i = k = left

            while i <= center:
                 buff[p] = a[i]
                 p += 1
                 i += 1

            while i <= right and j < p:
                 if buff[j] <= a[i]:
                     a[k] = buff[j]
                     j += 1
                 else:
                     a[k] = a[i]
                     i += 1
                 k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n           # 创建临时数组
    _merge_sort(a, 0, n - 1)    # 对整个数组进行归并排序
    del buff                    # 释放临时数组

if __name__ == '__main__':
    print('归并排序')
    num = int(input('元素个数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    merge_sort(x)       # 对数组x进行归并排序

    print('已按升序排序。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
