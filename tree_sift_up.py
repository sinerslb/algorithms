def sift_up(heap, idx):
    if idx == 1:
        return idx
    parent_idx = int(idx / 2)
    if heap[parent_idx] < heap[idx]:
        heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
        return sift_up(heap, parent_idx)
    else:
        return idx


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()
