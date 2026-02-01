# 直接交换排序（显示排序过程）

from typing import MutableSequence

def bubble_sort_verbose(a: MutableSequence) -> None:
    """直接交换排序（显示排序过程）"""
    ccnt = 0    # 比较次数
    scnt = 0    # 交换次数
    n = len(a)
    for i in range(n - 1):
        print(f'第{i + 1}趟排序')
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'比较次数为{ccnt}。')
    print(f'交换次数为{scnt}。')

if __name__ == '__main__':
    print('直接交换排序（冒泡排序）')
    num = int(input('元素个数：'))
    x = [None] * num       # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    bubble_sort_verbose(x)  # 对数组x进行直接交换排序

    print('已按升序排序。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
