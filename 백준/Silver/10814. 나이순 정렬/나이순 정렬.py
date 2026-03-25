import sys
input = sys.stdin.readline



N = int(input())
cmd = []
for i in range(N):
    age, name = input().split()
    cmd.append((int(age), name))


cmd.sort(key=lambda x:x[0])
for i in range(N):
    print(*cmd[i])
