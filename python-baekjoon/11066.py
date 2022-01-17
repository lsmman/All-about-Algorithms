def main(n, inputs):
    dp = [[0 for i in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = inputs[i]

    for term in range(2, n):
        term = term - 1
        for i in range(n-term+1):
            dp[i][i+term]
                

    pass


for _ in range(int(input())):
    n = input()
    inputs = list(map(int, input().split()))
    main(n, inputs)