# 递归列举每行每列摆放一个皇后的摆法

pos = [0] * 8        # 每列的皇后位置
flag = [False] * 8   # 是否每行都已摆放皇后？

def put() -> None:
    """输出盘面（每列的皇后位置）"""
    for i in range(8):
        print(f'{pos[i]:2}', end=' ')
    print()

def set(i: int) -> None:
    """在第i列的适当位置摆放皇后"""
    for j in range(8):
        if not flag[j]:     # 第j行还未摆放皇后
            pos[i] = j          # 在第j行摆放皇后
            if i == 7:          # 所有列摆放完成
                put()
            else:
                flag[j] = True
                set(i + 1)      # 在下一列摆放皇后
                flag[j] = False

set(0)          # 在第0列摆放皇后
