text = input()
pattern = input()

# Please write your code here.
lpattern = len(pattern)
def cnt():
    for i in range(len(text)):
        if text[i:i+lpattern] == pattern:
            return i
    return -1

print(cnt())