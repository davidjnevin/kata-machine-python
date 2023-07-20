class ArrayList:
    def __init__(self, capacity=10):
        self.capacity: int = capacity  # maximum capacity
        self.data = [None] * capacity  # allocate memory
        self.length: int = 0  # initial length

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        return str([item for item in self.data])

    def _isFull(self) -> bool:
        isFull = False
        if self.length >= self.capacity:
            isFull = True
        return isFull

    def _resize(self) -> None:
        self.capacity *= 2
        extended_array_list = [None] * self.capacity
        for i in range(self.length):
            extended_array_list[i] = self.data[i]
        self.data = extended_array_list

    def _isValidIndex(self, idx) -> bool:
        isValidIndex = True
        if idx < 0 or idx >= self.length:
            raise IndexError("Invalid index")
        return isValidIndex

    def prepend(self, item):
        if self.length + 1 > self.capacity:
            self._resize()
        keepgoing = True
        last_idx = self.length
        while(keepgoing):
            self.data[last_idx] = self.data[last_idx - 1]
            last_idx -= 1
            if last_idx == 0:
                keepgoing = False
        self.data[0] = item
        self.length += 1

    def append(self, item):
        if self._isFull():
            self._resize()
        self.data[self.length] = item
        self.length += 1

    def insert_at(self, item, idx):
        if self._isFull():
            self._resize()

    def remove(self, item):
        found = False
        # better search possibilities
        for idx, element in enumerate(self.data):
            if element == item:
                found = True
                self.remove_at(idx)
        if not found:
            raise ValueError(f"{item} not found")

    def remove_at(self, idx):
        if self._isValidIndex(idx):
            # Shift all items left overwriting idx item
            for i in range(idx, self.length):
                self.data[i] = self.data[i+1]
            self.length -= 1

    def get(self, idx):
        if self._isValidIndex(idx):
            return self.data[idx]



