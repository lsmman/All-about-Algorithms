from collections import defaultdict
from bisect import insort, bisect_left


def solution(info, queries):
    ans = []
    sets = defaultdict(list)
    for _info in info:
        *data, score = _info.split()
        for k in range(16):
            key = ""
            for sift in range(4):
                if k & (1 << sift):
                    key += "-"
                else:
                    key += data[sift][0]
            insort(sets[key], int(score))

    for q in queries:
        *cur_q, q_score = q.split()
        key = ""
        for c in cur_q:
            if c != "and":
                key += c[0]
        count = len(sets[key]) - bisect_left(sets[key], int(q_score))
        ans.append(count)
    return ans


# https://velog.io/@study-dev347/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89
# https://lioliolio.github.io/python-bisect-module/