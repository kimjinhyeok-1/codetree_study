N = int(input())

commands = []
nums = []

for _ in range(N):
    line = input().split()
    commands.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        nums.append(int(line[1]))
    else:
        nums.append(0)

# Please write your code here.

ans = []
for command, num in zip(commands,nums):
    if command == 'push_back':
        ans.append(num)
    if command == 'pop_back':
        ans.pop()
    if command == 'size':
        print(len(ans))
    if command == 'get':
        print(ans[num-1])