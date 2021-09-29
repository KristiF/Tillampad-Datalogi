class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent

    def writechain(self):
        writechain_helper(self)

def writechain_helper(nod):
    if nod.parent is None:
        print(nod.word)
    else:
        writechain_helper(nod.parent)
        print(nod.word)
