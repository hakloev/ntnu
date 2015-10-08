inf = float('inf')

def floyd(W):
    n = len(W)
    D = [W]
    for k in range(1, n):
        if (k != 0):
            D.append([[0 for x in range(n)] for y in range(n)])
        for i in range(n):
            for j in range(n):
                D[k][i][j] = min(D[k - 1][i][j], (D[k -1][i][k] + D[k -1][k][j]))
    return D

if __name__ == "__main__":
    W = [[0, inf, inf, inf, -1, inf],
         [1, 0, inf, 2, inf, inf],
         [inf, 2, 0, inf, inf, -8],
         [-4, inf, inf, 0, 3, inf],
         [inf, 7, inf, inf, 0, inf],
         [inf, 5, 10, inf, inf, 0]]
    RES = floyd(W)
    for D in RES:
        for row in D:
            print row
        print 'new D   ------'
