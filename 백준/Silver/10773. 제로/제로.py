import sys
input = sys.stdin.readline

K = int(input().strip())

stack = []

for i in range(K):
    X = int(input().strip())

    if X == 0:
        stack.pop()
    else:
        stack.append(X)

print(sum(stack))