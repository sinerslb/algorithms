class StackMaxEffective:

    def __init__(self):
        self.items = []
        self.items_max = None

    def push(self, item):
        if self.items_max is None:
            self.items_max = item
        else:
            if item > self.items_max:
                self.items_max = item
        self.items.append((item, self.items_max))

    def pop(self):
        if len(self.items):
            self.items.pop()
            if len(self.items):
                self.items_max = self.items[-1][1]
            else:
                self.items_max = None
            return
        print('error')

    def get_max(self):
        print(self.items_max)


if __name__ == '__main__':

    stack = StackMaxEffective()
    commands = int(input())
    for i in range(commands):
        command = input().split()
        if len(command) == 1:
            getattr(stack, command[0])()
        else:
            getattr(stack, command[0])(int(command[1]))
