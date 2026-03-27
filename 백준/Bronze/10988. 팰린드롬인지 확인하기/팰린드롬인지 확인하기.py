import sys
input = sys.stdin.readline


cmd = input().strip()


for i in range(len(cmd)):
    if cmd[i] == cmd[len(cmd)-i-1]:
        continue
    else:
        print(0)
        exit()


print(1)