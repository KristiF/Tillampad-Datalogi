from WordQueue import WordQueue

number_list = [2, 3, 4, 5, 6, 7, 8, 9]


class SyntaxError(Exception): # innebär att den fungerar som vilken exception som helst.
    pass


def readMolecule(q):
    readAtom(q)
    while not q.isEmpty():
        if q.peek().isnumeric():
            readNum(q)
            return

def readAtom(q):
    readBigLetter(q)
    if q.peek() is not None and q.peek().islower():
        q.dequeue()
#    q.dequeue()


def readBigLetter(q):
    char = q.peek()
    if char.isupper():
        q.dequeue()
        return
    else:
        raise SyntaxError("Saknad stor bokstav vid radslutet " + exportQueue(q))

def readNum(q):
    num = q.dequeue()
    if (int(num) == 0) or (int(num) == 1 and q.peek() is None):
        raise SyntaxError('För litet tal vid radslutet ' + exportQueue(q))
    q.dequeue()


def storeMolecule(molecule):
    q = WordQueue()
    nums = []
    for char in molecule:
        #if char.isnumeric():
         #   nums.append(char)
        #else:
            q.enqueue(char)
    #q.enqueue("".join(nums))
    return q

def exportQueue(q):
    result = []
    while not q.isEmpty():
        result.append(q.dequeue())
    return "".join(result)

def CheckSyntax(molecule): #vill fånga upp för att skriva vår egna felutskrift.
    q = storeMolecule(molecule)
    try:
        readMolecule(q)
        return True
    except SyntaxError as e:
        print(e)
        return False

def main():
    molecule = input("Ange molekyl: ").strip()
    if CheckSyntax(molecule):
        print("Formeln är syntaktiskt korrekt")

if __name__ == "__main__":
    main()
