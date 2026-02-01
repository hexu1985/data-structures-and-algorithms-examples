# 递归列举每列摆放一个皇后的摆法

pos = [0] * 8   # 各每列的皇后位置

def put() -> None:
    """输出盘面（每列的皇后位置）"""
    for i in range(8):
        print(f'{pos[i]:2}', end=' ')
    print()

def set(i: int) -> None:
    """在第i列摆放皇后"""
    for j in range(8):
        pos[i] = j          # 在第j行摆放皇后
        if i == 7:          # 所有列摆放完成
            put()
        else:
            set(i + 1)      # 在下一列摆放皇后

set(0)          # 在第0列摆放皇后
