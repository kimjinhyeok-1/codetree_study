n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dirs = [(-1, 1), (-1, -1), (1, -1), (1, 1)]

ans = 0

for sr in range(n):
    for sc in range(n):
        for a in range(1, n):
            for b in range(1, n):
                r, c = sr, sc
                total = 0
                possible = True

                for d, length in enumerate([a, b, a, b]):
                    dr, dc = dirs[d]

                    for _ in range(length):
                        r += dr
                        c += dc

                        if not (0 <= r < n and 0 <= c < n):
                            possible = False
                            break

                        total += grid[r][c]

                    if not possible:
                        break

                if possible:
                    ans = max(ans, total)

print(ans)