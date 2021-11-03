# coding=utf-8
from WordQueue import WordQueue


class SyntaxError(Exception):
    pass


def exportQueue(q):
    result = []
    while not q.isEmpty():
        result.append(q.dequeue())
    return "".join(result)


def loadAtoms():
    atoms = []
    with open('Atoms') as file:
        for row in file.readlines():
            for col in row.split('  '):
                atoms.append(col.strip())
    return atoms


def loadQueue(formula):
    q = WordQueue()
    for char in formula:
        q.enqueue(char)
    return q


'''
<formel>::= <mol> 
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
'''


def readFormula(q, atoms):
    while not q.isEmpty():
        readMole(q, atoms)


def readMole(q, atoms, parenthesis=False):
    readGroup(q, atoms, parenthesis)



def readGroup(q, atoms, parenthesis=False):
    """<atom> |<atom><num> | (<mol>) <num>"""
    if q.peek() == '#':
        return

    readAtom(q, atoms)
    if q.peek() == '(':
        parenthesis = True
        q.dequeue()

        while not q.isEmpty() and q.peek().isalpha():
            readMole(q, atoms, True)

        if not q.peek() == ')':
            raise SyntaxError('Saknad högerparentes vid radslutet ' + exportQueue(q))
        q.dequeue()

        readNum(q)

    if q.peek() == ')' and not parenthesis:
        raise SyntaxError('Felaktig gruppstart vid radslutet ' + exportQueue(q))

def readAtom(q, atoms):
    readLetter(q, atoms)
    if not q.isEmpty() and q.peek().isnumeric():
        readNum(q)

def readNum(q):
    if q.isEmpty() or not q.peek().isnumeric():
        raise SyntaxError('Saknad siffra vid radslutet ' + exportQueue(q))
    num = q.dequeue()
    if (int(num) == 0) or (int(num) == 1 and not q.peek().isnumeric()):
        raise SyntaxError('För litet tal vid radslutet ' + exportQueue(q))
    while not q.isEmpty() and q.peek().isnumeric():
        q.dequeue()

def readLetter(q, atoms):
    char = q.peek()
    if char.islower():
        raise SyntaxError('Saknad stor bokstav vid radslutet ' + exportQueue(q))
    if not char.isalpha():
        raise SyntaxError('Felaktig gruppstart vid radslutet ' + exportQueue(q))
    else:
        char = q.dequeue()
        char2 = q.peek()
        if not q.isEmpty() and char2.islower():
            char2 = q.dequeue()
            atom = char + char2

        else:
            atom = char
        if atom not in atoms and atom.isalpha():
            raise SyntaxError('Okänd atom vid radslutet ' + exportQueue(q))

def CheckSyntax(formula):
    try:
        readFormula(loadQueue(formula), loadAtoms())
        return 'Formeln är syntaktiskt korrekt'
    except SyntaxError as e:
        return e

#while True:
print(CheckSyntax(input()))
