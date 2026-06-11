n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

rects = []

# 모든 직사각형 만들기
for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                total = 0

                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        total += grid[r][c]

                rects.append((r1, c1, r2, c2, total))


def not_overlap(a, b):
    ar1, ac1, ar2, ac2, _ = a
    br1, bc1, br2, bc2, _ = b

    return (
        ar2 < br1 or
        br2 < ar1 or
        ac2 < bc1 or
        bc2 < ac1
    )


ans = -10**18

for i in range(len(rects)):
    for j in range(i + 1, len(rects)):
        if not_overlap(rects[i], rects[j]):
            ans = max(ans, rects[i][4] + rects[j][4])

print(ans)