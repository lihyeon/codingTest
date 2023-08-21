from collections import deque
import sys
n = int(sys.stdin.readline())
d = deque([i for i in range(1, n+1)])

while n>1:
    d.popleft()
    n-=1
    d.append(d.popleft())

print(d[0])