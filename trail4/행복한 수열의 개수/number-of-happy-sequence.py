n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0

for r in range(n):
    t1 = 1
    t2 = 1
    prev = grid[r][0]
    for c in range(1,n):
        curr = grid[r][c]
        if prev == curr:
            t2 += 1
        else:
            t2 = 1
        t1 = max(t1, t2)
        prev = curr
    if t1 >= m:
        ans += 1
for c in range(n):
    t1 = 1
    t2 = 1
    prev = grid[0][c]
    for r in range(1,n):
        curr = grid[r][c]
        if prev == curr:
            t2 += 1
        else:
            t2 = 1
        t1 = max(t1, t2)
        prev = curr
    if t1 >= m:
        ans += 1
print(ans)