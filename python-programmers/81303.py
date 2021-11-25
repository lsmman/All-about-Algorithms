# 2021 카카오 채용연계 인턴쉽

C, D, U, Z = ["C", "D", "U", "Z"]


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
    def __repr__(self):
        return str(self.data)

def up(cursor, move):
    moved = 0
    while cursor.prev and moved < move:
        cursor = cursor.prev
        moved += 1
    return cursor

def down(cursor, move):
    moved = 0
    while cursor.next and moved < move:
        cursor = cursor.next
        moved += 1
    return cursor

def cancel(cursor):
    next_cursor = cursor.next
    if not cursor.next:
        next_cursor = cursor.prev
        
    if cursor.prev:
        cursor.prev.next = cursor.next
    if cursor.next:
        cursor.next.prev = cursor.prev
    cursor.prev = None
    cursor.next = None
    
    return next_cursor

def insert_after(target, before):
    after = before.next
    
    target.prev = before
    target.next = after
    
    before.next = target
    
    if after:
        after.prev = target
    
def solution(n, k, cmds):
    answer = ["O"] * n
    cursor = None
    last_cancels = []
    root = Node(-1)
    last = root
    
    for data in range(n):
        cur = Node(data)
        
        if data == k:
            cursor = cur
            
        last.next = cur
        cur.prev = last
        last = cur
        
    for cmd in cmds:
        if not cmd:
            continue
            
        if cmd[0] == C:
            answer[cursor.data] = 'X'
            last_cancels.append([cursor.prev, cursor])
            cursor = cancel(cursor)
        
        elif cmd[0] == U:
            move = int(cmd.split()[1])
            cursor = up(cursor, move)
        
        elif cmd[0] == D:
            move = int(cmd.split()[1])
            
            cursor = down(cursor, move)
        
        elif cmd[0] == Z:
            if not last_cancels:
                continue
            last_prev, last_cancel = last_cancels.pop()
            answer[last_cancel.data] = 'O'
            insert_after(last_cancel, last_prev)
    
    return "".join(answer)