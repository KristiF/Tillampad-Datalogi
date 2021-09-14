# Labb 1
# Krist & Nora

class Pokemon:
    def __init__(self, ID, name, type1, type2, total, HP, attack, defense,
                 spAttack, spDefense, speed, gen, legendary):
            self.ID = ID
            self.name = name
            self.type1 = type1
            self.type2 = type2
            self.total = total
            self.HP = HP
            self.attack = attack
            self.defense = defense
            self.spAttack = spAttack
            self.spDefense = spDefense
            self.speed = speed
            self.gen = gen
            self.legendary = legendary

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.total < other.total

    def isLegendary(self):
        return self.legendary

    def getSpeed(self):
        return self.speed


def testClass():
    test1 = Pokemon(1000, "Kristi", "Water", "Poison", 587, 42, 140, 3, 34, 64, 40, 1, True)
    test2 = Pokemon(1001, "Dunder", "Fire", "Bug", 1337, 69, 69, 69, 69, 69, 69, 1, True)

    print(test1 < test2, test1, test1.legendary, test1.getSpeed())

pokemons = []

def evalBool(string):
    return string.lower().strip() == 'true' # evaluerar

def loadPokemons():
    pokemons = []
    with open("pokemon.csv") as file:
        lines = file.readlines()
    for row in range(1, len(lines)):
        attr = lines[row].split(',')
        pokemons.append(Pokemon(int(attr[0]), attr[1], attr[2], attr[3], int(attr[4]),
                                int(attr[5]), int(attr[6]), int(attr[7]), int(attr[8]), int(attr[9]), int(attr[10]), int(attr[11]),
                               evalBool(attr[12])))
    return pokemons

def searchPokemon(search, pokemonList):
    for pokemon in pokemonList:
        if str(pokemon).lower() == search.lower():
            return pokemon

print(searchPokemon('Dratini', loadPokemons()).isLegendary())




