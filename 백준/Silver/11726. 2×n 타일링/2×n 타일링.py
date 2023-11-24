n = int(input())
dp = [0]*n


if n <= 3:
    print(n%10007)
else:
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[-1] % 10007)