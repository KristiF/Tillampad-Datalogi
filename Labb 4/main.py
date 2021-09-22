from bintreeFile import Bintree

svenska = Bintree()
gamla = Bintree()

def ordlista():
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # Ett trebokstavsord per rad
            svenska.put(ordet)  # in i sökträdet

#startord = input("Mata in startord: ")

def makeChildren(startord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö" # definierar vilka tecken som existerar i alfabetet
    gamla.put(startord) # lägger automatiskt in startord som ett dumbarn
    for bokstav in range(len(startord)): # går igenom varje bokstav i starordet
        for tkn in alfabet:  # går igenom varje tecken i alfabetet
            nyttOrd = list(startord) # gör om startordet till en lista där varje bokstav är ett element
            nyttOrd[bokstav] = tkn #byter ut varje bokstav till varje tecken i alfabetet
            nyttOrd = "".join(nyttOrd) # sätter ihop alla elementen i listan till en sträng och bildar det nya ordet
            if nyttOrd in svenska and nyttOrd not in gamla:
                gamla.put(nyttOrd)
                print(nyttOrd)

def main():
    ordlista()
    startord = input("Mata in startord: ")
    slutord = input("Mata in slutord: ")
    makeChildren(startord)

if __name__ == '__main__':
    main()



