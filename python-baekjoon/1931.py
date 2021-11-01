# 회의실 배정 1931 
# Greedy algorithm
# time complexity: NlogN

meetings = []
N = int(input())

for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort()

last_srt = 0
last_end = 0
cnt = 0

for srt, end in meetings:
    if last_end <= srt:
        cnt += 1
        last_srt = srt
        last_end = end
        continue
    if end < last_end:
        last_srt = srt
        last_end = end

print(cnt)
