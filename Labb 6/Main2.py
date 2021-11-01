def binary_search(list, key):
    Found = False
    First = 0
    Last = (len(list) - 1)
    while First <= Last and not Found:
        midpnt = (First + Last) // 2
        if list[midpnt] == key:
            Found = True
            return key
        else:
            if key > list[midpnt]:
                First = midpnt + 1
            else:
                Last = midpnt - 1
    if Found:
        return key
    else:
        return



def main():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main()

