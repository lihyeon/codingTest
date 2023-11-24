import sys
input = sys.stdin.readline

dp = [1, 2, 4]
t = int(input())
for i in range(t):
    n = int(input())
    if n <= len(dp):
        print(dp[n-1])
    else:
        for j in range(len(dp), n):
            dp.append(dp[j-1]+dp[j-2]+dp[j-3])

        print(dp[-1])