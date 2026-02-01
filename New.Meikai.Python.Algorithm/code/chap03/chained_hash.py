# 通过拉链法实现散列表

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """组成散列表的节点"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """初始化"""
        self.key   = key    # 关键字
        self.value = value  # 值
        self.next  = next   # 指向后继节点

class ChainedHash:
    """通过散列表类实现拉链法"""

    def __init__(self, capacity: int) -> None:
        """初始化"""
        self.capacity = capacity                # 散列表的容量
        self.table = [None] * self.capacity     # 散列表（列表）

    def hash_value(self, key: Any) -> int:
        """求散列值"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16)
                % self.capacity)

    def search(self, key: Any) -> Any:
        """查找关键字为key的元素（返回值）"""
        hash = self.hash_value(key)     # 待查找关键字的散列值
        p = self.table[hash]            # 关注的节点

        while p is not None:
            if p.key == key:
                 return p.value         # 查找成功
            p = p.next                  # 关注后继节点

        return None                     # 查找失败

    def add(self, key: Any, value: Any) -> bool:
        """插入关键字为key、值为value的元素"""
        hash = self.hash_value(key)     # 待插入关键字的散列值
        p = self.table[hash]            # 关注的节点

        while p is not None:
            if p.key == key:
                return False            # 添加失败
            p = p.next                  # 关注后继节点

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp         # 插入节点
        return True                     # 插入成功

    def remove(self, key: Any) -> bool:
        """删除关键字为key的元素"""
        hash = self.hash_value(key)     # 待删除关键字的散列值
        p = self.table[hash]            # 关注的节点
        pp = None                       # 前一次所关注的节点

        while p is not None:
            if p.key == key:            # 如果找到
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True             # 删除成功
            pp = p
            p = p.next                  # 关注后继节点
        return False                    # 删除失败（key不存在）

    def dump(self) -> None:
        """转储散列表 """
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  → {p.key} ({p.value})', end='')
                p = p.next
            print()
