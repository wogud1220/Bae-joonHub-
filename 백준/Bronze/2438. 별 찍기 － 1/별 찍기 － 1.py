import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
sys.setrecursionlimit(1000)

N = int(input().strip())

for i in range(1,N+1):
    print('*'*i)