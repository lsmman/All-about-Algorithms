from collections import defaultdict, deque


class Trie:
    def __init__(self):
        self.trie = defaultdict(Trie)
        self.end = -1
        self.parent = None

    def add(self, char):
        self.trie[char].setParent(self)
        return self.trie[char]

    def add_end(self, index):
        self.end = index

    def setParent(self, parent):
        self.parent = parent

    def get_end(self):
        return self.end

    def is_end(self):
        return self.end != -1

    def search(self, char):
        if char in self.trie:
            return (True, self.trie[char])
        return (False, None)

    def has_child(self):
        return bool(self.trie)

    def get_all_child(self):
        return self.trie.values()

    def __repr__(self):
        if not self.has_child():
            return ""
        return_string = "{"
        for k, v in self.trie.items():
            return_string += k + " " + v.__repr__() + ", "
        return_string += "}"
        return return_string

def solution(user_id, banned_id):
    root = Trie()
    wildcard = '*'
    candidators = []

    for index, u in enumerate(user_id):
        cur = root
        for char in u:
            cur = cur.add(char)
        cur.add_end(index)

    for b in banned_id:
        candidate = deque([root])
        for char in b:
            length = len(candidate)
            while length:
                length -= 1
                cur = candidate.popleft()
                if not cur.has_child():
                    continue

                if char == wildcard:
                    candidate.extend(cur.get_all_child())
                    continue

                exist, next_ = cur.search(char)
                if not exist:
                    continue
                candidate.append(next_)
        candidator = [c.get_end() for c in candidate if c.is_end()]
        if not candidator:
            return 0
        candidators.append(candidator)

    answers = set()

    def bfs(index, cur):
        if index < 0:
            answers.add(tuple(sorted(cur)))
            return
        for c in candidators[index]:
            if c in cur:
                continue
            bfs(index-1, cur+[c])

    bfs(len(candidators)-1, [])
    return len(answers)