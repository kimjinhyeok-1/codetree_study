str = input()

# Please write your code here.
arr = []
isG = True

for s in str:
    if s == '(':
        arr.append('(')
    else:
        if len(arr) == 0:
            isG = False
            break
        arr.pop()

if len(arr) != 0:
    isG = False

if isG:
    print("Yes")
else:
    print("No")