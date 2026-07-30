import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
result = 0

q = deque()

for _ in range(K):
    r,c = map(int, input().split())
    visited[r-1][c-1] = True
    result += 1
    q.append((r-1,c-1))

while q:
    r,c = q.popleft()
    for dr, dc in d:
        nr,nc = r + dr, c + dc
        if 0<= nr < N and 0<= nc < N and not visited[nr][nc] and grid[nr][nc] == 0:
            result += 1
            visited[nr][nc] = True
            q.append((nr,nc))

print(result)
