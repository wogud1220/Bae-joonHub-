import sys
input = sys.stdin.readline
num = int(input())
S = set()
for i in range(num): # 0부터 num-1까지

    cmd = input().split()

    if cmd[0] == "add":
        S.add(int(cmd[1]))

    elif cmd[0] == "remove":
        S.discard(int(cmd[1]))

    elif cmd[0] == "check":
        if int(cmd[1]) in S:
            print("1")
        else:
            print("0")

    elif cmd[0] == "toggle":
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            S.add(int(cmd[1]))

    elif cmd[0] == "all":
        S = set(range(1,21))

    elif cmd[0] == "empty":
        S = set()

