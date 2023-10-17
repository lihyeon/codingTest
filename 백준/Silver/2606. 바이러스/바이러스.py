from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
p = int(input())

graph = [[] for i in range(n+1)]
for i in range(p):
    n1, n2 = map(int, input().split())
    graph[n1] += [n2]
    graph[n2] += [n1]

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

_visited = [0]*(n+1)
bfs(graph, 1, _visited)

print(sum(_visited)-1)