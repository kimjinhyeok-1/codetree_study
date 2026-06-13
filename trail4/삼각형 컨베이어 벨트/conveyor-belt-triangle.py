n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))
arr = l + r + d
# Please write your code here.
length = 3 * n
t %= length

for _ in range(t):
    temp = arr[-1]

    for i in range(length - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = temp

for i in range(3):
    print(*arr[i * n:(i + 1) * n])