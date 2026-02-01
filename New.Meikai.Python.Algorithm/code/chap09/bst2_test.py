# 二叉查找树类BinarySearchTree的使用示例（其二）

from enum import Enum
from bst2 import BinarySearchTree

Menu = Enum('Menu', ['插入', '删除', '查找', '升序转储', '降序转储', '关键字范围', '结束'])

def select_Menu() -> Menu:
    """菜单选择"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()                        # 创建二叉查找树

while True:
    menu = select_Menu()                         # 菜单选择

    if menu == Menu.插入:                        # 插入
        key = int(input('关键字：'))
        val = input('值：')
        if not tree.add(key, val):
            print('插入失败！')

    elif menu == Menu.删除:                      # 删除
        key = int(input('关键字：'))
        tree.remove(key)

    elif menu == Menu.查找:                      # 查找
        key = int(input('关键字：'))
        t = tree.search(key)
        if t is not None:
            print(f'该关键字的值为{t}。')
        else:
            print('没有符合条件的数据。')

    elif menu == Menu.升序转储:                # 升序转储
        tree.dump()

    elif menu == Menu.降序转储:                # 降序转储
        tree.dump(reverse = True)

    elif menu == Menu.关键字范围:                  # 关键字范围（最大值和最小值）
        print(f'最小关键字＝{tree.min_key()}')
        print(f'最大关键字＝{tree.max_key()}')

    else:                                        # 结束
        break
