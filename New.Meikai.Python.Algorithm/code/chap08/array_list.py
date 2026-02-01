# 单链表（数组游标版）

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    """"单链表的节点类（数组游标版）"""

    def __init__(self, data = Null, next = Null, dnext = Null):
        """初始化"""
        self.data  = data   # 数据
        self.next  = next   # 单链表的后继指针
        self.dnext = dnext  # 自由列表的后继指针

class ArrayLinkedList:
    """单链表类（数组游标版）"""

    def __init__(self, capacity: int):
        """初始化"""
        self.head = Null            # 头节点
        self.current = Null         # 当前节点
        self.max = Null             # 当前使用的最后一条记录
        self.deleted = Null         # 自由列表的头节点
        self.capacity = capacity    # 单链表容量
        self.n = [Node()] * self.capacity     # 单链表主体
        self.no = 0

    def __len__(self) -> int:
        """返回单链表中的节点的个数"""
        return self.no

    def get_insert_index(self):
        """求下一条待插入记录的下标"""
        if self.deleted == Null:            # 待删除的记录不存在
            if self.max < self.capacity:
                self.max += 1
                return self.max             # 使用新记录
            else:
                return Null                 # 容量溢出
        else:
            rec = self.deleted                  # 从自由列表中
            self.deleted = self.n[rec].dnext    # 取出头节点rec
            return rec

    def delete_index(self, idx: int) -> None:
        """将记录idx添加到自由列表中"""
        if self.deleted == Null:            # 待删除的记录不存在
            self.deleted = idx              # 将idx添加到自由列表
            self.n[idx].dnext = Null        # 头部
        else:
            rec = self.deleted              # 将idx插入
            self.deleted = idx              # 自由列表头部
            self.n[rec].dnext = rec

    def search(self, data: Any) -> int:
        """查找与data相等的节点"""
        cnt = 0
        ptr = self.head                     # 当前遍历的节点
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt                  # 查找成功
            cnt += 1
            ptr = self.n[ptr].next          # 遍历后继节点
        return Null                         # 查找失败

    def __contains__(self, data: Any) -> bool:
        """单链表中是否包含data？"""
        return self.search(data) >= 0

    def add_first(self, data: Any):
        """向头部插入节点"""
        ptr = self.head                     # 插入操作前的头节点
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec  # 插入到第rec条记录
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        """向尾部插入节点"""
        if self.head == Null:               # 如果单链表为空，
            self.add_first(data)            # 则在头部插入
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()
            if rec != Null:                # 插入到第rec条记录
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        """删除头节点"""
        if self.head != Null:              # 如果单链表不为空
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        """删除尾节点"""
        if self.head != Null:
            if self.n[self.head].next == Null:  # 如果只有一个节点
                self.remove_first()             # 则删除头节点
            else:
                ptr = self.head     # 当前遍历的节点
                pre = self.head     # 当前遍历的节点的前驱节点

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null     # pre是执行删除操作后的尾节点
                self.delete_index(pre)
                self.current = pre
                self.no -= 1

    def remove(self, p: int) -> None:
        """删除记录p"""
        if self.head != Null:
            if p == self.head:          # 如果p是头节点
                self.remove_first()     # 则删除头节点
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return          # 单链表中不包含p
                self.n[ptr].next = Null
                self.delete_index(ptr)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """删除当前节点"""
        self.remove(self.current)

    def clear(self) -> None:
        """删除所有节点"""
        while self.head != Null:    # 删除头节点
            self.remove_first()     # 直到单链表为空
        self.current = Null

    def next(self) -> bool:
        """将当前节点向后移动一位"""
        if self.current == Null or self.n[self.current].next == Null:
            return False            # 不能继续移动
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) -> None:
        """显示当前节点"""
        if self.current == Null:
            print('当前节点不存在。')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        """显示所有节点"""
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        """转储数组"""
        for i in self.n:
            print(f'[{i}]  {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        """返回迭代器"""
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    """ArrayLinkedList类的迭代器类"""

    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
