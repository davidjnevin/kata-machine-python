# Singly Linked List


from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next_node: Optional["Node"] = None):
        self.data = data
        self.next = next_node  # To avoid overshadowing of 'next' builtin


class Singly_linked_list:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __str__(self) -> str:
        output = "["
        curr_node = self.head
        while curr_node:
            output += f"{curr_node.data}, "
            curr_node = curr_node.next
        return output + "]"

    def prepend(self, data):
        if self.head:
            node = Node(data)
            node.next = self.head
            self.head = node

        else:
            self.head = Node(data)
        self.length += 1
        return

    def get_at(self, idx: int):
        if not self.head:
            raise ValueError(f"No value at index {idx}")

        if idx not in range(self.length):
            raise IndexError()

        if self.head:
            curr_node = self.head
            for _ in range(idx):
                if curr_node.next:
                    curr_node = curr_node.next
            return curr_node.data

    def append(self, data):
        if self.head:
            node = Node(data)
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node
        else:
            self.head = Node(data)
        self.length += 1
        return

    def insertAt(self, idx: int, data):
        if self.length == idx and idx == 0:
            self.append(data)
            return

        if idx not in range(self.length):
            raise IndexError()

        if self.head:
            node = Node(data)
            curr_node = self.head
            prev = self.head
            if idx == 0:
                self.prepend(data)
                return

            position = 0
            while curr_node and position != idx:
                prev = curr_node
                curr_node = curr_node.next
                position += 1
            node.next = curr_node
            prev.next = node
            self.length += 1
            return
        else:
            self.append(data)
            return

    def removeAt(self, idx: int):
        if not self.head:
            raise IndexError()

        if idx not in range(self.length):
            raise IndexError()

        if self.head:
            curr_node = self.head
            prev = self.head
            if idx == 0:
                # self.head.data = None
                self.head = self.head.next
                self.length -= 1
                return

            position = 1
            while curr_node and position <= idx:
                prev = curr_node
                curr_node = curr_node.next
                position += 1

            prev.next = curr_node.next
            curr_node = None
            self.length -= 1

    def remove(self, data):
        if not self.head:
            raise ValueError()

        curr_node = self.head
        idx = 0
        while curr_node:
            if curr_node.data == data:
                self.removeAt(idx)
                return
            curr_node = curr_node.next
            idx += 1
        raise ValueError()
