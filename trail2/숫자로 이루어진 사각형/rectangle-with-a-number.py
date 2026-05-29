n = int(input())

# Please write your code here.
def printnum(n):
    i = 1
    for _ in range(n):
        for _ in range(n):
            print((i-1) % 9 +1, end = " ")
            i += 1
        print()

printnum(n)