from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        q.append(int(cmd[1]))

    elif cmd[0] == "pop":
        print(q.popleft())

    elif cmd[0] == "size":
        print(len(q))

    elif cmd[0] == "empty":
        print(1 if not q else 0)

    elif cmd[0] == "front":
        print(q[0])
        