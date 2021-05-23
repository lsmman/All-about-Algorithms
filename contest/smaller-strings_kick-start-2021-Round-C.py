# TLE 나옴 다시 공부할 것
def count_smaller_strings(N, K, S):
    mid_point = (N - 1) // 2
    cnt = 0
    S = list(map(lambda x: ord(x) - ord("a") + 1, S))
    pal_S = S[:]

    for i in range(mid_point + 1):
        pal_S[N - 1 - i] = S[i]
    if pal_S < S:
        cnt += 1

    power_K = 1
    for i in range(mid_point, -1, -1):
        cnt += (S[i] - 1) * power_K
        cnt = cnt % 1000000007
        power_K *= K

    return cnt % 1000000007


ans = []
for case in range(int(input())):
    N, K = map(int, input().split())
    S = input()
    ans.append(count_smaller_strings(N, K, S))
for i, a in enumerate(ans):
    print("Case #{}: {}".format(i + 1, a))
