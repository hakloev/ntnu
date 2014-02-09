from sys import stdin

def subgraftetthet(m, sn, n):
    e, v = 0, 0
    cv =  [False] *n #node som er mulig aa besoeke fra 
    cv[sn] = True #startnode kan besoekes
    q = [sn] #dfs
    app = q.append
    pop = q.pop
    while q:
        nr = pop(0)
        for nc in xrange(0, n):
            if (m[nr][nc]) and (not cv[nc]): # hvis kant og ikke besokt
                cv[nc] = True
                app(nc)
    for nr in xrange(0, n): #traverserer alle nextColr
        if (not cv[nr]): #er ikke besokt
            v += 1
            for nc in xrange(0, n): 
                if (m[nr][nc]) and (not cv[nc]): #kan besokes og er ikke besokt
                    e += 1
    return 0.0 if v == 0 else float(e) / float(v)**2 

def main():
    try: 
        nl = stdin.readline
        n = int(nl())
        mx = [None] * n # rader
        for i in xrange(0, n):
            mx[i] = [False] * n # kolonner
            li = nl()
            for j in xrange(0, n):
                mx[i][j] = (li[j] == '1')
        for l in stdin:
            stn = int(l)
            print "%.3f" % (subgraftetthet(mx, stn, n) + 1E-12)
    except:
        print "Dette gikk feil"

main()
