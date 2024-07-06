class CircularBufferArray:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def __repr__(self):
        return f"CircularBufferArray({self.buffer})"
