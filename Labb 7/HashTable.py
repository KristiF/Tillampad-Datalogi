from LinkedList import LinkedList

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size):
        self.size = size
        self._array = []
        #self._array = [LinkedList()] * self.size
        for i in range(self.size):
            self._array.append(LinkedList())

    def store(self, key, data):
        idx = hash(key) % self.size
        if self._array[idx].find(key, replace=True, newNode=Node(key, data)) is None:
            self._array[idx].add(Node(key, data))

    def search(self, key):
        idx = hash(key) % self.size

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
