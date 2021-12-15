from math import sqrt

def main():
    #Antal noder som behövs
    N = int(input())

    #Skapar en tom hashtabell
    nodes = {}
    #Skapar varje nod och stoppar in den i hashtabellen
    #Nyckeln är ID för varje nod, värdena är huvud(ovanstående nod), flow(andel vatten som flödar igenom), power (om det är en supernod)
    for n in range(N-1):
        #Ai, Bi, Xi, T
        head, ID, flow, power = input().split()
        nodes[int(ID)] = (int(head), float(flow)/100, bool(int(power)))
    #Hur vatten varje nod ska ha
    outflows = [int(x) for x in input().split()]
    result = 0
    index = 0
    for required in outflows: #Itererar genom varje varje nod
        index += 1
        if required == -1: #Inget löv, hoppar vidare
            continue
        current = index
        #Beräknar baklänges hur mycket vatten som behövs.
        while current != 1:
            current, flow, power = nodes[current]
            if power:
                required = sqrt(required)
            required /= flow
        #Returnerar det största värdet
        if required > result:
            result = required
    print(result)

if __name__ == '__main__':
    main()
