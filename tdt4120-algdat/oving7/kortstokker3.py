from sys import stdin
from itertools import repeat

if __name__ == "__main__":
    decks = {}
    for line in stdin:
        (index, list) = line.split(':')
        decks.update(zip(map(int, list.split(',')), repeat(index)))
    decks.update()
    print ''.join(decks.values())
