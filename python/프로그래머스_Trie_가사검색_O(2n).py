class w_node:
    def __init__(self, val):
        self.val = val
        self.voca_data = {}
        self.child = {}
    
    def add_length_of_vaca_data(self, leng):
        if leng in self.voca_data:
            self.voca_data[leng] += 1
        else:
            self.voca_data[leng] = 1
    
class Trie:
    def __init__(self):
        self.root = w_node("")
        
    def push(self, word):
        parent = self.root
        for w in word:
            if w in parent.child:
                cur = parent.child[w]
            else:
                cur = w_node(w)
                parent.child[w] = cur
            cur.add_length_of_vaca_data(len(word))
            parent = cur

    def get_word_count(self, query_word):
        prev = self.root
        question = '?'
        leng = len(query_word)
        
        for q in query_word:
            if q == question:
                break
            if q in prev.child:
                cur = prev.child[q]
            else:
                return 0
            prev = cur
        
        if leng in cur.voca_data:
            return cur.voca_data[leng]
        else:
            return 0

def solution(words, queries):
    result = []
    question = '?'
    prefix_trie, suffix_trie = Trie(), Trie()
    for word in words:
        prefix_trie.push(word)
        suffix_trie.push(word[::-1])
    
    for query in queries:
        leng = len(query)
        if query[0] is question:
            cnt = suffix_trie.get_word_count(query[::-1])
        else:
            cnt = prefix_trie.get_word_count(query)
        result.append(cnt)
        
    return result


### version2

# class w_node:
#     def __init__(self, val):
#         self.val = val
#         self.voca_data = []
#         self.child = []
        
# #     def __str__(self):
# #         return "[val:{}, voca_data:{}, num_of_child:{}]".format( \
# #                 self.val, self.voca_data, len(self.child))
    
#     def search_child(self, char):
#         for node in self.child:
#             if node.val is char:
#                 return node
#         return None
    
#     def add_length_of_vaca_data(self, leng):
#         self.voca_data.append(leng)
    
# def create_Trie(words, reverse=False):
#     root = w_node("")
#     for word in words:
#         parent = root
#         if reverse:
#             word = word[::-1]
#         for w in word:
#             cur = parent.search_child(w)
#             if cur is None:
#                 cur = w_node(w)
#                 parent.child.append(cur)
#             cur.add_length_of_vaca_data(len(word))
#             parent = cur
#         cur.end_check = True
#     return root

# def search_Trie(query_word, trie):
#     prev = trie
#     question = '?'
#     for q in query_word:
#         if q is question:
#             break
#         cur = prev.search_child(q)
#         if cur is None:
#             return None
#         prev = cur
#     return cur

# def solution(words, queries):
#     result = []
#     question = '?'
#     root = create_Trie(words)
#     root_r = create_Trie(words, reverse=True)
    
#     for query in queries:
#         leng = len(query)
#         cnt = 0
#         if query[0] is question:
#             cur = search_Trie(query[::-1], root_r)
#         else:
#             cur = search_Trie(query, root)
            
#         if not cur is None:
#             for data in cur.voca_data:
#                 if data == leng:
#                     cnt += 1
#         result.append(cnt)
        
#     return result