# 다이나믹 프로그래밍, 그리디, 완전 탐색

str1 = input().strip()
str2 = input().strip()

short_str, long_str = str1, str2
if len(short_str) > len(long_str):
    short_str, long_str = long_str, short_str

cur = [0] * (len(long_str)+1)

for short_idx in range(len(short_str)-1, -1, -1):
    short = short_str[short_idx]
    for long_idx, long_ in enumerate(long_str):
        if long_ == short:
            cur[long_idx] = max(cur[long_idx], max(cur[long_idx+1:]) + 1)
print(max(cur))
