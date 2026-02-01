# 归并排序（使用heapq.merge）

from typing import MutableSequence
import heapq

def merge_sort(a: MutableSequence) -> None:
    """归并排序"""
    atype = type(a)

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """对a[left] ～ a[right]递归地进行归并排序"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)        # 对前半部分进行归并排序
            _merge_sort(a, center + 1, right)   # 对后半部分进行归并排序

            buff = atype(heapq.merge(a[left: center+1], a[center + 1: right+1]))
            for i in range(len(buff)):
                a[left + i] = buff[i]

    _merge_sort(a, 0, len(a))     # 对整个数组进行归并排序

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
