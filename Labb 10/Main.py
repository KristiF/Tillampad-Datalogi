from Syntax2 import *

while True:
    formula = input('Ange formel: ')
    print(CheckSyntax(formula))
    print('Vad vill du göra?\n1. Visa träd\n2. Beräkna molmassa\n3. Både och')
    val = int(input('Val: '))
    if val == 1:
        buildTree(formula)
    if val == 2:
        print('Vikt:',weight(readFormula(loadQueue(formula))))
    if val == 3:
        print('Vikt:', weight(readFormula(loadQueue(formula))))
        buildTree(formula)