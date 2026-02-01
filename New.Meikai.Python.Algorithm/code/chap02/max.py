# 输出序列中元素的最大值

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """返回序列a中元素的最大值"""
    maximum = a[0]
    for i in range(1, len(a)):
         if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('求数组的最大值。')
    num = int(input('元素个数：'))
    x = [None] * num  # 创建包含num个元素的列表

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    print(f'最大值为{max_of(x)}。')
