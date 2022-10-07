class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.first = 0
        self.last = 0

    def insert(self, item):
        if self.is_overflow:
            bigger_queue = [None] * len(self.queue) * 2

            for idx, item in enumerate(self.queue):
                bigger_queue[idx] = item
            self.queue = bigger_queue
        self.queue[self.last] = item
        self.last += 1

    def remove(self):
        removed = self.queue[self.first] # The list keeps the same structure, but add +1 to exclude a node
        self.first += 1
        return removed

    @property
    def is_overflow(self):
        return self.last >= len(self.queue)

    @property
    def size(self):
        return self.last - self.first

    @property
    def is_empty(self):
        return self.first == self.last