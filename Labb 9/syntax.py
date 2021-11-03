from WordQueue import WordQueue


class SyntaxError(Exception):  # innebär att den fungerar som vilken exception som helst.
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
    readGroup(q, atoms)



def readGroup(q, atoms, parenthesis=False):
    """<atom> |<atom><num> | (<mol>) <num>"""

    readAtom(q, atoms)
    if q.peek() == '(':
        parenthesis = True
        q.dequeue()

        while not q.isEmpty() and q.peek().isalpha():
            print(q.peek())
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
        raise SyntaxError('Saknad siffra vid radslutet C')
    num = q.dequeue()
    if (int(num) == 0) or (int(num) == 1 and q.peek() is None):
        raise SyntaxError('För litet tal vid radslutet ' + exportQueue(q))
    while not q.isEmpty() and q.peek().isnumeric():
        q.dequeue()

def readLetter(q, atoms):
    char = q.dequeue()
    if char.islower():
        raise SyntaxError('Saknad stor bokstav vid radslutet ' + exportQueue(q))
    else:
        if not q.isEmpty() and q.peek().islower():
            atom = char + q.peek()
        else:
            atom = char
        if atom not in atoms:
            raise SyntaxError('Okänd atom vid radslutet ' + exportQueue(q))

def CheckSyntax(formula):  # vill fånga upp för att skriva vår egna felutskrift.
    try:
        readFormula(loadQueue(formula), loadAtoms())
        return True
    except SyntaxError as e:
        return e

while True:
    print(CheckSyntax(input()))
