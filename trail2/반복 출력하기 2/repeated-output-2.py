n = int(input())

# Please write your code here.
def pHW(n):
    if n == 0:
        return
    pHW(n-1)
    print("HelloWorld")
    

pHW(n)