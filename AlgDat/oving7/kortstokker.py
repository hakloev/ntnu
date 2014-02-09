from sys import stdin
from itertools import repeat

def merge(A1, A2):
    # SKRIV DIN KODE HER
    if len(A1) * len(A2) == 0:
        return A1 + A2
    v = (A1[0][0] < A2[0][0] and A1 or A2).pop(0) # if A1[0] < A[2] pop A1[0], else pop A2[0] AND A[0][0] 'cause of the tuples inside the list
    return [v] + merge(A1, A2)

#def mergeSort(A):
#    n = len(A)
#    if n < 2:
#        return A
#    return merge(mergeSort(A[:n/2]), mergeSort(A[n/2:]))

def get(decks):
    merged = [decks.pop(0)]
    while decks:
        merged.append(merge(merged.pop(0), decks.pop(0)))
    s = ""
    for letter in merged[0]:
        s += letter[1]
    return s

if __name__ == "__main__":
    decks = []
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        decks.append(deck)
    #li = [1,6,8,3,9,5,0,3,5,7,2]    
    #print mergeSort(li)
    #print decks
    # [[(1, 'i'), (3, 'i'), (5, 'i'), (8, 'i')], [(2, 'n')], [(4, 't'), (7, 't')], [(6, 'a')], [(9, 'v')]]]
    print(get(decks))
