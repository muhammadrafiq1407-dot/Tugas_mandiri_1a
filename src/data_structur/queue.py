from collections import deque


class Queue:
    def __init__(self):
        # deque digunakan sebagai tempat penyimpanan data
        self.items = deque()

    def enqueue(self, item):
        if item is None:
            raise ValueError("Item tidak boleh None")

        self.items.append(item)


    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()

        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]

        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def get_all(self):
        return list(self.items)

    def clear(self):
        self.items.clear()


    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(list(self.items))

