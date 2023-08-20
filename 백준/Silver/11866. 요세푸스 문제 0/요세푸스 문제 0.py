import sys
n, k = map(int, sys.stdin.readline().split())
d = [i for i in range(1, n+1)]
result = []
target = 0

while d:
    target += (k-1)
    if target >= len(d):
        target %= len(d)
    result.append(str(d.pop(target)))

print("<", ', '.join(result), ">", sep='')