from sys import stdin, stderr

class Vertex():
    prob = None
    pred = None
    number = None
    dist = 0
    
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return repr(self.number)

class Pri_Q():
    
    q = []

    def __init__(self, nodes):
        self.q = list(nodes)

    def __len__(self):
        return len(self.q)

    def extract_max(self):
        (_, index) = max((x.dist, i) for i,x in enumerate(self.q))
        return self.q.pop(index)

def relax(u, v):
    if v.dist < (u.dist * v.prob):
        v.dist = (u.dist * v.prob)
        v.pred = u 

def beste_sti(Adj, V ):
    V[0].dist = V[0].prob
    Q = Pri_Q(V)
    while Q:
        u = Q.extract_max()
        for Vert, nabo in enumerate(Adj[u.number]):
            if nabo:
                v = V[Vert]
                relax(u, v)
    # returner stien 
    last = V[-1]
    sti = [last]
    while v.pred:
        v = v.pred
        sti.append(v)
    if sti[-1] == 0.0:
        return '0'
    else:
        sti.reverse()
        return '-'.join(str(node) for node in sti)
            
if __name__ == "__main__":
    n = int(stdin.readline())
    Vert = [Vertex(i) for i in xrange(n)]
    for node, prob in enumerate(stdin.readline().split()):
        Vert[node].prob = float(prob)
    nabomatrise = []
    for linje in stdin:
        rad = [0] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for nabo in naboer:
            rad[nabo] = 1
        nabomatrise.append(rad)
    print beste_sti(nabomatrise, Vert)
