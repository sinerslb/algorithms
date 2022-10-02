# id решения 69304525
from typing import List


def nearest_null(houses: List[int], num_houses: int) -> List[int]:
    """Расчёт расстояния до ближайшего пустого участка."""

    # определяем и фиксируем позиции '0'
    no_houses: List[int] = [i for i in range(num_houses) if houses[i] == 0]
    null_first: int = no_houses[0]
    null_last: int = no_houses[0] if len(no_houses) == 1 else no_houses[1]

    # определяем дистанции на отрезке до первого ноля
    for i in range(null_first):
        houses[i] = null_first-i

    # определяем дистанции на всех отрезках между парами нолей
    n_next: int = 1
    for i in range(null_first+1, no_houses[-1]):
        if houses[i]:
            houses[i] = min(i - null_first, null_last - i)
        else:
            n_next += 1
            null_first = null_last
            null_last = no_houses[n_next]

    # определяем дистанции на отрезке после последнего ноля
    for i in range(null_last+1, num_houses):
        houses[i] = i - null_last

    return houses


if __name__ == '__main__':
    # считываем входные данные
    num_houses: int = int(input())
    houses: List[int] = list(map(int, input().split()))
    print(*nearest_null(houses, num_houses), sep=' ')
