from Node import Node
class Bintree:
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        self.root = putta(self.root, newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def putta(root, newvalue):
    if root is None:
        return Node(newvalue)
    if newvalue > root.value:
        root.right = putta(root.right, newvalue)
    else:
        root.left = putta(root.left, newvalue)
    return root


def finns(root, value):
    if root.value == value:
        return True
    elif root.value is None:
        return False
    if value > root.value:
        finns(root.right, value)
    else:
        finns(root.left, value)

def skriv(root):
    if root is None:
        return
    skriv(root.left)
    print(root.value, end=' ')
    skriv(root.right)

test = Bintree()
test.put(51)
test.put(57)
print(test.root.right.value)

