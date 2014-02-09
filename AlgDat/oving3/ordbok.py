from sys import stdin

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

# Add comments to bygg() and position()
def bygg(ordliste):
    rot = Node()
    for ord, pos in ordliste:
        node = rot
        for bokstav in ord:
            if bokstav not in node.barn:
                node.barn[bokstav] = Node()
            node = node.barn[bokstav]
        node.posi.append(pos)
    return rot

def position(ord, index, node):
    if index == len(ord):
        return node.posi
    elif ord[index] == '?':
        posi = []
        for bokstav in node.barn:
            posi += (position(ord, index + 1, node.barn[bokstav]))
        return posi
    elif ord[index] not in node.barn:
        return []
    else:
        return position(ord, index + 1, node.barn[ord[indeks]])

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        app = ordliste.append
        for o in ord:
            app( (o,pos) )
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print sokeord + ":",
            posi = position(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print p,
            print
    except:
            print "Gikk feil detta"
main()
