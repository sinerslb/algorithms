# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def print_range(node: Node, left: int, right: int) -> None:
    if node.value < left:
        if node.right:
            print_range(node.right, left, right)
    elif node.value >= left:
        if node.left:
            print_range(node.left, left, right)
        if node.value <= right:
            print(node.value)
            if node.right:
                print_range(node.right, left, right)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test()
