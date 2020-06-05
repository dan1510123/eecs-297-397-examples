class Stack:
    def __init__(self, iterable=None):
        self.__stack = []
        if iterable:
            for item in iterable:
                self.__stack.append(item)

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        return self.__stack.pop()

    def is_empty(self):
        return not self.__stack

    def size(self):
        return len(self.__stack)

    def __repr__(self):
        return f"Stack{repr(self.__stack)}"


class Queue:
    def __init__(self, iterable=None):
        self.__queue = []
        if iterable:
            for item in iterable:
                self.__queue.insert(0, item)

    def enqueue(self, item):
        self.__queue.insert(0, item)

    def dequeue(self):
        return self.__queue.pop()

    def is_empty(self):
        return not self.__queue

    def size(self):
        return len(self.__queue)

    def __repr__(self):
        return f"Queue{repr(self.__queue)}"