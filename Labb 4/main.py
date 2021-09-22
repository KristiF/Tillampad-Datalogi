from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()
gamla = Bintree()
q = LinkedQ()

class Hittat(Exception):
    pass

def ordlista():
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # Ett trebokstavsord per rad
            svenska.put(ordet)  # in i sökträdet

#startord = input("Mata in startord: ")

#Version 1
def makeChildren(startord, q):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö" # definierar vilka tecken som existerar i alfabetet
    gamla.put(startord) # lägger automatiskt in startord som ett dumbarn
    for bokstav in range(len(startord)): # går igenom varje bokstav i starordet
        for tkn in alfabet:  # går igenom varje tecken i alfabetet
            nyttOrd = list(startord) # gör om startordet till en lista där varje bokstav är ett element
            nyttOrd[bokstav] = tkn #byter ut varje bokstav till varje tecken i alfabetet
            nyttOrd = "".join(nyttOrd) # sätter ihop alla elementen i listan till en sträng och bildar det nya ordet
            if nyttOrd in svenska and nyttOrd not in gamla:
                gamla.put(nyttOrd)
                q.enqueue(nyttOrd )# print(nyttOrd) i version 1 samt bort med parametern q

def main():
    ordlista()
    startord = input("Välj startord: ")
    slutord = input("Välj slutord: ")
    q.enqueue(startord)
    while not q.isEmpty():
        nod = q.dequeue()
        try:
            makeChildren(nod, q)
            if nod == slutord:
                raise Hittat
                print("Det finns ingen väg till", slutord)
        except Hittat:
            print("Det finns en väg till", slutord)
            break

if __name__ == '__main__':
    main()



