class Stack:
    def __init__(self, stackMaxSize=10):
        self.data = []
        self.pointer = -1
        self.dataMaxSize = stackMaxSize

    def count(self):
        return len(self.data)

    def isEmpty(self):
        if self.data:
            return False
        else:
            return True

    def isFull(self):
        if self.count == self.dataMaxSize:
            return True
        else:
            return False

    def peek(self, index):
        try:
            return self.data[index]
        except IndexError:
            return "IndexError: Outside scope of stack."

    def display(self):
        return self.data

    def push(self, element):
        if self.dataMaxSize <= self.count():
            return "StackOverflow: No more space in memory"
        else:
            self.pointer += 1
            self.data.insert(self.pointer, element)

    def pop(self):
        if self.count() == 0:
            return "StackUnderflow: Can't remove element from empty list"
        else:
            self.data.pop()
            self.pointer -= 1