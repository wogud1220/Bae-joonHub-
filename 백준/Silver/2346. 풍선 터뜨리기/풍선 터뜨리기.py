import sys
input = sys.stdin.readline
from collections import deque
import heapq
sys.setrecursionlimit(1000)


N = int(input().strip())

arr = list(map(int,input().split()))

deck = deque((i+1, arr[i]) for i in range(N))

result = []
while deck:
    index, value = deck.popleft()
    result.append(index)

    if value > 0: #양수면
        deck.rotate(-value+1)

    else:
        deck.rotate(-value)

print(*result)



