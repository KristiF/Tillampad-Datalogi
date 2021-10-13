class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._first = None
        self._last = None

    def add(self, data):
        if self._first is None:
            self._first = Node(data)
            self._last = self._first
        else:
            self._last.next = Node(data)
            self._last = self._last.next

    def dequeue(self):
        result = self._first
        self._first = self._first.next
        return result.data

    def isEmpty(self):
        return (self._first and self._last) is None

    def find(self, key, replace=False, newNode=None):
        cur = self._first
        while cur is not None:
            if cur.data.key == key:
                if replace:
                    cur.data = newNode
                return cur.data.value
            cur = cur.next

