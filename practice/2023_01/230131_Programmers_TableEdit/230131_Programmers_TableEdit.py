class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.status = 'O'

def solution(n, k, cmd):
    table = [Node(i - 1, i + 1) for i in range(n)]
    table[0].left, table[n - 1].right = None, None
    history = []
    
    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c[2:])): k = table[k].left
            
        elif c[0] == 'D':
            for _ in range(int(c[2:])): k = table[k].right
            
        elif c[0] == 'C':
            history.append(k)
            table[k].status = 'X'
            
            l, r = table[k].left, table[k].right
            
            if l != None: table[l].right = r
            if r != None: table[r].left = l
            
            if not r: k = l
            else: k = r
            
        elif c[0] == 'Z':
            pos = history.pop()
            table[pos].status = 'O'
            
            l, r = table[pos].left, table[pos].right
            
            if l != None: table[l].right = pos
            if r != None: table[r].left = pos

    return ''.join([node.status for node in table])