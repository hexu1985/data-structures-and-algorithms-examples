# 有序数组的归并

from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """"将有序数组a和b归并后存入c"""
    pa, pb, pc = 0, 0, 0                    # 游标
    na, nb, nc = len(a), len(b), len(c)     # 元素个数

    while pa < na and pb < nb:      # 存储较小的元素
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:                  # 复制a中的剩余元素
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:                  # 复制b中的剩余元素
        c[pc] = b[pb]
        pb += 1
        pc += 1

if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    print('两个有序数组的归并')

    merge_sorted_list(a, b, c)    # 将数组a和b归并后存入c

    print('已将数组a和b归并并存入数组c。')
    print(f'数组a：{a}')
    print(f'数组b：{b}')
    print(f'数组c：{c}')
