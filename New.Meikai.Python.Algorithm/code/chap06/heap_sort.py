# 堆排序

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """堆排序"""

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """将a[left] ～ a[right]堆化"""
        temp = a[left]      # 根节点

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     # 左子节点
            cr = cl + 1             # 右子节点
            child = cr if cr <= right and a[cr] > a[cl] else cl # 较大值
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):   # 将a[i] ～ a[n - 1]堆化
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]     # 将最大元素与无序区最后一个元素进行交换
        down_heap(a, 0, i - 1)      # 将a[0] ～ a[n - 1]堆化

if __name__ == '__main__':
    print('堆排序')
    num = int(input('元素个数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    heap_sort(x)        # 对数组x进行堆排序

    print('已按升序排序。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
