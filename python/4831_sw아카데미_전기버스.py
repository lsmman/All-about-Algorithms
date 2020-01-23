# sw expert academy
# 4831 전기버스
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys

sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargings = list(map(int, input().split()))
    stop = 0
    charge_count = 0

    station_now = 0 # start point = 0
    moved_station = 0

    while not stop:
      for moving_station in range(K, -1, -1):
        if not moving_station:
          charge_count = 0
          stop = 1
          break

        moved_station = station_now + moving_station

        if moved_station >= N:
          stop = 1
          break

        if moved_station in chargings:
          station_now = moved_station
          charge_count = charge_count + 1
          break
        # else : pass

    print("#" + str(test_case), charge_count)

# K = 충전 시 이동 가능한 수
# N = 총 정류장의 수
# M = 충전기가 있는 정류장의 수

# input 
# 3
# 3 10 5
# 1 3 5 7 9
# 3 10 5
# 1 3 7 8 9
# 5 20 5
# 4 7 9 14 17

# output
#1 3
#2 0
#3 4

