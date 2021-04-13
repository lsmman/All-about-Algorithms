# T = int(input())
# for t in range(T):
#     X, Y, S = input().split()
#     cost = get_min_cost(int(X), int(Y), S)
#     print("Case #{}: {}".format(t+1, cost))

# 1
# import sys
# from itertools import product


# def get_copyright_cost(X_Y, word):
#     cost = [0, 0]
#     if not word:
#         return cost

#     preq = word[0]
#     for w in word:
#         if w == preq:
#             continue
#         if w == "C":
#             cost[1] += 1
#         else:  # w = 'J'
#             cost[0] += 1
#         preq = w
#     return cost[0] * X_Y[0] + cost[1] * X_Y[1]


# def get_min_cost(X, Y, S):
#     min_cost = int(sys.maxsize)
#     X_Y = [X, Y]
#     empty_count = S.count("?")
#     n = len(S)

#     for p in product(("C", "J"), repeat=empty_count):
#         filled_S = list(S)
#         j = 0
#         for i in range(n):
#             if filled_S[i] == "?":
#                 filled_S[i] = p[j]
#                 j += 1
#         cost = get_copyright_cost(X_Y, filled_S)
#         min_cost = min(min_cost, cost)

#     return min_cost


# print(get_min_cost(100, 1, "CJ?CC?"))


# # 2
# def get_min_cost(X, Y, S):
#     min_S = S.replace("?", "")
#     cost = min_S.count("CJ") * X + min_S.count("JC") * Y
#     return cost


# # 3


# def get_min_cost(X, Y, S):
#     if not S.count("?"):
#         return S.count("CJ") * X + S.count("JC") * Y

#     get_cost_by_list = lambda word: (word == ["C", "J"]) * X + (word == ["J", "C"]) * Y
#     S = list(S)
#     for i in range(len(S)):
#         if S[i] == "?":
#             S[i] = "C"
#             cost_C = get_cost_by_list(S[i - 1 : i + 1]) + get_cost_by_list(S[i : i + 2])
#             S[i] = "J"
#             cost_J = get_cost_by_list(S[i - 1 : i + 1]) + get_cost_by_list(S[i : i + 2])
#             S[i] = "C" if cost_C <= cost_J else "J"

#     S = "".join(S)
#     return S.count("CJ") * X + S.count("JC") * Y

# # 3 fail
# from itertools import product


# def get_min_cost(X, Y, S):
#     if not S.count("?"):
#         return S.count("CJ") * X + S.count("JC") * Y
#     div = []
#     i = 0
#     n = len(S)
#     while i < n - 1:
#         if S[i] == "?":
#             k = i
#             while k < n and S[k] == "?":
#                 k += 1
#             div.append(S[i : k + 1])
#             i = k
#         elif i + 1 < n and S[i + 1] == "?":
#             k = i + 1
#             while k < n and S[k] == "?":
#                 k += 1
#             div.append(S[i : k + 1])
#             i = k
#         else:
#             div.append(S[i : i + 2])
#             i = i + 1
#     print(div)

#     return 0


def get_min_cost(X, Y, S):
    def recursion(S, score):
        if len(S) < 2:
            return score
        elif S[0] == "?":
            return min(recursion("C" + S[1:], score), recursion("J" + S[1:], score))
        elif S[1] == "?":
            C = recursion(S[0] + "C" + S[2:], score)
            J = recursion(S[0] + "J" + S[2:], score)
            return min(C, J)
        elif S[0] == S[1]:
            return recursion(S[1:], score)
        elif S[0] == "C" and S[1] == "J":
            return recursion(S[1:], X + score)
        elif S[0] == "J" and S[1] == "C":
            return recursion(S[1:], Y + score)

    return recursion(S, 0)


def get_min_cost(X, Y, S):
    if not S.count("?"):
        return S.count("CJ") * X + S.count("JC") * Y
    n = len(S)
    S = list(S)
    i = k = 1
    div_S = []
    score = 0

    def recursion(S, score=0):
        if len(S) < 2:
            return score
        elif S[0] == "?":
            S[0] = "C"
            C = recursion(S, score)
            S[0] = "J"
            J = recursion(S, score)
            S[0] = "?"
            return min(C, J)
        elif S[1] == "?":
            S[1] = "C"
            C = recursion(S, score)
            S[1] = "J"
            J = recursion(S, score)
            S[1] = "?"
            return min(C, J)
        elif S[0] == S[1]:
            return recursion(S[1:], score)
        elif S[0] == "C" and S[1] == "J":
            return recursion(S[1:], X + score)
        elif S[0] == "J" and S[1] == "C":
            return recursion(S[1:], Y + score)
        return score

    while i < n:
        if S[i] == "?":
            k = i
            while k < n and S[k] == "?":
                k += 1
            div_S.append(S[i - 1 : k + 1])
            i = k + 1
        else:
            div_S.append(S[i - 1 : i + 1])
            i += 1

    for d in div_S:
        score += recursion(d)
    return score


# a = b = c = d = e = 0
# a = get_min_cost(2, 3, "CJ?CC?")
# b = get_min_cost(4, 2, "CJCJ")
# c = get_min_cost(1, 3, "C?J")
# d = get_min_cost(2, 5, "??J???")
# e = get_min_cost(2, -5, "??JJ??")
# print(a, b, c, d, e)


#!/usr/bin/env python3


# def main(x, y, s):
#     x = int(x)
#     y = int(y)

#     vc, vj = 0, 0
#     inf = int(1e9)
#     if s[0] == "C":
#         vj = inf
#     elif s[0] == "J":
#         vc = inf

#     for c in s[1:]:
#         if c == "C":
#             vc = min(vc, vj + y)
#             vj = inf
#         elif c == "J":
#             vj = min(vj, vc + x)
#             vc = inf
#         else:
#             vc, vj = min(vc, vj + y), min(vj, vc + x)

#     print(min(vc, vj))


def main(x, y, S):
    c, j = "C", "J"
    x, y = int(x), int(y)
    vc, vj = 0, 0
    inf = int(1e9)

    if S[0] == c:
        vj = inf
    elif S[0] == j:
        vc = inf
    for s in S[1:]:
        if s == c:
            vc = min(vc, vj + y)
            vj = inf
        elif s == j:
            vj = min(vj, vc + x)
            vc = inf
        else:
            vc = min(vc, vj + y)
            vj = min(vj, vc + x)
    return min(vc, vj)


x, y, s = 2, 3, "CJ?CC?"
print(main(x, y, s))
x, y, s = 4, 2, "CJCJ"
print(main(x, y, s))
x, y, s = 1, 3, "C?J"
print(main(x, y, s))
x, y, s = 2, 5, "??J???"
print(main(x, y, s))
x, y, s = 2, -5, "??JJ??"
print(main(x, y, s))