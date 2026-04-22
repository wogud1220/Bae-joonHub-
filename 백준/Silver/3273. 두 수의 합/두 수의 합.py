import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
sys.setrecursionlimit(1000)


N = int(input().strip())

arr = list(map(int, input().split()))
X = int(input().strip())
arr.sort()
cnt = 0

j = N-1
i = 0
while i < j:
    if arr[i] + arr[j] == X:
        cnt +=1
        i+=1
        # j-=1
    elif arr[i] + arr[j] > X:
        j -= 1
    elif arr[i] + arr[j] < X:
        i+=1

print(cnt)
