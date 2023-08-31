import sys
k = int(sys.stdin.readline())
stack = []

for i in range(k):
    n = int(sys.stdin.readline().strip())
    stack.append(n)
    if n==0:
        stack.pop()
        stack.pop()

print(sum(stack))