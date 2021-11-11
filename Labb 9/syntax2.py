#coding utf-8
from WordQueue import WordQueue

class SyntaxError(Exception):
    pass


def exportQueue(q):
    result = []
    while not q.isEmpty():
        result.append(q.dequeue())
    return "".join(result)

def loadAtoms():
    atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
     'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y',
     'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce',
     'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
     'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm',
     'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']
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


def readFormula(q):
    readMole(q)

def readMole(q):
    if q.peek() == '(' or q.peek().isalpha() or not q.peek().isnumeric():
        readGroup(q)
        readMole(q)

def readGroup(q):
    if q.peek() == '(':
        q.dequeue()
        if q.peek() == ')':
            raise SyntaxError('Felaktig gruppstart vid radslutet ' + exportQueue(q))
        readMole(q)
        if not q.peek() == ')':
            raise SyntaxError('Saknad högerparentes vid radslutet ' + exportQueue(q))
        q.dequeue()
        if not q.peek().isnumeric():
            raise SyntaxError('Felaktig gruppstart vid radslutet ' + exportQueue(q))
        readNum(q)


    readAtom(q)
    """
    if q.peek() == '(':
        q.dequeue()

        if not q.peek() == ')':
            raise SyntaxError('Saknad högerparentes vid radslutet ' + exportQueue(q))
        q.dequeue()
        readNum(q)
    if not q.isEmpty():
        if (q.peek() == ')' and not parenthesis):
            raise SyntaxError('Felaktig gruppstart vid radslutet ' + exportQueue(q))
"""
def readAtom(q):
    readLetter(q)
    if not q.isEmpty():
        if q.peek().isnumeric():
            readNum(q)

def readNum(q):
    if q.isEmpty() or not q.peek().isnumeric():
        raise SyntaxError('Saknad siffra vid radslutet ' + exportQueue(q))
    num = q.dequeue()
    if (int(num) == 0):
        raise SyntaxError('För litet tal vid radslutet ' + exportQueue(q))
    if (int(num) == 1):
        if q.isEmpty() or not q.peek().isnumeric():
            raise SyntaxError('För litet tal vid radslutet ' + exportQueue(q))
    while not q.isEmpty() and q.peek().isnumeric():
        q.dequeue()

def readLetter(q):
    atoms = loadAtoms()
    char = q.peek()
    if not char.isalpha():
        raise SyntaxError('Felaktigt gruppstart vid radslutet ' + exportQueue(q))
    elif char.islower():
        raise SyntaxError('Saknad stor bokstav vid radslutet ' + exportQueue(q))
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
        readFormula(loadQueue(formula))
        return 'Formeln är syntaktiskt korrekt'
    except SyntaxError as e:
        return str(e)

