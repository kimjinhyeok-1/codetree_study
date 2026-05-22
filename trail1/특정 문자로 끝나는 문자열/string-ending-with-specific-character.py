arr = list(input() for _ in range(10))
last = input()

result = []
for a in arr:
    if a[-1] == last:
        result.append(a)

if result:
    for r in result:
        print(r)
else:
    print("None")