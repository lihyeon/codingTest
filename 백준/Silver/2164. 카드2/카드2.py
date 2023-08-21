import sys
n = int(sys.stdin.readline())

i = 0
while True:
    if n <= 2**i:
        break
    i += 1

print(int((n-2**(i-1))*2))