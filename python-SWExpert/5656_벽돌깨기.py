"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 30초 / C++의 경우 30초 / Java의 경우 30초 / Python의 경우 30초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys


def break_block(blocks, checker, W, H):
    new_b = [[0 for _ in range(W)] for _ in range(H)]
    for j in range(W):
        delay = 0
        for i in range(H - 1, -1, -1):
            if not checker[i][j]:
                new_b[i + delay][j] = blocks[i][j]
            else:
                delay += 1
    return new_b


def boom(w, h, b, checker, W, H):
    if w < 0 or w >= W or h < 0 or h >= H:
        return
    if checker[h][w] or b[h][w] == 0:
        return
    checker[h][w] = True
    if b[h][w] > 1:
        for term in range(1, b[h][w]):
            boom(w, h - term, b, checker, W, H)
            boom(w, h + term, b, checker, W, H)
            boom(w - term, h, b, checker, W, H)
            boom(w + term, h, b, checker, W, H)
    return


def _solution(N, W, H, blocks, counts):
    if not N:
        count = 0
        for b in blocks:
            count += W - b.count(0)
        counts.add(count)
        return

    for w in range(W):
        checker = [[False for _ in range(W)] for __ in range(H)]
        start_h = 0
        while start_h < H and not blocks[start_h][w]:
            start_h += 1
        boom(w, start_h, blocks, checker, W, H)
        new_b = break_block(blocks, checker, W, H)
        _solution(N - 1, W, H, new_b, counts)


def solution(N, W, H, blocks):
    counts = set()
    _solution(N, W, H, blocks, counts)
    return min(counts)


def main():
    sys.stdin = open("python-SWExpert\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        N, W, H = map(int, input().split())
        blocks = []
        for _ in range(H):
            blocks.append(list(map(int, input().split())))
        ans = solution(N, W, H, blocks)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()
    # test()

# 1 12
# 2 27
# 3 4
# 4 8
# 5 0

# def test():
# solution(
#     3,
#     10,
#     10,
#     [
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#         [1, 0, 3, 0, 1, 1, 0, 0, 0, 1],
#         [1, 1, 1, 0, 1, 2, 0, 0, 0, 9],
#         [1, 1, 4, 0, 1, 1, 0, 0, 1, 1],
#         [1, 1, 4, 1, 1, 1, 2, 1, 1, 1],
#         [1, 1, 5, 1, 1, 1, 1, 2, 1, 1],
#         [1, 1, 6, 1, 1, 1, 1, 1, 2, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
#         [1, 1, 7, 1, 1, 1, 1, 1, 1, 1],
#     ],
# )
