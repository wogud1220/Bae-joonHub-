import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
sys.setrecursionlimit(1000)


N, S = map(int,input().split())

arr = list(map(int, input().split()))
i = 0
j = 0
window_sum = 0

result = float('inf')


while True:
    if window_sum >= S: #윈도우 값이 크다면
        result = min(abs(j-i), result)
        window_sum -= arr[i]
        i+=1

    else: # 윈도우값이 작으면
        if j == N: # 끝에 도달했다면 브레이크
            break

        window_sum += arr[j]
        j+=1

if result == float('inf'):
    print(0)
else:
    print(result)