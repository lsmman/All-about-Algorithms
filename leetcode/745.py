"""
날짜 : 2021-05-15
문제 : 745. Prefix and Suffix Search
링크 : https://leetcode.com/problems/prefix-and-suffix-search/
"""

# Input
#     words = ["apple"]
#     prefix = "a"
#     suffix = "e"

#     obj = WordFilter(words)
#     output = obj.f(prefix,suffix)

# Output
#     0 // index of words, has prefix = "a" and suffix = "e"


"""
How solve?
    - word의 prefix, suffix 일치 여부를 체크해서 index 리턴
    - 단순하게 prefix, suffix 체크하면 word[:len(prefix)] == prefix and word[-len(suffix):] == suffix
    - prefix, suffix check가 반복적으로 일어나므로
        words를 O(length of word)로 search 할 수 있는 trie search를 사용한다.
    - N : word의 개수
    - K : word 중에 최대 길이
    - Q : prefix, suffix query 개수
    - 시간: O(NK^2 + QK)
    - 공간: O(NK^2)

How implement with python?
    - Python에서는 trie를 간단하게 Trie = lambda: collections.defaultdict(Trie)로 구현할 수 있다.
"""

import collections

Trie = lambda: collections.defaultdict(Trie)
INDEX = False


class WordFilter:
    def __init__(self, words: list):
        self.trie = Trie()

        for index, word in enumerate(words):
            """
            apple -> make trie
                - e#apple
                - le#apple
                - ple#apple
                - pple#apple
                - apple#apple
            """
            # cover suffix + # + prefix
            word = word + "#" + word
            word_len = len(word)

            for i in range(word_len):
                cur = self.trie
                cur[INDEX] = index

                for j in range(i, word_len):
                    cur = cur[word[j]]
                    cur[INDEX] = index

    def f(self, prefix: str, suffix: str) -> int:
        target = suffix + "#" + prefix
        cur = self.trie

        for t in target:
            if not t in cur:
                return -1
            cur = cur[t]
        return cur[INDEX]


# test example case
def test():
    words = ["apple"]
    prefix = "a"
    suffix = "e"

    obj = WordFilter(words)
    output = obj.f(prefix, suffix)
    assert output == 0


test()