import sys


def solution(r, c, commend):
    visit = [[False for i in range(c)] for _ in range(r)]
    direct = {"<": (-1, 0), ">": (1, 0), "^": (0, 1), "v": (0, -1)}
    cur_info = {"x": 0, "y": 0, "mem": 0, "di": direct[">"]}  # x, y, mem, di
    visit[0][0] = True

    # while True:
"""
_	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
|	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.
.	아무 것도 하지 않는다.
@	프로그램의 실행을 정지한다.
0~9	메모리에 문자가 나타내는 값을 저장한다.
+	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
-	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다.
"""
    return 0


def main():
    sys.stdin = open("python-SWExpert/input.txt")

    T = int(input())
    for test_case in range(1, T + 1):
        r, c = map(int, input().split())
        commend = []
        for _ in range(r):
            commend.append(list(input()))
        ans = solution(r, c, commend)
        print("#{} {}".format(test_case, ans))
        break


if __name__ == "__main__":
    main()
