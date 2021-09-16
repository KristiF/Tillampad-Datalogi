from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ")
        else:
            svenska.put(ordet)             # in i sökträdet

engelska = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for rad in engelskfil:
        for ordet in rad.split():
            if ordet in engelska:
                pass
            elif ordet in svenska:
                engelska.put(ordet)
                print(ordet, end=" ")

print("\n")