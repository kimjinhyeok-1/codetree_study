from collections import deque

n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
q = deque()
for c, n in zip(cmd,num):
    if c == "push_front":
        q.appendleft(n)
    if c == "push_back":
        q.append(n)
    if c == "pop_front":
        print(q.popleft())
    if c == "pop_back":
        print(q.pop())
    if c == "empty":
        if q:
            print(0)
        else:
            print(1)
    if c == "front":
        print(q[0])
    if c == "back":
        print(q[-1])
    if c == "size":
        print(len(q))