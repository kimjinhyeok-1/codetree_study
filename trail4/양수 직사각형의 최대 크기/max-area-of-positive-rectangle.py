n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = -1
for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                possible = True
                for r in range(r1,r2+1):
                    for c in range(c1,c2+1):
                        if grid[r][c] <= 0:
                            possible = False
                            break
                    if not possible:
                        break
                if possible:
                    temp = (r2-r1+1) * (c2-c1+1)
                    ans = max(ans,temp)
print(ans)