n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
while t != 0:
    up_temp = u[n-1]
    down_temp = d[n-1]

    for i in range(n-1,0,-1):
        u[i] = u[i-1]
    u[0] = down_temp

    for i in range(n-1,0,-1):
        d[i] = d[i-1]
    d[0] = up_temp
    
    t -= 1

print(*u)
print(*d)