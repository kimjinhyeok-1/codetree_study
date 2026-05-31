n, m = map(int, input().split())
s = input()

left = list(s)
right = []

for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'L':
        if left:
            right.append(left.pop())

    elif cmd[0] == 'R':
        if right:
            left.append(right.pop())

    elif cmd[0] == 'D':
        if right:
            right.pop()

    elif cmd[0] == 'P':
        left.append(cmd[1])

print(''.join(left + right[::-1]))