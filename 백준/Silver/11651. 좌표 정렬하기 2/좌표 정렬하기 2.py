import sys
input = sys.stdin.readline



N = int(input())
cordinate = []
for i in range(N):
    X, Y = input().split()
    cordinate.append((int(X),int(Y)))


cordinate.sort(key=lambda X:(X[1], X[0]))


for i in range(N):
    print(*cordinate[i])