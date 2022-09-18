# id решения 69453757
import operator
import re
from typing import List


class Stack:
    """Стек для результатов вычислений."""

    def __init__(self) -> None:
        self.items: List[int] = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> int:
        if len(self.items):
            result = self.items.pop()
        return result


def pol_calculation(list: List[str], stack: Stack) -> None:
    """Вычисления."""

    do_calc = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
        }

    for i in list:
        if re.fullmatch(r'[-+]?\d+', i):
            stack.push(int(i))
        else:
            first = stack.pop()  # type: int
            stack.push(do_calc[i](stack.pop(), first))


if __name__ == '__main__':
    stack: Stack = Stack()
    data: List[str] = [i for i in input().split()]
    pol_calculation(data, stack)
    print(stack.pop())
