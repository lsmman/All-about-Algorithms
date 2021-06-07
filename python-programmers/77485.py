# 행렬 테두리 회전하기
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3
# 문제 걸린 시간 : 36분


def solution(rows, columns, queries):
    answer = []
    MAP = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]

    for loc in queries:
        y1, x1, y2, x2 = list(map(lambda x: x - 1, loc))
        temp = preq = MAP[y1][x1]
        min_val = rows * columns + 1

        y = y1
        for x in range(x1, x2):
            temp = preq
            preq = MAP[y][x]
            MAP[y][x] = temp
            min_val = min(preq, min_val)

        x = x2
        for y in range(y1, y2):
            temp = preq
            preq = MAP[y][x]
            MAP[y][x] = temp
            min_val = min(preq, min_val)

        y = y2
        for x in range(x2, x1, -1):
            temp = preq
            preq = MAP[y][x]
            MAP[y][x] = temp
            min_val = min(preq, min_val)

        x = x1
        for y in range(y2, y1 - 1, -1):
            temp = preq
            preq = MAP[y][x]
            MAP[y][x] = temp
            min_val = min(preq, min_val)

        answer.append(min_val)
    return answer