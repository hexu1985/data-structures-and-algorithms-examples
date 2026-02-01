# 通过开放地址法实现散列表

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 桶的属性
class Status(Enum):
    OCCUPIED = 0    # 数据存储
    EMPTY = 1       # 空
    DELETED = 2     # 已删除

class Bucket:
    """组成散列表的桶"""

    def __init__(self, key: Any = None, value: Any = None,
                       stat: Status = Status.EMPTY) -> None:
        """初始化"""
        self.key   = key    # 关键字
        self.value = value  # 値
        self.stat  = stat   # 属性

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """为所有字段设置值"""
        self.key   = key    # 关键字
        self.value = value  # 値
        self.stat  = stat   # 属性

    def set_status(self, stat: Status) -> None:
        """设置属性"""
        self.stat = stat

class OpenHash:
    """实现开放地址法的散列类"""

    def __init__(self, capacity: int) -> None:
        """初始化"""
        self.capacity = capacity                    # 散列表的容量
        self.table = [Bucket()] * self.capacity     # 散列表

    def hash_value(self, key: Any) -> int:
        """求散列值"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)

    def rehash_value(self, key: Any) -> int:
        """求再散列值"""
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """查找关键字为key的桶"""
        hash = self.hash_value(key)     # 待查找关键字的散列值
        p = self.table[hash]            # 关注的桶

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)      # 再散列
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        """查找关键字为key的元素（返回值）"""
        p = self.search_node(key)
        if p is not None:
            return p.value              # 查找成功
        else:
            return None                 # 查找失败

    def add(self, key: Any, value: Any) -> bool:
        """ 添加关键字为key、值为value的元素"""
        if self.search(key) is not None:
            return False                # 该关键字已存储

        hash = self.hash_value(key)     # 待添加关键字的散列值
        p = self.table[hash]            # 关注的桶
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  # 再散列
            p = self.table[hash]
        return False                        # 散列表已满

    def remove(self, key: Any) -> int:
        """删除关键字为key的元素"""
        p = self.search_node(key)       # 关注的桶
        if p is None:
            return False                # 该关键字还未存储
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        """转储散列表"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')

            elif self.table[i].stat == Status.EMPTY:
                print('-- 未存储 --')

            elif self.table[i].stat == Status.DELETED:
                print('-- 已删除 --')
