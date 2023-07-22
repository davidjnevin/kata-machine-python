# Singly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singly_linked_list:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def prepend(self, data):
        if self.head:
            node = Node(data)
            node.next = self.head
            self.head = node

        else:
            self.head = Node(data)
        self.length += 1

    def append(self, data):
        if self.head:
            node = Node(data)
            self.head.next = node
        else:
            self.head = Node(data)
        self.length += 1

    def get_at(self, idx: int):
        if not self.head:
            raise ValueError(f"No value at index {idx}")

        if 0 <= idx and idx >= self.length:
            raise IndexError()

        if self.head:
            curr_node = self.head
            for _ in range(idx):
                if curr_node.next:
                    curr_node = curr_node.next
            return curr_node.data


#     prepend(item: T): void {
#     insertAt(item: T, idx: number): void {
#     append(item: T): void {
#     remove(item: T): T | undefined {
#     get(idx: number): T | undefined {
#     removeAt(idx: number): T | undefined {
