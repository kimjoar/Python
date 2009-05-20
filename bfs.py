from sys import stdin

True = 1
False = 0

White = 0
Gray = 1
Black = 2

class Node:
    color = White
    dist = None
    parent = None
    children = None
    def __init__(self):
        self.children = []

def bfs(rot):
    rot.color = Gray
    rot.dist = 0
    rot.parent = None
    queue = []
    queue.append(rot)

    while queue:
        u = queue.pop(0)
        print u
        for v in u.children:
            if v.color == White:
                v.color = Gray
                v.dist = u.dist + 1
                v.parent = u
                queue.append(v)
        u.color = Black
    return None

antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.children.append(noder[int(barn_nr)])
print bfs(start_node)