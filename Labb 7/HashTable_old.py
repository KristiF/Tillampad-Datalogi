from LinkedList import LinkedList

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self._array = [LinkedList()] * self.size

    def store(self, key, data):
        idx = self.hashfunction(key)
        if not self._array[idx].find(data):
            self._array[idx].add(Node(key, data))

    def search(self, key):
        idx = self.hashfunction(key)

        if not self._array[idx].isEmpty():
            k = self._array[idx].find(key)
            if k is not None:
                return k
        raise KeyError

    def hashfunction(self, key):
        result = 0
        for i in range(len(key)):
            result += ord(key[i]) * (i + 1)
        return result % self.size
