A = input()

# Please write your code here.
answer = float('inf')
# 1. 시뮬레이션으로 전체 돌기
# 2. 돌면서 길이 구하기
# ===============================================
#                  길이 구하기
# ===============================================
# prev랑 curr를 설정한다. 
# curr가 prev랑 다르면 result에 추가하고 prev를 curr로 바꾸고 count를 1로 초기화
# curr가 prev랑 같다면 count += 1
def cal(s):
    result = ""
    prev = s[0] 
    count = 1
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        elif s[i] != prev:
            result += prev + str(count)
            prev = s[i]
            count = 1
    result += prev + str(count)
    return len(result)

current = A
for _ in range(len(current)):
    answer = min(answer, cal(current))
    current = current[-1] + current[:-1]

print(answer)