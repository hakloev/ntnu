from sys import stdin

Inf = float(1e3000)
#False = 0
#True = 1

def mst(nm):
    # SKRIV DIN KODE HER
    n = len(nm) 
    tre = [0]
    ikkeTre = range(1, n)
    kanter = []
    while ikkeTre:
        minste = Inf
        hvilken = []
        for node in tre:
            for neste in ikkeTre:
                if nm[node][neste] < minste:
                    minste = nm[node][neste]
                    hvilken = [neste, node]
        tre.append(hvilken[0])
        ikkeTre.remove(hvilken[0])
        kanter.append(nm[hvilken[1]][hvilken[0]])
    print max(kanter)
    # SLUTT EGEN KODE

def main():
    linjer = [str for str in stdin]
    n = len(linjer)
    nabomatrise = [None] * n
    node = 0
    for linje in linjer:
        nabomatrise[node] = [Inf] * n
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            nabomatrise[node][nabo] = vekt
        node += 1
    mst(nabomatrise)

main()