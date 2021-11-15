#coding utf-8
from WordQueue import WordQueue
from Molgrafik import *
p = WordQueue()

'''
<formel>::= <mol> 
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
'''

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

def readFormula(q):
    return readMole(q)

def readMole(q):
    rutan = readGroup(q)
    if q.peek():
        if q.peek() == "(" or q.peek().isalpha():
            rutan.next = readMole(q)
    return rutan

def readGroup(q):
    rutan = Ruta()
    if q.peek() == '(':
        p.enqueue(q.dequeue())
        if q.peek() == ')':
            raise SyntaxError('Felaktig gruppstart vid radslutet ' + exportQueue(q))
        rutan.down = readMole(q)
        if q.peek() == ')':
            if p.isEmpty():
                raise SyntaxError('Felaktig gruppstart vid radslutet ' + exportQueue(q))
            else:
                q.dequeue()
                rutan.num = readNum(q)
                p.dequeue()

    else:
        rutan.atom = readAtom(q)
        if not q.isEmpty():
            if q.peek().isnumeric():
                rutan.num = readNum(q)
    if not p.isEmpty() and q.isEmpty():
        raise SyntaxError('Saknad högerparentes vid radslutet ' + exportQueue(q))
    return rutan

def readAtom(q):
    return readLetter(q)

def readNum(q):
    result = []
    if not q.peek().isnumeric():
        raise SyntaxError('Saknad siffra vid radslutet ' + exportQueue(q))
    num = q.dequeue()
    result.append(num)
    if (int(num) == 0):
        raise SyntaxError('För litet tal vid radslutet ' + exportQueue(q))
    if (int(num) == 1):
        if q.isEmpty() or not q.peek().isnumeric():
            raise SyntaxError('För litet tal vid radslutet ' + exportQueue(q))
    while not q.isEmpty() and q.peek().isnumeric():
        result.append(q.dequeue())
    return int("".join(result))

def readLetter(q):
    atoms = loadAtoms()
    char = q.peek()
    if not char.isalpha():
        raise SyntaxError('Felaktig gruppstart vid radslutet ' + exportQueue(q))
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
    return atom

def CheckSyntax(formula):
    p.empty()
    try:
        return readFormula(loadQueue(formula))
    except SyntaxError as e:
        return str(e)

def buildTree(formula):
    p.empty()
    rutan = CheckSyntax(formula)
    mg = Molgrafik()
    mg.show(rutan)

vikter = {"H": 1.00794, "He": 4.002602, "Li": 6.941, "Be": 9.012182, "B": 10.811, "C": 12.0107, "N": 14.0067,
            "O": 15.9994, "F": 18.9984032, "Ne": 20.1797, "Na": 22.98976928, "Mg": 24.3050, "Al": 26.9815386,
            "Si": 28.0855, "P": 30.973762, "S": 32.065, "Cl": 35.453, "K": 39.0983, "Ar": 39.948, "Ca": 40.078,
            "Sc": 44.955912, "Ti": 47.867, "V": 50.9415, "Cr": 51.9961, "Mn": 54.938045, "Fe": 55.845, "Ni": 58.6934,
            "Co": 58.933195, "Cu": 63.546, "Zn": 65.38, "Ga": 69.723, "Ge": 72.64, "As": 74.92160, "Se": 78.96,
            "Br": 79.904, "Kr": 83.798, "Rb": 85.4678, "Sr": 87.62, "Y": 88.90585, "Zr": 91.224, "Nb": 92.90638,
            "Mo": 95.96, "Tc": 98, "Ru": 101.07, "Rh": 102.90550, "Pd": 106.42, "Ag": 107.8682, "Cd": 112.411,
            "In": 114.818, "Sn": 118.710, "Sb": 121.760, "I": 126.90447, "Te": 127.60, "Xe": 131.293, "Cs": 132.9054519,
            "Ba": 137.327, "La": 138.90547, "Ce": 140.116, "Pr": 140.90765, "Nd": 144.242, "Pm": 145, "Sm": 150.36,
            "Eu": 151.964, "Gd": 157.25, "Tb": 158.92535, "Dy": 162.500, "Ho": 164.93032, "Er": 167.259,
            "Tm": 168.93421, "Yb": 173.054, "Lu": 174.9668, "Hf": 178.49, "Ta": 180.94788, "W": 183.84, "Re": 186.207,
            "Os": 190.23, "Ir": 192.217, "Pt": 195.084, "Au": 196.966569, "Hg": 200.59, "Tl": 204.3833, "Pb": 207.2,
            "Bi": 208.98040, "Po": 209, "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Pa": 231.03588,
            "Th": 232.03806, "Np": 237, "U": 238.02891, "Am": 243, "Pu": 244, "Cm": 247, "Bk": 247, "Cf": 251,
            "Es": 252, "Fm": 257, "Md": 258, "No": 259, "Lr": 262, "Rf": 265, "Db": 268, "Hs": 270, "Sg": 271,
            "Bh": 272, "Mt": 276, "Rg": 280, "Ds": 281, "Cn": 285}

def weight(ruta, vikter):
    result = 0
    if ruta.down:
        result += ruta.num * weight(ruta.down, vikter)
    if ruta.next:
        result += vikter[ruta.atom] * ruta.num + weight(ruta.next, vikter)
    if not ruta.next and not ruta.down:
        result += vikter[ruta.atom] * ruta.num

    return result

#buildTree('Si(C3(COOH)2)4(H2O)7')
#buildTree('(CH3)2(CH2)4')
ruta = CheckSyntax('Si(C3(COOH)2)4(H2O)7')
print(weight(ruta, vikter))