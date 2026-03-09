import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = []
current = 1

for _ in range(n):
    target = int(input())

    while current <= target:
        stack.append(current)
        result.append("+")
        current += 1

    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit()

for r in result:
    print(r)