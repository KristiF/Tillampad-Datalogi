from LinkedList import LinkedQ

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
        val = Node(key, data)
        if self._array[idx] is None:
            self._array[idx] = val
        else:
            if isinstance(self._array[idx], Node):
                if self._array[idx].key == key:
                    self._array[idx] = val
                    return
                tmp_list = LinkedQ()
                tmp_list.enqueue(self._array[idx])
                tmp_list.enqueue(val)
                self._array[idx] = tmp_list
            else:
                while not self._array[idx].isEmpty():
                    curNode = self._array[idx].dequeue()
                    if curNode.key == key:
                        self._array[idx].enqueue(val)
                    else:
                        self._array[idx].enqueue(curNode)


    def search(self, key):
        idx = self.hashfunction(key)
        if self._array[idx] is None:
            raise KeyError
        else:
            if isinstance(self._array[idx], LinkedQ):
                while not self._array[idx].isEmpty():
                    curNode = self._array[idx].dequeue()
                    tmp_array = []
                    tmp_array.append(curNode)
                    if curNode.key == key:
                        return curNode.value

            else:
                return self._array[idx].value
        raise KeyError

    def hashfunction(self, key):
        result = 0
        for i in range(len(key)):
            result += ord(key[i]) * (i + 1)
        return result % self.size

