# 双向循环链表类DoubleLinkedList的使用示例

from enum import Enum
from double_list import DoubleLinkedList

Menu = Enum('Menu', ['向头部插入', '向尾部插入', '向当前节点之后插入',
                     '删除头节点', '删除尾节点', '显示当前节点',
                     '当前节点向后移动', '返回当前节点', '删除当前节点',
                     '全部删除', '查找', '成员判断', '显示所有节点',
                     '逆序显示所有节点', '遍历', '反向遍历', '结束'])

def select_Menu() -> Menu:
    """菜单选择"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = DoubleLinkedList()                         # 创建双向循环键表

while True:
    menu = select_Menu()                         # 菜单选择

    if menu == Menu.向头部插入:                  # 向头部插入
        lst.add_first(int(input('值：')))

    elif menu == Menu.向尾部插入:                # 向尾部插入
        lst.add_last(int(input('值：')))

    elif menu == Menu.向当前节点之后插入:        # 向当前节点之后插入
        lst.add(int(input('值：')))

    elif menu == Menu.删除头节点:                # 删除头节点
        lst.remove_first()

    elif menu == Menu.删除尾节点:                # 删除尾节点
        lst.remove_last()

    elif menu == Menu.显示当前节点:              # 显示当前节点
        lst.print_current_node()

    elif menu == Menu.当前节点向后移动:          # 当前节点向后移动
        lst.next()

    elif menu == Menu.返回当前节点:                # 返回当前节点
        lst.prev()

    elif menu == Menu.删除当前节点:              # 删除当前节点
        lst.remove_current_node()

    elif menu == Menu.全部删除:                  # 全部删除
        lst.clear()

    elif menu == Menu.查找:                      # 查找
        pos = lst.search(int(input('值：')))
        if pos >= 0:
            print(f'等于该值的数据位于表中第{pos + 1}位。')
        else:
            print('没有符合条件的数据。')

    elif menu == Menu.成员判断:                  # 成员判断
        print('等于该值的数据'
              + ('存在。' if int(input('值：')) in lst else '不存在。'))

    elif menu == Menu.显示所有节点:              # 显示所有节点
        lst.print()

    elif menu == Menu.逆序显示所有节点:          # 逆序显示所有节点
        lst.print_reverse()

    elif menu == Menu.遍历:                      # 遍历所有节点
        for e in lst:
             print(e)

    elif menu == Menu.反向遍历:                  # 反向遍历所有节点
        for e in reversed(lst):
             print(e)

    else:                                        # 结束
        break
