from sys import stdin, maxint

Inf = float(1e3000)

def korteste_rute(rekkefolge, nabomatrise, byer):
    rekkefolge.append(rekkefolge[0]) # Add first city to end, must always return
    cost = 0 # Init cost
    for city in xrange(len(rekkefolge) - 1): # How many cities we must visit
        cityCost = nabomatrise[rekkefolge[city]][rekkefolge[city + 1]] # Cost of path from current city to next city
        if cityCost == Inf: # If stepCost is Inf, we have no path between the cities
            return 'umulig'
        cost += cityCost # Add cost to total cost
    return cost

def floydW(A): # Floyd Warshalls algorithm
    n = len(A) 
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                A[i][j] = min(A[i][j], (A[i][k] + A[k][j]))
    return A

if __name__ == "__main__":
    for test in xrange(int(stdin.readline())):
        byer = int(stdin.readline())
        rekkefolge = [int(by) for by in stdin.readline().split()]
        nabomatrise = []
        app = nabomatrise.append
        for city in xrange(byer): # Once for each city in input
            row = [int(cost) for cost in stdin.readline().split()] # Row with cost to each city from given city
            for nextCity in xrange(byer): # Next town in row 
                if row[nextCity] == -1: # If edge is -1, there is no path
                    row[nextCity] = Inf
            app(row) 
        print korteste_rute(rekkefolge, floydW(nabomatrise), byer)
