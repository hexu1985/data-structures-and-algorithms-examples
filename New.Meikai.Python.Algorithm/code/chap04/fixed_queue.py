# 固定长度队列类

from typing import Any

class FixedQueue:

    class Empty(Exception):
        """对于空的FixedQueue队列，在调用deque或peek方法时抛出的异常"""
        pass

    class Full(Exception):
        """对于满的FixedQueue队列，在调用enque方法时抛出的异常"""
        pass

    def __init__(self, capacity: int) -> None:
        """初始化"""
        self.no = 0                    # 当前数据个数
        self.front = 0                 # 队头元素游标
        self.rear = 0                  # 队尾元素游标
        self.capacity = capacity       # 队列容量
        self.que = [None] * capacity   # 队列主体

    def __len__(self) -> int:
        """返回已经入队的数据的个数"""
        return self.no

    def is_empty(self) -> bool:
        """队列是否为空？"""
        return self.no <= 0

    def is_full(self) -> bool:
        """队列是否已满？"""
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        """让数据x入队"""
        if self.is_full():
            raise FixedQueue.Full           # 队列已满
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        """让数据出队"""
        if self.is_empty():
            raise FixedQueue.Empty          # 队列为空
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        """查看数据（查看队头元素）"""
        if self.is_empty():
            raise FixedQueue.Empty      # 队列为空
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        """从队列中查找value并返回下标（如果未找到，则返回-1）"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 查找成功
                return idx
        return -1                       # 查找失败

    def count(self, value: Any) -> bool:
        """返回队列中包含的value的个数"""
        c = 0
        for i in range(self.no):        # 从队尾开始线性查找
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 查找成功
                c += 1                  # 已入队
        return c

    def __contains__(self, value: Any) -> bool:
        """队列中是否包含value？"""
        return self.count(value)

    def clear(self) -> None:
        """清空队列""
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        """按照从队头到队尾的顺序显示队列中的所有数据"""
        if self.is_empty():             # 队列为空
            print('队列为空。')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()
