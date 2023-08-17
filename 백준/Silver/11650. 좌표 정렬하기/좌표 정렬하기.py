import sys
n = int(sys.stdin.readline())
d = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    d.append((x,y))

d.sort(key=lambda x:(x[0],x[1]))
for i in d:
    print(i[0], i[1])