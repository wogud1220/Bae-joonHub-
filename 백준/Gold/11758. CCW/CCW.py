import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
sys.setrecursionlimit(1000)

X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())

ad = (X2-X1) * (Y3 - Y1)
bc = (X3-X1) * (Y2 - Y1)

if ad-bc > 0: # 양수면 세타가 커지니깐 counter clock wiise
    print(1)
elif ad-bc < 0:
    print(-1)
else:
    print(0)