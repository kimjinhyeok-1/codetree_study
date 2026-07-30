import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
isTrue = False
q = deque([(0,0)])

d = [(1,0),(-1,0),(0,1),(0,-1)]
while q: 
    r,c = q.popleft()
    if r == n-1 and c == m-1:
        isTrue = True
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0<= nr < n and 0<= nc < m:
            if map[nr][nc] == 1 and visited[nr][nc] == False:
                visited[nr][nc] = True
                q.append((nr,nc))

if isTrue:
    print(1)
else:
    print(0) 