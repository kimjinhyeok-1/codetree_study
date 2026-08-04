import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
rr, cc = map(int, input().split())
distory_dist = grid[rr-1][cc-1]

def inRange(r, c):
    return 0<=r<N and 0<=c<N

def explode(r, c, n):
    for dr, dc in d:
        for dist in range(1, n):
            nr = r + dr * dist
            nc = c + dc * dist
            if inRange(nr,nc):
                grid[nr][nc] = 0

grid[rr-1][cc-1] = 0
explode(rr-1, cc-1, distory_dist)

for c in range(N):
    temp = []
    for r in range(N):
        if grid[r][c] != 0:
            temp.append(grid[r][c])
    for r in range(N):
        grid[r][c] = 0
    
    start = N - len(temp) 
    for i in range(len(temp)): 
        grid[start + i][c] = temp[i]

for i in range(N):
    print(*grid[i])