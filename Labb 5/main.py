from bintreeFile import Bintree
from linkedQFile import LinkedQ
from ParentNode import ParentNode

svenska = Bintree()
gamla = Bintree()
q = LinkedQ()


def ordlista():
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # Ett trebokstavsord per rad
            svenska.put(ordet)  # in i sökträdet


# Version 2

def makeChildren_old(startord, q):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"  # definierar vilka tecken som existerar i alfabetet
    gamla.put(startord.word)  # lägger automatiskt in startord som ett dumbarn
    for bokstav in range(len(startord.word)):  # går igenom varje bokstav i starordet
        for tkn in alfabet:  # går igenom varje tecken i alfabetet
            nyttOrd = list(startord)  # gör om startordet till en lista där varje bokstav är ett element
            nyttOrd[bokstav] = tkn  # byter ut varje bokstav till varje tecken i alfabetet
            nyttOrd = "".join(nyttOrd)  # sätter ihop alla elementen i listan till en sträng och bildar det nya ordet
            if nyttOrd in svenska and nyttOrd not in gamla:
                gamla.put(nyttOrd)
                q.enqueue(nyttOrd)  # print(nyttOrd) i version 1 samt bort med parametern q


def makeChildren(startord, q):
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z å ä ö'.split()
    ord = list(startord.word)
    gamla.put(startord.word)
    for i in range(len(ord)):
        tmp_ord_list = ord[:]
        for j in range(len(letters)):
            tmp_ord_list[i] = letters[j]
            tmp_ord = ''.join(tmp_ord_list)
            if tmp_ord in svenska and not tmp_ord in gamla:
                q.enqueue(ParentNode(tmp_ord, startord))
                gamla.put(tmp_ord)


def main():
    ordlista()
    startord = input("Välj startord: ")
    slutord = input("Välj slutord: ")
    q.enqueue(ParentNode(startord))
    while not q.isEmpty():
        nod = q.dequeue()
        makeChildren(nod, q)
        if nod.word == slutord:
            nod.writechain()
            #print("Det finns en väg till", slutord)
            return
    print("Det finns ingen väg till", slutord)


if __name__ == '__main__':
    main()
