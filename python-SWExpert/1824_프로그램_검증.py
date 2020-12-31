import sys
from copy import deepcopy
from collections import deque


def n_arr(n, size, default=0):
    if n is 0:
        return default
    return [n_arr(n - 1, size, default) for _ in range(size[-n])]


def solution(r, c, commend):
    visit = n_arr(4, [r, c, 16, 4], default=False)
    di_idx = {"<": 0, ">": 1, "^": 2, "v": 3}
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([{"x": 0, "y": 0, "mem": 0, "di": 1}])
    while queue:
        cur = queue.popleft()
        cur_commend = commend[cur["y"]][cur["x"]]
        # print(cur, cur_commend, len(queue))
        if cur_commend == "@":
            return True
        elif visit[cur["y"]][cur["x"]][cur["mem"]][cur["di"]]:
            continue
        else:
            visit[cur["y"]][cur["x"]][cur["mem"]][cur["di"]] = True

        if cur_commend == "?":
            for di in range(4):
                cur_t = deepcopy(cur)
                cur_t["x"] = (cur_t["x"] + direct[di][0] + c) % c
                cur_t["y"] = (cur_t["y"] + direct[di][1] + r) % r
                cur_t["di"] = di
                queue.append(cur_t)
            continue
        elif cur_commend in ["<", ">", "^", "v"]:
            cur["di"] = di_idx[cur_commend]
        elif cur_commend == "_":
            cur["di"] = di_idx[">"] if cur["mem"] == 0 else di_idx["<"]
        elif cur_commend == "|":
            cur["di"] = di_idx["v"] if cur["mem"] == 0 else di_idx["^"]
        elif cur_commend == "+":
            cur["mem"] = (cur["mem"] + 1) % 16
        elif cur_commend == "-":
            cur["mem"] = (cur["mem"] + 15) % 16
        elif cur_commend >= "0" and cur_commend <= "9":
            cur["mem"] = int(cur_commend)
        # elif cur_commend == ".":
        #     pass

        cur["x"] = (cur["x"] + direct[cur["di"]][0] + c) % c
        cur["y"] = (cur["y"] + direct[cur["di"]][1] + r) % r
        queue.append(cur)

    return False


def main():
    sys.stdin = open("python-SWExpert/input.txt")

    T = int(input())
    for test_case in range(1, T + 1):
        r, c = map(int, input().split())
        commend = []
        for _ in range(r):
            commend.append(list(input()))
        ans = "YES" if solution(r, c, commend) else "NO"
        print("#{} {}".format(test_case, ans))


# def test():
#     whywhy = [36, 46, 47, 50, 52, 53, 54, 55, 58, 62, 69]
#     whywhy = [3, 28, 30, 31, 45, 50, 52, 62, 69]
#     whywhy = [69]
#     whywhy = [49, 57, 62]
#     sys.stdin = open("output.txt")
#     T = int(input())
#     answers = [""]
#     for test_case in range(1, T + 1):
#         answers.append(input().split()[1])
#     sys.stdin = open("python-SWExpert/input.txt")

#     T = int(input())
#     check = []
#     for test_case in range(1, T + 1):
#         r, c = map(int, input().split())
#         commend = []
#         for _ in range(r):
#             commend.append(list(input()))
#         # if test_case in whywhy:
#         #     print(r, c)
#         #     for asdf in commend:
#         #         print(asdf)
#         ans = "YES" if solution(r, c, commend) else "NO"
#         print("#{} {} {}".format(test_case, ans, ans == answers[test_case]))
#         if not ans == answers[test_case]:
#             check.append(test_case)
#     print(check)


if __name__ == "__main__":
    # test()
    main()