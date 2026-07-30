import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True

q = deque([(0,0)])

d = [(1,0),(-1,0),(0,1),(0,-1)]
while q: 
    r,c = q.popleft()

    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0<= nr < n and 0<= nc < m:
            if grid[nr][nc] == 1 and visited[nr][nc] == False:
                visited[nr][nc] = True
                q.append((nr,nc))

print(1 if visited[n-1][m-1] else 0)