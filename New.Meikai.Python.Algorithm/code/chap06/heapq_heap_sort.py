# 堆排序（使用heapq.push和heapq.pop）

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """堆排序（使用heapq.push和heapq.pop）"""

    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)

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
