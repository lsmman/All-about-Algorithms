# 이거 망 다시 공부할것
def solve(G):
    ans = 1
    if G % 2 == 1:
        ans += 1
    if G % 3 == 0:
        ans += 1
    left = right = 1
    limit = G // 3
    sum_val = 1
    while left < limit:
        if sum_val < G:
            right += 1
            sum_val += right
        else:
            if sum_val == G:
                ans += 1
            sum_val -= left
            left += 1
    return ans


for c in range(int(input())):
    G = int(input())
    ans = solve(G)
    print("Case #{}: {}".format(c + 1, ans))
