import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N = int(input().strip())



arr = []
for i in range(N):
    arr.append(input().strip())


arr = sorted(list(set(arr)), key= lambda X:(len(X), X))

for i in arr:
    print(i)


