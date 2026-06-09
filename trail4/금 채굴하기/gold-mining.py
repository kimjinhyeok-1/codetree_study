n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

"""
    완탐으로 풀어보자
    완탐으로 풀 때 중앙 좌표을 통해 구할 값은 두 개
    1. 비용
    2. 금 비용
"""

def p (k):
    return k**2 + (k+1)**2
ans = 0
for c_r in range(n):
    for c_c in range(n):
        for k in range(2*n):
            gold_count = 0
            for r in range(n):
                for c in range(n):
                    if abs(r-c_r) + abs(c-c_c) <= k:
                        gold_count += grid[r][c]
            if gold_count * m >= p(k):
                ans = max(ans, gold_count)

print(ans)