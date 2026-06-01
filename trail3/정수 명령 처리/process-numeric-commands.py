n = int(input())
stack = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        stack.append(int(cmd[1]))

    elif cmd[0] == "pop":
        print(stack.pop())

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        print(1 if not stack else 0)

    elif cmd[0] == "top":
        print(stack[-1])