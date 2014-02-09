from sys import stdin

class Node:
    barn = None 
    r = None
    n = None # nivaa
    def __init__(self):
        self.barn = [] # liste med barne-noder
        self.r = False
        self.n = 0

def dfs(rot):
    noder = [rot] # legger rot-noden i stacken
    while noder: # saa lenge det er noder i stacken
        current = noder.pop() # ta ut oeverste node i stacken
        if current.r:
            return current.n
        for barn in current.barn: # legg til alle barn i stacken
            barn.n = current.n + 1 # oek barnets dybde med en  
            noder.append(barn) 

def bfs(rot):
    koe = [rot]
    while koe:
        current = koe.pop(0)
        if current.r:
            return current.n
        for barn in current.barn:
            barn.n = current.n + 1
            koe.append(barn)

def go():
    r = stdin.readlines()
    f = r.pop(0)
    n = [Node() for i in xrange(int(r.pop(0)))]
    s_n = n[int(r.pop(0))]
    r_n = n[int(r.pop(0))]
    r_n.r = True
    for linje in r:
        t = linje.split()
        t_n = n[int(t.pop(0))]
        app = t_n.barn.append
        for b_n in t:
            app(n[int(b_n)])
    print(bfs(s_n))

go()
