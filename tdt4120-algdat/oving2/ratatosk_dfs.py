from sys import stdin
from collections import deque

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = [] # liste med barne-noder
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
    if rot.ratatosk: # hvis ratatosk er paa rot-noden
        return 0
    noder = [rot] # legger rot-noden i stacken
    while noder: # saa lenge det er noder i stacken
        current = noder.pop() # ta ut oeverste node i stacken
        for barn in current.barn: # legg til alle barn i stacken
            noder.append(barn) 
            barn.nesteBarn = current.nesteBarn + 1 # oek barnets dybde med en i forhold til foreldre noden 
            if barn.ratatosk: # er barne-noden ratatosk, returner dybden til noden
                return barn.nesteBarn

def bfs(rot):
   if rot.ratatosk:
        return 0
   koe = deque([rot])
   while (len(koe) > 0):
        current = koe.popleft()
        for barn in current.barn:
            koe.append(barn)
            barn.nesteBarn = current.nesteBarn + 1
            if barn.ratatosk:
                return barn.nesteBarn
       
funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    # SKRIV DIN KODE HER
    print (dfs(start_node))
