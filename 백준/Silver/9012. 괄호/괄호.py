t = int(input())


for i in range(t):
    stack = []
    x = list(input())

    for j in x:
        if j == "(":
            stack.append(j)
        if j == ")":
            if "(" in stack:
                stack.remove("(")
            else:
                stack.append(j)

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")