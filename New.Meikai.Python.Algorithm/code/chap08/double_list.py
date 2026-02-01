# 双向循环链表

from __future__ import annotations
from typing import Any, Type

class Node:
    """双向循环链表中的节点类"""

    def __init__(self, data: Any = None, prev: Node = None,
                       next: Node = None) -> None:
        """初始化"""
        self.data = data            # 数据
        self.prev = prev or self    # 前驱指针
        self.next = next or self    # 后继指针

class DoubleLinkedList:
    """双向循环链表类"""

    def __init__(self) -> None:
        """初始化"""
        self.head = self.current = Node()    # 创建虚拟节点
        self.no = 0

    def __len__(self) -> int:
        """返回链表中的节点个数"""
        return self.no

    def is_empty(self) -> bool:
        """链表是否为空？"""
        return self.head.next is self.head

    def search(self, data: Any) -> Any:
        """查找与data相等的节点"""
        cnt = 0
        ptr = self.head.next                # 当前遍历的节点
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt                  # 查找成功
            cnt += 1
            ptr = ptr.next                  # 移动到后继节点
        return -1                           # 查找失败

    def __contains__(self, data: Any) -> bool:
        """链表中是否包含data？"""
        return self.search(data) >= 0

    def print_current_node(self) -> None:
        """显示当前节点"""
        if self.is_empty():
            print('当前节点不存在。')
        else:
            print(self.current.data)

    def print(self) -> None:
        """显示所有节点"""
        ptr = self.head.next        # 虚拟节点的后继节点
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        """逆序显示所有节点"""
        ptr = self.head.prev        # 虚拟节点的前驱节点
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        """当前节点向后移动一位"""
        if self.is_empty() or self.current.next is self.head:
            return False        # 无法移动
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        """当前节点向前移动一位"""
        if self.is_empty() or self.current.prev is self.head:
            return False        # 无法移动
        self.current = self.current.prev
        return True

    def add(self, data: Any) -> None:
        """在当前节点之后插入节点"""
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        """向链表头部插入节点"""
        self.current = self.head        # 向虚拟节点head之后插入节点
        self.add(data)

    def add_last(self, data: Any) -> None:
        """向链表尾部插入节点"""
        self.current = self.head.prev   # 向尾节点head.prev之后插入节点
        self.add(data)

    def remove_current_node(self) -> None:
        """删除当前节点"""
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self, p: Node) -> None:
        """删除节点p"""
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:        # 找到p
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next

    def remove_first(self) -> None:
        """删除头节点"""
        self.current = self.head.next     # 删除头节点head.next
        self.remove_current_node()

    def remove_last(self) -> None:
        """删除尾节点"""
        self.current = self.head.prev     # 删除尾节点head.prev
        self.remove_current_node()

    def clear(self) -> None:
        """删除所有节点"""
        while not self.is_empty():  # 删除头节点
            self.remove_first()     # 直到链表为空
        self.no = 0

    def __iter__(self) -> DoubleLinkedListIterator:
        """返回迭代器"""
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        """返回降序迭代器"""
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    """DoubleLinkedList的迭代器类"""

    def __init__(self, head: Node):
        self.head    = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    """DoubleLinkedList的降序迭代器类"""

    def __init__(self, head: Node):
        self.head    = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data
