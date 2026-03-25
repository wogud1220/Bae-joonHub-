import sys
input = sys.stdin.readline

stack = []

N = int(input())
arr = [0, 0]

for i in range(N):
    cmd = input().split()
    if len(cmd) > 1:
        cmd[1] = int(cmd[1])
    if cmd[0] == "pop" and not stack: #팝인경우 제일 위에 꺼내기
        print("-1")
    elif cmd[0] == "pop":
        print(stack.pop())

    elif cmd[0] == "push":
        stack.append(cmd[1])

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "top" and not stack:
        print("-1")

    elif cmd[0] == "top":
        print(stack[-1])

    elif cmd[0] == "empty":
        if not stack:
            print("1")
        else:
            print("0")