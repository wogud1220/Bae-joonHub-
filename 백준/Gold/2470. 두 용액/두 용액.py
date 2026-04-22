import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
sys.setrecursionlimit(1000)


N = int(input().strip())

arr = list(map(int, input().split()))
arr.sort()
i = 0
j = N - 1
min_x = float('inf')

while i < j:
    s = arr[i] + arr[j]
    if abs(s) < min_x:
        min_x = abs(arr[i]+arr[j])
        left = i
        right = j

    if s > 0:
        j-=1
    else:
        i+=1

print(arr[left], arr[right])


