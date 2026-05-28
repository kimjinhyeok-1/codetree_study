n = int(input())

# Please write your code here.
def pHW(n):
    if n == 0:
        return
    print("HelloWorld")
    pHW(n-1)

pHW(n)