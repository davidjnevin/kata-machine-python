from typing import Any, Optional


class Node:
    def __init__(
        self,
        data: Any,
        next_node: Optional["Node"] = None,
    ):
        self.data = data
        self.next = next_node  # To avoid overshadowing of 'next' builtin


class MyQueue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def enqueue(self, data):
        self.length += 1
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node

    def deque(self):
        if self.head:
            self.length -= 1
            value = self.head.data
            self.head.data = None
            self.head = self.head.next
            if self.length == 0:
                self.tail = None
            return value
        else:
            return None

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None

    def getlength(self):
        return self.length
