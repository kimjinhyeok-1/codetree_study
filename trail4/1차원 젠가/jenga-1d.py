import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
block = deque()
for _ in range(2):
    s1,e1 = map(int, input().split())
    block.append((s1, e1))

# 비어있는 리스트 만들기
temp = []

# 돌면서 배열 값을 0으로 바꾸기
# 0이 아닌 경우 temp 추가
# 기존 arr를 temp로 바꾸고 temp 다시 초기화
for _ in range(2):
    s, e = block.popleft()
    for i in range(s-1, e):
        arr[i] = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            temp.append(arr[j])
    arr = temp
    temp = []

print(len(arr))
print(*arr, sep = "\n")