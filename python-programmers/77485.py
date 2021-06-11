# 행렬 테두리 회전하기
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/77485
# 문제 유형 : 구현, 2x2 matrix
# 문제 걸린 시간 : 36분

"""
문제 설명

x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.
행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때, 각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

"""


def solution(rows, columns, queries):
    answer = []
    # 문제 조건대로 MAP 생성
    # 예) rows, columns = 2, 3인 경우
    # [ [1, 2, 3]
    #   [4, 5, 6] ]
    MAP = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    min_init_val = rows * columns + 1  # MAP의 가장 큰 값 + 1

    for loc in queries:
        y1, x1, y2, x2 = list(map(lambda x: x - 1, loc))  # queries는 1부터 시작하기 때문에 -1
        preq = temp = MAP[y1][x1]
        min_val = min_init_val

        # x1, y1으로부터 x를 더해가며 visit = 오른쪽으로 이동하며 visit
        y = y1
        for x in range(x1, x2):
            temp = MAP[y][x]  # 현재 좌표의 값은 저장
            MAP[y][x] = preq  # 전 칸의 값은 현재 좌표의 값에 assign
            preq = temp
            min_val = min(temp, min_val)  # visit한 숫자 중 가장 작은 숫자

        # x2, y1으로부터 y를 더해가며 visit = 아래쪽으로 이동하며 visit
        x = x2
        for y in range(y1, y2):
            temp = MAP[y][x]  # 현재 좌표의 값은 저장
            MAP[y][x] = preq  # 전 칸의 값은 현재 좌표의 값에 assign
            preq = temp
            min_val = min(temp, min_val)

        # x2, y2으로부터 x를 빼가며 visit = 왼쪽으로 이동하며 visit
        y = y2
        for x in range(x2, x1, -1):
            temp = MAP[y][x]  # 현재 좌표의 값은 저장
            MAP[y][x] = preq  # 전 칸의 값은 현재 좌표의 값에 assign
            preq = temp
            min_val = min(temp, min_val)

        # x1, y2으로부터 y를 빼가며 visit = 위쪽으로 이동하며 visit
        x = x1
        for y in range(y2, y1 - 1, -1):
            temp = MAP[y][x]  # 현재 좌표의 값은 저장
            MAP[y][x] = preq  # 전 칸의 값은 현재 좌표의 값에 assign
            preq = temp
            min_val = min(temp, min_val)  # visit한 숫자 중 가장 작은 숫자

        answer.append(min_val)
    return answer