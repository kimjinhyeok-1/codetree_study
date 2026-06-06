n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n-2):
    for j in range(n-2):
        temp = 0
        for r in range(i,i+3):
            for c in range(j,j+3):
                if grid[r][c] == 1:
                    temp += 1
        ans = max(temp,ans)

print(ans)