def sift_down(heap, idx):
    left = 2 * idx
    right = 2 * idx + 1
    len_heap = len(heap) - 1

    # нет дочерних узлов
    if len_heap < left:
        return idx

    # right <= heap.size проверяет, что есть оба дочерних узла
    if (right <= len_heap) and (heap[left] < heap[right]):
        idx_largest = right
    else:
        idx_largest = left

    if heap[idx] < heap[idx_largest]:
        heap[idx], heap[idx_largest] = heap[idx_largest], heap[idx]
        return sift_down(heap, idx_largest)
    else:
        return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
