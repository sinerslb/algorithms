# id решения 69610279
from typing import List


def binarySearch(nums: List[int], target: int, left: int, right: int) -> int:
    """Бинарный поиск."""
    if right < left:
        return -1
    mid = (left + right) // 2  # type: int
    if nums[mid] == target:
        return mid
    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            return binarySearch(nums, target, left, mid)
        else:
            return binarySearch(nums, target, mid + 1, right)
    else:
        if nums[mid] < target <= nums[right]:
            return binarySearch(nums, target, mid + 1, right)
        else:
            return binarySearch(nums, target, left, mid)


def broken_search(nums: List[int], target: int) -> int:
    """Поиск в отсортированном, но сломанном массиве."""

    return binarySearch(nums, target, 0, len(nums) - 1)


def test() -> None:
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()
