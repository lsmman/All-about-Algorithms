# class action:
#     def __init__(self, d, o, t):
#         self.d = d
#         self.o = int(o)
#         self.t = int(t)
#     def __repr__(self):
#         if self.d is 'A':
#             return "노드 {}를/을 노드 {}의 앞으로 이동".format(self.o, self.t)
#         elif self.d is 'B':
#             return "노드 {}를/을 노드 {}의 뒤로 이동".format(self.o, self.t)
#         else :
#             return "wrong_action"

# class Node:
#     def __init__(self, prev=None, nex=None, val=-1):
#         self.prev = prev
#         self.next = nex
#         self.val = val
#     def __str__(self):
#         return str(self.val)

# class dLlist:
#     def __init__(self, num_of_node):
#         self.set_dList(num_of_node)

#     def set_dList(self, num_of_node):
#         self.start = Node()
#         # self.end = Node()
#         now = self.start

#         for i in range(1, num_of_node+1):
#             new = Node(val=i)
#             self.set_relation(now, new)
#             now = new

#         # self.set_relation(now, self.end)

#     def set_relation(self, front, back):
#         front.next = back
#         back.prev = front
    
#     def __repr__(self):
#         nex = self.start.next
#         while nex:
#             print(nex)
#             nex = nex.next

#     def __str__(self):
#         val_list = []
#         nex = self.start.next
#         while nex:
#             val_list.append(nex.val)
#             nex = nex.next
#         return ' -> '.join(list(map(str, val_list)))

# if __name__ == "__main__":
#     action_list = []
#     num_of_node, num_of_action = map(int, input().split())
#     for i in range(num_of_action):
#         inputs = input().split()
#         action_list.append(action(inputs[0], inputs[1], inputs[2]))
    

if __name__ == "__main__":
        pass