#from ArrayQ import ArrayQ
from linkedQFile import LinkedQ


def doMagic(cards):

    #card_deck = ArrayQ()
    card_deck = LinkedQ()
    table = []
    for card in cards:
        card_deck.enqueue(card)

    while not card_deck.isEmpty():
        card_deck.enqueue(card_deck.dequeue())
        table.append(card_deck.dequeue())
    return table


if __name__ == "__main__":
    table = doMagic(input().split())
    for card in table:
        print(card, end=' ')