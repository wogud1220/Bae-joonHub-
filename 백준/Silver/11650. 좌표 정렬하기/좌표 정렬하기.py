import sys
input = sys.stdin.readline



N = int(input())
cordinate = []
for i in range(N):
    X, Y = input().split()
    cordinate.append((int(X),int(Y)))


cordinate.sort()


for i in range(N):
    print(*cordinate[i])
