# 线性查找（for语句：查找失败时抛出ValueError异常）

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """从序列a中线性查找与key相等的元素（for语句）"""
    for i in range(len(a)):
        if a[i] == key:
            return i    # 查找成功（返回下标）
    raise ValueError    # 查找失败

if __name__ == '__main__':
    num = int(input('元素个数：'))
    x = [None] * num    # 创建一个元素个数为num的数组

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    ky = int(input('目标值：')) # 读取关键字ky

    try:
        idx = seq_search(x, ky)     # 在x中查找与ky相等的元素
    except ValueError:
        print('不存在与该值相等的元素。')
    else:
        print(f'元素下标为x[{idx}]。')
