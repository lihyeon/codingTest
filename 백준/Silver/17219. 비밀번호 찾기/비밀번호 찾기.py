import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}
for _ in range(n):
    url, passworld = input().split()
    dict[url] = passworld

for i in range(m):
    url = input().strip()
    if url in dict:
        print(dict[url])