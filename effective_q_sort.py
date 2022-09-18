# id решения 69610315
from random import randrange
from typing import Tuple


def partition(arr, start_point, end_point) -> int:
    """Перестановка элементов внутри выбранной части,
    относительно случано выбранного опорного элемента.
    """

    # Определяем опорный элемент, и ставим его в начало интервала
    pivot_index = randrange(start_point, end_point)
    arr[start_point], arr[pivot_index] = arr[pivot_index], arr[start_point]
    pivot = arr[start_point]
    l_pointer = start_point + 1
    r_pointer = end_point
    done = False
    # Сортировка элементов
    while not done:
        while l_pointer <= r_pointer and arr[l_pointer] <= pivot:
            l_pointer += 1
        while r_pointer >= l_pointer and arr[r_pointer] >= pivot:
            r_pointer -= 1
        if l_pointer > r_pointer:
            done = True
        else:
            arr[l_pointer], arr[r_pointer] = arr[r_pointer], arr[l_pointer]
    # Ставим опорный элемент между отсортированными частями
    arr[start_point], arr[r_pointer] = arr[r_pointer], arr[start_point]
    return r_pointer


def quick_sort(arr, l_pointer, r_pointer) -> None:
    """Быстрая сортировка методом in-place."""

    if l_pointer < r_pointer:
        split_index = partition(arr, l_pointer, r_pointer)
        quick_sort(arr, l_pointer, split_index - 1)
        quick_sort(arr, split_index + 1, r_pointer)


def ordering(tpl) -> Tuple[int, int, str]:
    """Упорядочивание данных для сортировки."""

    return (-int(tpl[1]), int(tpl[2]), tpl[0])


if __name__ == '__main__':
    nums_participants = int(input())
    array = [ordering(input().split()) for _ in range(nums_participants)]
    quick_sort(array, 0, len(array) - 1)
    for intern in array:
        print(intern[2])
