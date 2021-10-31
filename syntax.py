from WordQueue import WordQueue
import string

class SyntaxError(Exception): # innebär att den fungerar som vilken exception som helst.
    pass

def readMolecule(q):
    readAtom(q)
    if q.isEmpty() != True:
        readNum(q)

def readAtom(q):
    readBigLetter(q)
    if not q.peek() == None:
        if q.peek() in string.ascii_lowercase:
            readSmallLetter(q)

def readBigLetter(q):
    char = q.dequeue()
    if char in string.ascii_uppercase:
        return
    raise SyntaxError("Not a big letter: " + char)

def readSmallLetter(q):
    char = q.dequeue()
    if char in string.ascii_lowercase:
        return
    raise SyntaxError("Not a small letter: " + char)


def readNum(q):
    num = q.dequeue()
    if num.isnumeric():
        if num in number_list:
            if q.isEmpty() is not True:
                readNum(q)
            return
        raise SyntaxError("Wrong number!")
    raise SyntaxError("A number or a small letter was expected")


def storeMolecule(molecule):
    q = WordQueue()
    molecule = molecule.split()
    for char in molecule:
        q.enqueue(char)
    return q

def CheckSyntax(molecule): #vill fånga upp för att skriva vår egna felutskrift.
    q = storeMolecule(molecule)

    try:
        readMolecule(q)
        return "Follows the syntax!"
    except SyntaxError as error: #error får man från det man raisat
        return str(error) + " before " + str(q)

def main():
    number_list = [2, 3, 4, 5, 6, 7, 8, 9]
    molecule = input("Write a molecule: ")
    result = CheckSyntax(molecule)
    print(result)

if __name__ == "__main__":
    main()
