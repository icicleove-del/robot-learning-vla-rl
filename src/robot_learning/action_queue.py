"""教学用的简化 action-chunk 队列。

目的：帮助理解动作序列、缓存、重新规划时的替换行为。
不等于 SmolVLA 的真实 select_action，也不承担真实机器人安全控制。
"""
from collections import deque
from typing import Deque, Generic, Iterable, TypeVar

T = TypeVar("T")


class ToyActionQueue(Generic[T]):
    def __init__(self) -> None:
        self._queue: Deque[T] = deque()

    def replace_chunk(self, actions: Iterable[T]) -> None:
        """用新动作块覆盖旧动作：仅用于演示重新规划。"""
        self._queue = deque(actions)

    def next_action(self) -> T:
        """取出一项待执行动作，队列空时抛出 IndexError。"""
        return self._queue.popleft()

    def __len__(self) -> int:
        return len(self._queue)
