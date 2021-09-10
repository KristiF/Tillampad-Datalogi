#from ArrayQ import ArrayQ
from linkedQFile import LinkedQ


def doMagic(cards):

    #card_deck = ArrayQ() # korthögen (en array)
    card_deck = LinkedQ() # korthögen (en länkad lista)
    table = [] # bordet där korten läggs ut
    for card in cards:
        card_deck.enqueue(card) # lägger in korten i ett kösystem i LinkedQ eller ArrayQ

    while not card_deck.isEmpty(): # ifall korthögen inte är om
        card_deck.enqueue(card_deck.dequeue()) # ta bort kortet längst fram i "kön" och lägg till det i slutet av "kön"
        table.append(card_deck.dequeue()) # ta bort kortet som var bakom kortet som var längst fram och lägg det på bordet
    return table


if __name__ == "__main__":
    table = doMagic(input().split())
    for card in table: # går igenom alla kort på bordet och printar ut dem på rad
        print(card, end=' ')