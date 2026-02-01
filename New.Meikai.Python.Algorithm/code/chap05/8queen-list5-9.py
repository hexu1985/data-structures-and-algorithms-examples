# 八皇后问题

pos = [0] * 8           # 每列的皇后位置
flag_a = [False] * 8    # 是否每列(or每行？）都已摆放皇后？
flag_b = [False] * 15   # 正斜线“／”方向上是否都已摆放皇后？
flag_c = [False] * 15   # 反斜线“＼”方向上是否都已摆放皇后？

def put() -> None:
    """输出盘面（每列的皇后位置）"""
    for i in range(8):
        print(f'{pos[i]:2}', end=' ')
    print()

def set(i: int) -> None:
    """在第i列的适当位置摆放皇后"""
    for j in range(8):
        if (    not flag_a[j]           # 第j行还未摆放皇后
            and not flag_b[i + j]       # 正斜线“／”方向上还未摆放皇后
            and not flag_c[i - j + 7]): # 反斜线“＼”方向上还未摆放皇后
            pos[i] = j          # 在第j行摆放皇后
            if i == 7:          # 所有列摆放完成
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)      # 在下一列摆放皇后
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)          # 在第0列摆放皇后
