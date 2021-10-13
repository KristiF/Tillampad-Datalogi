from HashTable import HashTable
from sys import stdin

def main():
    hashtable = HashTable(2000000)

    for line in stdin:
        line = line.strip()
        key, *value = line.split()
        if key == '#':
            break
        elif len(value) != 0:
            hashtable.store(key, value[0])
        else:
            try:
                value = hashtable.search(key)
                print(value)
            except KeyError:
                print('None')


if __name__ == "__main__":
    main()