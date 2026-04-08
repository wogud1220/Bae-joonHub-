import sys
input = sys.stdin.readline
from collections import deque
import heapq



N, M = map(int, input().split())

arr = []

hash = {}


for i in range(N):
    cmd = input().split()
    hash[cmd[0]] = cmd[1]

for i in range(M):
    cmd = input().strip()
    print(   hash[cmd]       )