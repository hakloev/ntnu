from sys import stdin
from itertools import repeat

def printDeck(A):
    # SKRIV DIN KODE HER
    currMerged = A.pop(0)
    while A:
        A2 = A.pop(0)
        currMerged = merge(currMerged, A2)
    word = [tupple[1] for tupple in currMerged]
    return ''.join(word)
        

def merge(A1, A2):
    if len(A1) * len(A2) == 0: return A1 + A2
    return [(A1[0][0] < A2[0][0] and A1 or A2).pop(0)] + merge(A1, A2)

if __name__ == "__main__":
    decks = []
    app = decks.append
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        app(deck)
    print printDeck(decks)