class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self._array = [None] * self.size

    def store(self, key, data):
        idx = self.hashfunction(key)
        if self._array[idx] is None:
            self._array[idx] = data
        else:
            if isinstance(self._array[idx], list):
                self._array[idx].append(data)
            else:
                self._array[idx] = [self._array[idx], data]



    def search(self, key):
        idx = self.hashfunction(key)
        if self._array[idx] is None:
            raise KeyError
        else:
            if isinstance(self._array[idx], list):
                for e in self._array[idx]:
                    if str(e) == key:
                        return e
            else:
                return self._array[idx]
        raise KeyError

    def hashfunction(self, key):
        result = 0
        for i in range(len(key)):
            result += ord(key[i]) * (i + 1)
        return result % self.size



