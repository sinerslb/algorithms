# id решения 69452796
from typing import List, Optional


class Deque:
    """Дек."""
    def __init__(self, n: int) -> None:
        self.__queue = [None] * n  # type: List[Optional[int]]
        self.__max_n = n  # type: int
        self.__n_minus_1 = n - 1  # type: int
        self.__head = 0  # type: int
        self.__tail = 0  # type: int
        self.__size = 0  # type: int

    def is_empty(self) -> bool:
        """Проверка, очередь пуста или нет."""
        return self.__size == 0

    def is_empty_true(self) -> None:
        """Обнуление начала и конца, если дек пуст."""
        self.__head = 0
        self.__tail = 0

    def push_back(self, x: int) -> None:
        """Добавление элемента в конец очереди."""
        if self.__size == self.__max_n:
            print('error')
            return None
        if self.__queue[self.__tail] is not None:
            self.__tail = (self.__tail + 1) % self.__max_n
        self.__queue[self.__tail] = x
        self.__size += 1

    def push_front(self, x: int) -> None:
        """Добавление элемента в начало очереди."""
        if self.__size == self.__max_n:
            print('error')
            return None
        if self.__queue[self.__head] is not None:
            self.__head = self.__head - 1
            if self.__head < 0:
                self.__head = self.__n_minus_1
        self.__queue[self.__head] = x
        self.__size += 1

    def pop_front(self) -> Optional[int]:
        """Изъятие элемента из начала очереди."""
        if self.is_empty():
            print('error')
            res = None  # type: Optional[int]
        else:
            res = self.__queue[self.__head]
            self.__queue[self.__head] = None
            self.__head = (self.__head + 1) % self.__max_n
            self.__size -= 1
            if self.is_empty():
                self.is_empty_true()
        return res

    def pop_back(self) -> Optional[int]:
        """Изъятие элемента с конца очереди."""
        if self.is_empty():
            print('error')
            res = None  # type: Optional[int]
        else:
            res = self.__queue[self.__tail]
            self.__queue[self.__tail] = None
            self.__tail = self.__tail - 1
            if self.__tail < 0:
                self.__tail = self.__n_minus_1
            self.__size -= 1
            if self.is_empty():
                self.is_empty_true()
        return res


if __name__ == '__main__':
    # считываем входные данные
    num_commands = int(input())  # type: int
    queue_size = int(input())  # type: int
    queue = Deque(queue_size)  # type: Deque
    for i in range(num_commands):
        command = input().split()  # type: List[str]
        num_com = len(command)  # type: int
        if num_com == 1:
            res = getattr(queue, command[0])()  # type: Optional[int]
        else:
            res = getattr(queue, command[0])(int(command[1]))
        if res is not None:
            print(res)
