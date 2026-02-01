# 线性查找（哨兵法）

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """从序列seq中线性查找与key相等的元素（哨兵法）"""
    a = copy.deepcopy(seq)  # 复制seq
    a.append(key)           # 设置哨兵

    i = 0
    while True:
        if a[i] == key:
           break        # 查找成功
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('元素个数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    ky = int(input('目标值：')) # 读取关键字ky

    idx = seq_search(x, ky)     # 在x中查找与ky相等的元素

    if idx == -1:
        print('不存在与该值相等的元素。')
    else:
        print(f'元素下标为x[{idx}]。')
