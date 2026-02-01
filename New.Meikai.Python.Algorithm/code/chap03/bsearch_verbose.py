# 二分查找（显示中间过程）

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """从序列a中二分查找与key相等的元素（显示中间过程）"""
    pl = 0              # 查找范围的起始下标
    pr = len(a) - 1     # 　 〃 　结束下标

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i:4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2     # 中间下标

        print('   |', end='')
        if pl != pc:
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
        else:
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:
            print(((pr - pc) * 4 - 2) * ' ' + '->')
        else:
            print('->')
        print(f'{pc:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')
        print('\n   |')

        if a[pc] == key:
            return pc           # 查找成功
        elif a[pc] < key:
            pl = pc + 1         # 将查找范围缩小到右侧区域
        else:
            pr = pc - 1         # 将查找范围缩小到左侧区域
        if pl > pr:
            break
    return -1                   # 查找失败

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

    idx = bin_search(x, ky)     # 在x中查找与ky相等的元素

    if idx == -1:
        print('不存在与该值相等的元素。')
    else:
        print(f'元素下标为x[{idx}]。')
