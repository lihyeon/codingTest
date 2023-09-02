import sys
n, m = map(int, sys.stdin.readline().split())
d = {}

for _ in range(n):
    url, ps = sys.stdin.readline().split()
    d[url] = ps

for _ in range(m):
    print(d[sys.stdin.readline().rstrip()])