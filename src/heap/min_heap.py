# Description: Implementation of a min heap.


class MinHeap:
    """
    Children of node at index n
    are at indices 2n + 1 and 2n + 2.
    Parent of node at index n
    is at index (n - 1) // 2.
    """

    def __init__(self):
        self.data = []
        self.length = 0

    def insert(self, value):
        self.length += 1
        self.data.append(value)
        self.heapify_up(self.length - 1)

    def delete(self):
        if self.length == 0:
            return None

        out = self.data[0]

        if self.length == 0:
            self.length -= 1
            self.data = []
            return out

        # Replace the last entry with the root, and heapify down
        self.data[0] = self.data[self.length - 1]
        self.heapify_down(0)
        self.length -= 1
        return out

    def heapify_down(self, index):
        if index >= self.length:
            return

        right_index = self.right_child(index)
        left_index = self.left_child(index)

        if left_index >= self.length:
            return

        left_value = self.data[left_index]
        right_value = self.data[right_index]
        value = self.data[index]

        if left_value > right_value and value > right_value:
            # if the right value is the smallest
            # and the right value is smaller than the value
            # we need to swap and heapify down
            # right path
            self.data[index], self.data[right_index] = (
                self.data[right_index],
                self.data[index],
            )
            self.heapify_down(right_index)

        elif right_value > left_value and value > left_value:
            # if the left value is the smallest
            # and the left value is smaller than the value
            # we need to swap and heapify down
            # left path
            self.data[index], self.data[left_index] = (
                self.data[left_index],
                self.data[index],
            )
            self.heapify_down(left_index)

    def heapify_up(self, index):
        if index == 0:
            return

        parent_index = self.parent(index)
        parent_value = self.data[parent_index]
        value = self.data[index]

        if parent_value > value:
            self.data[parent_index], self.data[index] = (
                self.data[index],
                self.data[parent_index],
            )
            self.heapify_up(parent_index)

    def peek(self):
        if self.length == 0:
            return None
        return self.data[0]

    def __len__(self):
        return self.length

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return (2 * index) + 1

    def right_child(self, index):
        return (2 * index) + 2
