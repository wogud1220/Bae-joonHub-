import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N = int(input().strip())
arr = list(map(int, input().split()))


M = int(input().strip())
arr2 = list(map(int, input().split()))

hash = defaultdict(int)



for i in arr:
    hash[i] += 1

for i in arr2:
    print(hash[i])