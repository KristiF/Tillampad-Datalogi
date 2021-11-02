from WordQueue import WordQueue

class SyntaxError(Exception): # innebär att den fungerar som vilken exception som helst.
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
<formel>::= <mol> \n
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
'''

def readFormula(q, atoms):
    readMole(q, atoms)

def readMole(q, atoms):
    readGroup(q, atoms)

def readGroup(q, atoms):
    if q.peek() == '(':
        q.dequeue()
        readAtom(q, atoms)
        if not q.peek() == ')':
            SyntaxError('Saknad högerparentes vid radslutet ' + exportQueue(q))

def readAtom(q, atoms):
    readLetter(q, atoms)
    readNum(q)

def readNum(q):
    if q.peek() is None or not q.peek().isnumeric():
        return
    num = q.dequeue()
    if (int(num) == 0) or (int(num) == 1 and q.peek() is None):
        raise SyntaxError('För litet tal vid radslutet ' + exportQueue(q))
    q.dequeue()


def readLetter(q, atoms):
    if not q.peek().isupper():
        SyntaxError('Saknad stor bokstav vid radslutet ' + exportQueue(q))
    else:
        char = q.dequeue()
        if q.peek() is None and not char in atoms:
            SyntaxError('Okänd atom vid radslutet ' + exportQueue(q))
        else:
            if not char.join(q.peek()):
                SyntaxError('Okänd atom vid radslutet ' + exportQueue(q))
        q.dequeue()

def CheckSyntax(formula): #vill fånga upp för att skriva vår egna felutskrift.
    try:
        readFormula(loadQueue(formula), loadAtoms())
        return True
    except SyntaxError as e:
        print(e)
        return False

