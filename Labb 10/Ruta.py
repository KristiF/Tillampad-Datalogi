from Molgrafik import *

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

    def isEmpty(self):
        return self.atom == self.num == self.next == self.down == None

mol = Ruta(atom = "Cl", num = 2)
mg = Molgrafik()
mg.show(mol)
