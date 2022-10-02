# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root, min_val=None, max_val=None) -> bool:
    res_r = True
    res_l = True
    if root.right:
        if (
            root.right.value <= root.value
            or max_val is not None and root.right.value >= max_val
        ):
            return False
        else:
            res_r = solution(root.right, min_val=root.value, max_val=max_val)
    if root.left:
        if (
            root.left.value >= root.value
            or min_val is not None and root.left.value <= min_val
        ):
            return False
        else:
            res_l = solution(root.left, min_val=min_val, max_val=root.value)
    return res_r and res_l


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
