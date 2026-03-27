import sys
input = sys.stdin.readline


arr = [0] * 31

for i in range(28):
    a = int(input().strip())
    arr[a] = 1

for i in range(1,31):
    if arr[i] != 1:
        print(i)
