from Pokemon import Pokemon
from HashTable import HashTable
from DictHash import DictHash
from LinkedList import LinkedList

def hashtest(key):
    result = 0
    for i in range(len(key)):
        result += ord(key[i]) * (i + 1)
    return result % 1442



def loadPokemons():
    #pokemons = DictHash()
    pokemons = HashTable(1442)
    hashes = []
    collisions = 0
    with open("pokemon.csv") as file:
        lines = file.readlines()
    for row in range(1, len(lines)):
        attr = lines[row].split(',')
        pokemons.store(attr[1], Pokemon(int(attr[0]), attr[1], attr[2], attr[3], int(attr[4]),
                                int(attr[5]), int(attr[6]), int(attr[7]), int(attr[8]), int(attr[9]), int(attr[10]), int(attr[11]),
                                evalBool(attr[12])))
        if hashtest(attr[1]) in hashes:
            collisions += 1
        else:
            hashes.append(hashtest(attr[1]))
    print('Antal potentiella krockar:', collisions)
    return pokemons

def evalBool(string):
    return string.lower().strip() == 'true' # evaluerar


def main():
    pokemons = loadPokemons()
    print(pokemons.search('Gothorita').value.ID)
    pokemons.store('Gothorita', 'b')


main()

