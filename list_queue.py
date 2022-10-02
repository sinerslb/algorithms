class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):
        node = Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def get(self):
        if self.is_empty():
            print('error')
            return
        x = self.head.value
        print(x)
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return x


if __name__ == '__main__':
    # считываем входные данные
    commands = int(input())
    queue = Queue()
    for i in range(commands):
        command = input().split()
        num_com = len(command)
        if command[0] == 'size':
            print(queue.size)
        elif num_com == 1:
            getattr(queue, command[0])()
        else:
            getattr(queue, command[0])(int(command[1]))
