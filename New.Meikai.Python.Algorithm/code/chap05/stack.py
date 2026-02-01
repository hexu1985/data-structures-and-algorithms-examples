# 固定长度栈类（使用collections.deque）

from typing import Any
from collections import deque

class Stack:
    """固定长度栈类（使用collections.deque）"""

    def __init__(self, maxlen: int = 256) -> None:
        """初始化"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        """返回已经进栈的数据个数"""
        return len(self.__stk)

    def is_empty(self) -> bool:
        """栈是否为空？"""
        return not self.__stk

    def is_full(self) -> bool:
        """栈是否已满？"""
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        """让value进栈"""
        self.__stk.append(value)

    def pop(self) -> Any:
        """让数据出栈（取出栈顶数据）"""
        return self.__stk.pop()

    def peek(self) -> Any:
        """查看栈中数据（查看栈顶数据）"""
        return self.__stk[-1]

    def clear(self) -> None:
        """清空栈（删除所有数据）"""
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        """从栈中查找value并返回下标（如果未找到，则返回-1）"""
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        """返回栈中包含的value的个数"""
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        """栈中是否包含value？"""
        return self.count(value)

    def dump(self) -> int:
        """转储（按照从栈底到栈顶的顺序显示栈内的所有数据）"""
        print(list(self.__stk))
