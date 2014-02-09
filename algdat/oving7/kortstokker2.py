from sys import stdin as st
from itertools import repeat as rp

def pD(A):
    while len(A) > 1:
        A1 = A.pop(0)
        A2 = A.pop(0)
        res = []
        app = res.append
        ex = res.extend
        while len(A1) > 0 and len(A2) > 0:
            app((A1[0] < A2[0] and A1 or A2).pop(0))
        ex(A1), ex(A2)
        A.append(res)
    return ''.join([t[1] for t in A[0]])


#def merge(A1, A2):
#    res = []
#    ex = res.extend
#    while len(A1) > 0 and len(A2) > 0:
#        res.append((A1[0] < A2[0] and A1 or A2).pop(0))
#    ex(A1), ex(A2)
#    return res

if __name__ == "__main__":
    ds = []
    app = ds.append
    for l in st:
        (i, list) = l.split(':')
        d = zip(map(int, list.split(',')), rp(i))
        app(d)
    print pD(ds)
