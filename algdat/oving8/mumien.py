from sys import stdin, stderr

def extractBestSan(Q, v):
    m = 0
    index = -1
    for vertex in xrange(0, len(Q)):
        if (Q[vertex] > m) and (v[vertex] != 1):
            m = Q[vertex]
            index = vertex
    return index

def beste_sti(nm, sans):
    dist = [-1] * len(nm)
    dist[0] = sans[0]
    Q = nm
    pred = [None] * len(sans)
    visited = [0] * len(sans)
    count = 0
    while Q:
        uIndex = extractBestSan(dist, visited)
        u = Q[uIndex]
        for vertex in xrange(0, len(u)): 
            if (u[vertex] != 0) and (visited[vertex] != 1):
                if dist[vertex] < (sans[uIndex] * sans[vertex]):
                    dist[vertex] = (sans[uIndex] * sans[vertex])
                    pred[vertex] = uIndex
        visited[uIndex] = 1
        count += 1
    return path(len(sans) - 1, pred)
    
def path(node, pre):
    if pre[node] == None:
        return str(0)
    return path(pre[node], pre) + "-" + str(node)

            
if __name__ == "__main__":
    n = int(stdin.readline())
    sansynligheter = [float(x) for x in stdin.readline().split()]
    nabomatrise = []
    for linje in stdin:
        naborad = [0] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
    print beste_sti(nabomatrise, sansynligheter)
