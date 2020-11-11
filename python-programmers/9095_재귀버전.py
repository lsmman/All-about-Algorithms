
num_list = []
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

def solve(n):
    if not dp[n]:
        dp[n] = solve(n-3) + solve(n-2) + solve(n-1)
    return dp[n]
    
for _ in range(int(input())):
    num_list.append(int(input()))

for n in num_list:
    print(solve(n))