def solution(N):
    dp = [1] * (N+2)
    for i in range(2, N+2):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N+1] * 2

# def solution(N):
#     a, b = 1, 1
#     while N+2 > 2:
#         a, b = b, a + b
#         N -= 1
#     return 2 * b