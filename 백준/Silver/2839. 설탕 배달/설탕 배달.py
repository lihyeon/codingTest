import sys
n = int(sys.stdin.readline())
cnt = []
i = 0

while True:
    if (n%5)==0:
        cnt.append(n//5 + i)
    if (n%3)==0:
        cnt.append(n//3 + i)
    if (n%5)%3==0:
        cnt.append(n//5 + (n%5)//3 + i)
    if n<=5:
        break
    else:
        i += 1
        n -= 5

if len(cnt) > 0:
    print(min(cnt))
else:
    print(-1)