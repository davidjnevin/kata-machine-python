# Doubly Linked List
from typing import Any, Optional


class Node:
    def __init__(
        self,
        data: Any,
        prev_node: Optional["Node"] = None,
        next_node: Optional["Node"] = None,
    ):
        self.data = data
        self.prev = prev_node  # To avoid overshadowing of 'next' builtin
        self.next = next_node  # To avoid overshadowing of 'prev' builtin


class Doubly_linked_list:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def prepend(self, data):
        if self.head:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = Node(data)
        self.length += 1
        return

    def append(self, data):
        if self.tail:
            node = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = self.tail = Node(data)
        self.length += 1
        return

    def get_at(self, idx):
        if idx not in range(self.length):
            raise IndexError()
        if not self.head:
            raise IndexError()
        if idx == 0:
            return self.head.data
        if self.head:
            position = 1
            curr_node = self.head.next
            while curr_node and position <= idx:
                if position == idx:
                    return curr_node.data
                else:
                    curr_node = curr_node.next
                position += 1

    def insertAt(self, idx, data):
        if idx == 0:
            self.prepend(data)
            return
        if idx not in range(self.length):
            raise IndexError()
        if idx == self.length - 1:
            self.append(data)
            return

        position = 1
        node = Node(data)
        curr_node = self.head
        while curr_node.next:
            if position == idx:
                node.prev = curr_node
                node.next = curr_node.next
                curr_node.next.prev = node
                curr_node.next = node
            curr_node = curr_node.next
            position += 1
        self.length += 1
        return

    def _getNodeAt(self, idx):
        postion = 0
        curr_node = self.head
        while curr_node:
            if postion == idx:
                return curr_node
            curr_node = curr_node.next
            postion += 1
        return None

    def _removeNode(self, node):
        self.length -= 1

        if self.length == 0:
            value = self.head.data
            self.head = self.tail = None
            return value
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        node.prev = node.next = None
        return node.data

    def removeAt(self, idx):
        if idx not in range(self.length):
            raise IndexError()
        node = self._getNodeAt(idx)
        return self._removeNode(node)

    def remove(self, data):
        curr_node = self.head
        idx = 0
        while curr_node:
            if curr_node.data == data:
                node = self._getNodeAt(idx)
                return self._removeNode(node)
            curr_node = curr_node.next
            idx += 1
        raise ValueError()
