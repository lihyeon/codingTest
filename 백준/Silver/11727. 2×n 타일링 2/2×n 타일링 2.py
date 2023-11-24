n = int(input())
dp = [0] * (n+1)

dp[0] = 1
dp[1] = 3
if n <= 2:
    print(dp[n-1] % 10007)
else:
    for i in range(2, n):
        dp[i] = dp[i-1] + 2*dp[i-2]
    print(dp[n-1] % 10007)