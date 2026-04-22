import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
sys.setrecursionlimit(1000)


X = int(input().strip())
Y = int(input().strip())

if X > 0 and Y > 0:
    print(1)
elif X > 0 and Y < 0:
    print(4)
elif X < 0 and Y > 0 :
    print(2)
else:
    print(3)