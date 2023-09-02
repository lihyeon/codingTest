import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dic = {}
for _ in range(n):
    hear = input().rstrip()
    dic[hear] = 0

for _ in range(m):
    see = input().rstrip()
    if see in dic:
        dic[see] += 1

tmp = [k for k, v in dic.items() if v == 1]
tmp.sort()
print(len(tmp))
for i in tmp:
    print(i)