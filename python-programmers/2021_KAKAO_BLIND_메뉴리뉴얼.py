from collections import defaultdict


def solution(orders, course):
    ans = []
    max_c = max(course)
    menus = [defaultdict(set) for _ in range(max_c + 1)]
    for idx, order in enumerate(orders):
        for o in order:
            menus[1][o].add(idx)
    for c in range(2, max_c + 1):
        one, other = menus[1], menus[c - 1]
        for other_key in other.keys():
            for one_key in one.keys():
                if len(set(other_key + one_key)) != c:
                    continue
                new_key = "".join(sorted(other_key + one_key))
                new_set = other[other_key] & one[one_key]
                if len(new_set) >= 2:
                    menus[c][new_key] = new_set
    for c in course:
        if menus[c]:
            max_leng = max([len(v) for v in menus[c].values()])
            for k, v in menus[c].items():
                if len(v) == max_leng:
                    ans.append(k)
    return sorted(ans)