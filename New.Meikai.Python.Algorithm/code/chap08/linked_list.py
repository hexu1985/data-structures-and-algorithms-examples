# 单链表

from __future__ import annotations
from typing import Any, Type

class Node:
    """单链表中的节点类"""

    def __init__(self, data: Any = None, next: Node = None):
        """初始化"""
        self.data = data    # 数据
        self.next = next    # 后继指针

class LinkedList:
    """单链表类"""

    def __init__(self) -> None:
        """初始化"""
        self.no = 0           # 节点个数
        self.head = None      # 头节点
        self.current = None   # 当前节点

    def __len__(self) -> int:
        """返回单链表中的节点个数"""
        return self.no

    def search(self, data: Any) -> int:
        """查找与data相等的节点"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        """单链表中是否包含data？"""
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        """在头部插入节点"""
        ptr = self.head                     # 插入前的头节点
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any):
        """向单链表尾部插入节点"""
        if self.head is None:               # 如果单链表为空
            self.add_first(data)            # 插入头部
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1

    def remove_first(self) -> None:
        """删除头节点"""
        if self.head is not None:           # 如果单链表不为空
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self):
        """删除尾节点"""
        if self.head is not None:
            if self.head.next is None:      # 如果只有一个节点
                self.remove_first()         # 删除头节点
            else:
                ptr = self.head             # 当前遍历节点
                pre = self.head             # 当前遍历节点的前驱节点

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None             # pre指向删除后的尾节点
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        """删除节点p"""
        if self.head is not None:
            if p is self.head:              # 如果p为头节点
                self.remove_first()         # 删除头节点
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return              # 如果单链表中不包含ptr
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """删除当前节点"""
        self.remove(self.current)

    def clear(self) -> None:
        """删除所有节点"""
        while self.head is not None:        # 直到单链表为空
            self.remove_first()             # 删除头节点
        self.current = None
        self.no = 0

    def next(self) -> bool:
        """将当前节点向后移动一位"""
        if self.current is None or self.current.next is None:
            return False                    # 无法继续向后移动
        self.current = self.current.next
        return True

    def print_current_node(self) -> None:
        """显示当前节点"""
        if self.current is None:
            print('当前节点不存在。')
        else:
            print(self.current.data)

    def print(self) -> None:
        """显示所有节点"""
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self) -> LinkedListIterator:
        """返回迭代器"""
        return LinkedListIterator(self.head)

class LinkedListIterator:
    """LinkedList类的迭代器类"""

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
