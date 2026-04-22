import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
sys.setrecursionlimit(1000)

N = int(input().strip())
arr = []
for _ in range(N):
    a, b = map(int,input().split())
    arr.append([a,b])


X_hap = 0
n = 0
i = 0
j = 0
Y_hap = 0

while n < N: # 0, 1, 2, 3
    if i == N - 1:
        X_hap += arr[i][0]*arr[0][1]
        break
    else:
        X_hap += arr[i][0] * arr[i+1][1]
        i+=1
        n+=1
i = 0
n = 0
while n < N: #0, 1, 2, 3
    if i == N - 1: # i가 4이라면
        Y_hap += arr[0][0]* arr[i][1]
    else:
        Y_hap += arr[i][1] * arr[i+1][0]
    i+=1
    n+=1
area = abs(X_hap - Y_hap) / 2
print(area)