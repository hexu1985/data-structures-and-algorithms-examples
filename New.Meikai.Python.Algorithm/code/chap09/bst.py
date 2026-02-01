# ２分探索木

from __future__ import annotations
from typing import Any, Type

class Node:
    """二叉查找树的节点"""
    def __init__(self, key: Any, value: Any, left: Node = None,
                 right: Node = None):
        """构造函数"""
        self.key   = key    # 键
        self.value = value  # 值
        self.left  = left   # 左指针（指向左子节点的引用）
        self.right = right  # 右指针（指向右子节点的引用）

class BinarySearchTree:
    """二叉查找树"""

    def __init__(self):
        """初始化"""
        self.root = None    # 根节点

    def search(self, key: Any) -> Any:
        """查找关键字为key的节点"""
        p = self.root           # 关注根节点
        while True:
            if p is None:       # 如果无法继续前进
                return None     # …查找失败
            if key == p.key:    # 如果key与节点p的关键字相等
                return p.value  # …查找成功
            elif key < p.key:   # 如果key较小
                p = p.left      # …查找左子树
            else:               # 如果Key较大
                p = p.right     # …查找右子树


    def add(self, key: Any, value: Any) -> bool:
        """插入关键字为key、值为value的节点"""

        def add_node(node: Node, key: Any, value: Any) -> None:
            """向以node为根的子树中插入关键字为key、值为value的节点"""
            if key == node.key:
                return False            # 二叉查找树中已经存在关键字为key的节点
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        """删除关键字为key的节点"""
        p = self.root           # 当前遍历的节点
        parent = None           # 当前遍历节点的父节点
        is_left_child = True    # p是parent的左子节点吗？

        while True:
            if p is None:       # 如果无法继续前进
                return False    # …该关键字不存在

            if key == p.key:    # 如果key与节点p的关键字相等
                break           # …查找成功
            else:
                parent = p                  # 遍历分支前，首先设定父节点
                if key < p.key:             # 如果key较小
                    is_left_child = True    # …下一步遍历左子节点
                    p = p.left              # …查找左子树
                else:                       # 如果Key较大
                    is_left_child = False   # …下一步遍历右子节点
                    p = p.right             # …查找右子树

        if p.left is None:                  # p没有左子节点…
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left  = p.right      # 将父节点的左指针指向右子节点
            else:
                parent.right = p.right      # 将父节点的右指针指向右子节点
        elif p.right is None:               # p没有右子节点…
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left  = p.left       # 将父节点的左指针指向左子节点
            else:
                parent.right = p.left       # 将父节点的右指针指向右子节点
        else:
            parent = p
            left = p.left                   # 子树中最大的节点
            is_left_child = True
            while left.right is not None:   # 查找最大节点left
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key                # 将left的关键字移动到p
            p.value = left.value            # 将left的数据移动到p
            if is_left_child:
                parent.left  = left.left    # 删除left
            else:
                parent.right = left.left    # 删除left
        return True

    def dump(self) -> None:
        """转储（按关键字升序显示所有节点）"""

        def print_subtree(node: Node):
            """按关键字升序显示以node为根的子树中的节点"""
            if node is not None:
                print_subtree(node.left)            # 按升序显示左子树
                print(f'{node.key}  {node.value}')  # 显示node
                print_subtree(node.right)           # 按升序显示右子树

        print_subtree(self.root)

    def min_key(self) -> Any:
        """最小关键字"""
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        """最大关键字"""
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
