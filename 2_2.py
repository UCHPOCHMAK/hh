from collections import deque

class CircularBufferDeque:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def enqueue(self, item):
        if len(self.buffer) == self.buffer.maxlen:
            raise OverflowError("Buffer is full")
        self.buffer.append(item)

    def dequeue(self):
        if not self.buffer:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()

    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def is_empty(self):
        return not self.buffer

    def __repr__(self):
        return f"CircularBufferDeque({list(self.buffer)})"
