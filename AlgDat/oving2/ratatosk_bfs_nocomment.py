from sys import stdin
from collections import deque

True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None 
    def __init__(self):
        self.barn = [] 
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
    if rot.ratatosk:
        return 0
    noder = [rot] 
    while (len(noder) > 0): 
        current = noder.pop() 
        for barn in current.barn:
            noder.append(barn) 
            barn.nesteBarn = current.nesteBarn + 1  
            if barn.ratatosk: 
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
    print (bfs(start_node))
