import sys
input = sys.stdin.readline




N = int(input().strip())
arr = [0]*N
for i in range(N):
    arr[i] = int(input().strip())



arr = sorted(arr, reverse=True)

for i in arr:
    print(i)
