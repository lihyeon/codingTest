import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]

d = [0]*n

if len(stairs) <= 2:
    print(sum(stairs))

else:
    d[0] = stairs[0]
    d[1] = stairs[0] + stairs[1]
    d[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3, n):
        d[i] = max(d[i-3] + stairs[i-1] + stairs[i], d[i-2] + stairs[i])

    print(d[-1])