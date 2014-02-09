from sys import stdin, stderr

def extractMax(Q, v):
    highestProb = 0 # Init with 0
    bestNode = None # Init with None
    for node in Q: # For all nodes in Q
        if v[node] > highestProb: # If current vertex sum is higher than previous
            highestProb = v[node] # Set highest to current
            bestNode = node # Save index to return it
    return bestNode # NoneType or index

def dijkstra(Q, s):
    n = len(Q) # Used many times, good to have local variable
    S = [i for i in xrange(n)] # Set to see nodes left
    parent = [None] * n # Keep track of parent node in path, initial node will always be None
    vertexSums = [0.0] * n # Keep the vertex-sums in a list
    vertexSums[0] = s[0] # Init first node to its probability
    # Start Dijkstra
    while S: # As long as nodes
        u = extractMax(S, vertexSums) # Get the index of the node with highest probability
        if u == None: break # If no good node (NoneType) skip to next iteration
        S.remove(u) # Remove checked vertex from set of vertexes
        for node in S: # For each node in S, that is not visited
            # Start relax vertex
            if Q[u][node]:
                if vertexSums[node] < (vertexSums[u] * s[node]):
                    vertexSums[node] = (vertexSums[u] * s[node])
                    parent[node] = u
            # End relax
    # End Dijkstra
    # Print path
    if parent[-1] == None: # If no parent for last node
        return '0'
    v = parent[-1] 
    path = [n - 1]
    while True:
        if v == None:
            break
        path.append(v)
        v = parent[v]
    path.reverse()
    return '-'.join(str(node) for node in path)
    
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
    print dijkstra(nabomatrise, sansynligheter)
