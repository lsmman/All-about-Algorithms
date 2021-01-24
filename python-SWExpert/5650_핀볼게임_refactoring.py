"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""
# 버전 3
# 메모리 63728 KB, 541 ms
# 바운더리 체크 줄이고, visit 제거한 버전 (이 경우, visit의 cache hit 효과를 기대했는데 크지 않았던 듯)

from collections import defaultdict
import sys

sys.stdin = open("python-SWExpert\\input.txt", "r")


x, y, di = (0, 1, 2)
# left 0, right 1, up 2, down 3
direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
change_direction = [
    0,
    [2, 0, 3, 1],
    [3, 0, 1, 2],
    [1, 3, 0, 2],
    [1, 2, 3, 0],
    [1, 0, 3, 2],
]


# def calculate(ball, N, MAP, wormholes):


def solution(N, not_expanded_MAP):
    route_score = 0
    wormholes = [[] for _ in range(11)]
    MAP = []
    MAP = [[5] + M + [5] for M in not_expanded_MAP]
    MAP.insert(0, [5 for _ in range(N + 2)])
    MAP.append([5 for _ in range(N + 2)])
    for i in range(N + 2):
        for j in range(N + 2):
            if 6 <= MAP[i][j] and MAP[i][j] <= 10:
                wormholes[MAP[i][j]].append([j, i])
    for i in range(N + 2):
        for j in range(N + 2):
            if MAP[i][j] == 0:
                for each_di in range(4):
                    ball = [j, i, each_di]
                    score = 0
                    start_point = ball[:2]

                    while True:
                        ball[x] = ball[x] + direct[ball[di]][x]
                        ball[y] = ball[y] + direct[ball[di]][y]
                        sign = MAP[ball[y]][ball[x]]
                        if sign == -1 or start_point == ball[:2]:
                            break
                        elif 1 <= sign <= 5:
                            ball[di] = change_direction[sign][ball[di]]
                            score += 1
                        elif 6 <= sign <= 10:
                            ball[x], ball[y] = (
                                wormholes[sign][1]
                                if ball[:2] == wormholes[sign][0]
                                else wormholes[sign][0]
                            )
                    route_score = max(route_score, score)
    return route_score


def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        MAP = [list(map(int, input().split())) for _ in range(N)]
        ans = solution(N, MAP)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()


# 1 9
# 2 0
# 3 7
# 4 5
# 5 19


x, y, di = (0, 1, 2)
# left 0, right 1, up 2, down 3
direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
change_direction = [
    0,
    [2, 0, 3, 1],
    [3, 0, 1, 2],
    [1, 3, 0, 2],
    [1, 2, 3, 0],
    [1, 0, 3, 2],
]

# **********************************************
# 버전 2
# 메모리 98456 KB, 1780 ms
# 바운더리 체크만 줄임

# def calculate(ball, N, MAP, wormholes):
#     score = 0
#     start_point = ball[:2]

#     visit = set()
#     while True:
#         ball[x] = ball[x] + direct[ball[di]][x]
#         ball[y] = ball[y] + direct[ball[di]][y]
#         if tuple(ball) in visit:
#             return -1
#         visit.add(tuple(ball))

#         sign = MAP[ball[y]][ball[x]]
#         if sign == -1 or start_point == ball[:2]:
#             return score
#         elif 1 <= sign <= 5:
#             ball[di] = change_direction[sign][ball[di]]
#             score += 1
#         elif 6 <= sign <= 10:
#             ball[x], ball[y] = (
#                 wormholes[sign][1] if ball[:2] == wormholes[sign][0] else wormholes[sign][0]
#             )
#     return score


# def solution(N, not_expanded_MAP):
#     route_score = 0
#     wormholes = [[] for _ in range(11)]
#     MAP = []
#     MAP = [[5] + M + [5] for M in not_expanded_MAP]
#     MAP.insert(0, [5 for _ in range(N + 2)])
#     MAP.append([5 for _ in range(N + 2)])
#     for y in range(N + 2):
#         for x in range(N + 2):
#             if 6 <= MAP[y][x] and MAP[y][x] <= 10:
#                 wormholes[MAP[y][x]].append([x, y])
#     for y in range(N + 2):
#         for x in range(N + 2):
#             if MAP[y][x] == 0:
#                 for each_di in range(4):
#                     score = calculate([x, y, each_di], N + 2, MAP, wormholes)
#                     route_score = max(route_score, score)
#     return route_score


# def main():
#     T = int(input())
#     for t in range(1, T + 1):
#         N = int(input())
#         MAP = [list(map(int, input().split())) for _ in range(N)]
#         ans = solution(N, MAP)
#         print("#{} {}".format(t, ans))


# if __name__ == "__main__":
#     main()


# ****************************************
# 버전 -1
# 내 코드가 아니다
# 최고의 효율성을 달성한 코드
# 군더더기는 다 줄이고 동작하는 것에 집중했다.
# 함수를 만들지않아 넘어가는 과정 조차 없음
# 바운더리를 만들고 for문안에서 바로 계산하는 효율적인 코드이다.

# ewsn=[[0,0,1],[1,0,-1],[2,1,0],[3,-1,0]]
# direction=[0,[1,3,0,2],[1,2,3,0],[2,0,3,1],[3,0,1,2],[1,0,3,2]]
#
# for tc in range(int(input())):
#     N=int(input())
#     mat=[]
#     warmhole=[[] for _ in range(11)]
#     for row in range(N+2):
#         if row==0 or row==N+1:mat.append([5]*(N+2));continue
#         tmp=list(map(int,input().split()))
#         tmp.insert(0,5)
#         tmp.append(5)
#         for col in range(len(tmp)):
#             if tmp[col]>5:
#                 warmhole[tmp[col]].append([row,col])
#         mat.append(tmp)
#     ans=0
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             sx,sy=i,j
#             if mat[i][j]:continue
#             for k in range(4):
#                 cnt=0
#                 dn,dx,dy=ewsn[k]
#                 nx,ny=i+dx,j+dy
#                 while 1:
#                     if [nx,ny]==[sx,sy] or mat[nx][ny]==-1:
#                         if ans<cnt:ans=cnt;break
#                         break
#                     if 0<mat[nx][ny]<6:
#                         dn,dx,dy=ewsn[direction[mat[nx][ny]][dn]]
#                         cnt+=1
#                     elif 5<mat[nx][ny]<11:
#                         if [nx,ny]==warmhole[mat[nx][ny]][0]:
#                             nx,ny=warmhole[mat[nx][ny]][1]
#                         else:nx,ny=warmhole[mat[nx][ny]][0]
#                     nx,ny=nx+dx,ny+dy
#     print("#{} {}".format(tc+1,ans))