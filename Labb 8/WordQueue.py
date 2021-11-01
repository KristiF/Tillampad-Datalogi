class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class WordQueue:
    def __init__(self):
        self._first = None
        self._last = None

    def enqueue(self, data):
        if self._first is None:
            self._first = Node(data)
            self._last = self._first
        else:
            self._last.next = Node(data)
            self._last = self._last.next

    def dequeue(self):
        if self._first is None: return
        result = self._first
        self._first = self._first.next
        return result.data

    def isEmpty(self):
        return (self._first and self._last) is None

    def peek(self):
        if self._first is not None:
            return self._first.data

