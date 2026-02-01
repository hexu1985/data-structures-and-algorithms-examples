# 线性查找（while语句）

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """从序列a中线性查找与key相等的元素（while语句）"""
    i = 0

    while True:
        if i == len(a):
            return -1   # 查找失败（返回-1）
        if a[i] == key:
            return i    # 查找成功（返回下标）
        i += 1

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
