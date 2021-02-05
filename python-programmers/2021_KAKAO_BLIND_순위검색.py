from collections import defaultdict
import bisect


def solution(info, queries):
    ans = [0] * len(queries)
    sets = defaultdict(list)
    for ele in info:
        *cur, score = ele.split()
        for k in range(16):
            key = ""
            for sift in range(4):
                if k & (1 << sift):
                    key += "-"
                else:
                    key += cur[sift][:2]
            bisect.insort(sets[key], int(score))

    for q_i, query in enumerate(queries):
        *cur_q, q_score = query.split()
        key = ""
        for c in cur_q:
            if c != "and":
                key += c[:2]
        ans[q_i] = len(sets[key]) - bisect.bisect_left(sets[key], int(q_score))
    return ans