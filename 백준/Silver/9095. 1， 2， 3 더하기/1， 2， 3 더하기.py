import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 11

for i in range(t):
    n = int(input())
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if n <= 3:
        print(dp[n])
    else:
        for j in range(4, n+1):
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[n])