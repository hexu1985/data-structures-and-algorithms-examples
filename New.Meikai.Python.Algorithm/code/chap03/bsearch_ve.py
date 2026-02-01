# 二分查找（查找失败时抛出ValueError异常）

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """从序列a中二分查找与key相等的元素"""
    pl = 0              # 查找范围的起始下标
    pr = len(a) - 1     # 　 〃 　结束下标

    while True:
        pc = (pl + pr) // 2     # 中间下标
        if a[pc] == key:
            return pc           # 查找成功
        elif a[pc] < key:
            pl = pc + 1         # 将查找范围缩小到右侧区域
        else:
            pr = pc - 1         # 将查找范围缩小到左侧区域
        if pl > pr:
            break
    raise ValueError    # 查找失败

if __name__ == '__main__':
    num = int(input('元素个数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    print('请按照升序输入数据。')

    x[0] = int(input('x[0]：'))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]：'))
            if x[i] >= x[i - 1]:
                 break

    ky = int(input('目标值：')) # 读取关键字ky

    try:
        idx = bin_search(x, ky)     # 在x中查找与ky相等的元素
    except ValueError:
        print('不存在与该值相等的元素。')
    else:
        print(f'元素下标为x[{idx}]。')
