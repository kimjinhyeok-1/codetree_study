n, m = map(int, input().split())

# Please write your code here.


def k(n,m):
    ans = 0
    for i in range(1, min(n,m)+1):
        if n % i == 0 and m % i == 0:
            ans = i
    return ans

print(k(n,m))