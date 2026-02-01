# 固定长度的栈类

from typing import Any

class FixedStack:
    """固定长度的栈类"""

    class Empty(Exception):
        """对于空的FixedStack栈，在调用pop或peek方法时抛出的异常"""
        pass

    class Full(Exception):
        """对于满的FixedStack，调用push方法时抛出的异常"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """初始化"""
        self.stk = [None] * capacity    # 栈主体
        self.capacity = capacity        # 栈的容量
        self.ptr = 0                    # 栈指针

    def __len__(self) -> int:
        """返回已经进栈的数据的个数"""
        return self.ptr

    def is_empty(self) -> bool:
        """栈是否为空？"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """栈是否已满？"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """让value进栈"""
        if self.is_full():             # 栈已满
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """让数据出栈（取出栈顶数据）"""
        if self.is_empty():            # 栈为空
             raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """查看栈中数据（查看栈顶数据）"""
        if self.is_empty():            # 栈为空
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """清空栈（删除所有数据）"""
        self.ptr = 0

    def find(self, value: Any) -> Any:
        """从栈中查找value并返回下标（如果未找到，则返回-1）"""
        for i in range(self.ptr - 1, -1, -1):   # 从栈顶开始线性查找
            if self.stk[i] == value:
                return i            # 查找成功
        return -1                   # 查找失败

    def count(self, value: Any) -> bool:
        """返回栈中包含的value的个数"""
        c = 0
        for i in range(self.ptr):   # 从栈底开始线性查找
            if self.stk[i] == value:
                c += 1              # 已入栈
        return c

    def __contains__(self, value: Any) -> bool:
        """栈中是否包含value？""
        return self.count(value)

    def dump(self) -> None:
        """转储（按照从栈底到栈顶的顺序显示栈内的所有数据）"""
        if self.is_empty():                 # 栈为空
            print('栈为空。')
        else:
            print(self.stk[:self.ptr])
