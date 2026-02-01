# 计数排序

from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    """计数排序（数组元素的值大于等于0，小于等于max）"""
    n = len(a)
    f = [0] * (max + 1)     # 累积频数
    b = [0] * n             # 临时数组

    for i in range(n):             f[a[i]] += 1                     # [Step 1]
    for i in range(1, max + 1):    f[i] += f[i - 1]                 # [Step 2]
    for i in range(n - 1, -1, -1): f[a[i]] -= 1; b[f[a[i]]] = a[i]  # [Step 3]
    for i in range(n):             a[i] = b[i]                      # [Step 4]

def counting_sort(a: MutableSequence) -> None:
    """计数排序"""
    fsort(a, max(a))

if __name__ == '__main__':
    print('计数排序')
    num = int(input('元素个数：'))
    x = [None] * num      # 创建一个元素个数为num的数组

    for i in range(num):
        while True:
            x[i] = int(input(f'x[{i}]：'))
            if x[i] >= 0: break

    counting_sort(x)     # 对数组x进行计数排序

    print('已按升序排序。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
