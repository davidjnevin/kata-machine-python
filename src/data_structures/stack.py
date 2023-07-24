from typing import Optional


class Node:
    def __init__(self, data, prev_node: Optional["Node"] = None):
        self.data = data
        self.prev = prev_node


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        self.length += 1
        node = Node(data)
        if self.head:
            node.prev = self.head
            self.head = node
        else:
            self.head = node

    def pop(self):
        if not self.head:
            return None
        self.length -= 1
        value = self.head.data
        self.head = self.head.prev
        return value

    def peek(self):
        if not self.head:
            return None
        return self.head.data
