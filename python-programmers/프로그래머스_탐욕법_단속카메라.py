# 정말 간단
# 시간 효율도 O(n)
# 공간 효율도 O(n) routes 그대로
# 다음부터 생각을 좀 더 하고 풀자

def solution(routes):
    routes.sort(key=lambda x:x[1])
    lastTime = -30001
    answer = 0

    for srt, end in routes:
        if lastTime < srt:
            answer += 1
            lastTime = end
    return answer

"""
# 포인트마다 들어오고 나가는 걸 표시한 dict을 만들어서
# 나갈 때마다 차량이 카메라를 만났는지 체크
# 안만났다면 그 시점에 있는 모든 카메라 ok
# 시간 복잡도 O(n) -> 4n 정도
# 공간 복잡도 O(n)+a

import copy
from collections import defaultdict

def solution(routes):
    stop = 0
    d_list = [[], []]
    save = defaultdict(lambda: copy.deepcopy(d_list))
    for i, (srt, end) in enumerate(routes):
        save[srt][0].append(i)
        save[end][1].append(i)
    keys = sorted(save.keys())
    working = []
    check = [False] * len(routes)

    for key in keys:
        srts, ends = save[key]
        for s in srts:
            working.append(s)

        for e in ends:
            if not check[e]:
                stop += 1
                for w in working:
                    check[w] = True
            working.remove(e)



    return stop
"""