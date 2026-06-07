n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0

blocks = [
    [(0,0), (0,1), (0,2)],   # 가로 일자
    [(0,0), (1,0), (2,0)],   # 세로 일자

    [(0,0), (1,0), (1,1)],
    [(0,0), (0,1), (1,0)],
    [(0,0), (0,1), (1,1)],
    [(0,1), (1,0), (1,1)],
]

for r in range(n):
    for c in range(m):
        for block in blocks:
            isblock = True
            temp = 0
            for dr, dc in block:
                nr, nc = r + dr, c+ dc
                if not  (0<=nr<n and 0<=nc<m):
                    isblock = False
                    break
                temp += grid[nr][nc]
            if isblock:
                ans = max(ans,temp)
print(ans)
