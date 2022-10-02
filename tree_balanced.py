# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root, start=True):
    if root.left:
        bal_l, left = solution(root.left, start=False)
    else:
        left = 0
        bal_l = True
    if root.right:
        bal_r, right = solution(root.right, start=False)
    else:
        right = 0
        bal_r = True
    if start:
        return abs(left - right) <= 1 and bal_l and bal_r
    else:
        return abs(left - right) <= 1 and bal_l and bal_r, max(left, right) + 1


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
