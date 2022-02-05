# 후보키 https://programmers.co.kr/learn/courses/30/lessons/42890

from collections import defaultdict
from itertools import combinations

def is_unique_key(target, relation):
    checker = defaultdict(int)
    for r in relation:
        key = ""
        for t in target:
            key += r[t]
        checker[hash(key)] += 1
    for c in checker.values():
        if c > 1:
            return False
    return True

def solution(relation):
    key_count = len(relation[0])
    unique_keys = list()
    for term in range(1, key_count+1):
        for c in combinations(range(key_count), term):
            if is_unique_key(c, relation):
                unique_keys.append(c)
    
    unique_keys_length = len(unique_keys)
    is_candidate_key = [True] * unique_keys_length
    
    for i in range(unique_keys_length):
        if not is_candidate_key[i]:
            continue
        cur = unique_keys[i]
        for j in range(i+1, unique_keys_length):
            if is_candidate_key[i] and all(c in unique_keys[j] for c in cur):
                is_candidate_key[j] = False
    return len([k for k in is_candidate_key if k])

