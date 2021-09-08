# Nora och Kristi
from array import array
class ArrayQ:
    def __init__(self):
        self._array = array('i')

    def enqueue(self, x):
        self._array.append(x)

    def dequeue(self):
        return self._array.pop(0)

    def isEmpty(self):
        return len(self._array) == 0

    def size(self):
        return len(self._array)