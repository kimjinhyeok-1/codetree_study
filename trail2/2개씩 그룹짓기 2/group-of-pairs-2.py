n = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = float('inf')

for i in range(n):
    answer = min(answer, arr[i + n] - arr[i])

print(answer)