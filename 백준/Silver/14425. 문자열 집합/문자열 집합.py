import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N, M = map(int, input().split())


arr = []
for i in range(N):
    arr.append(input().strip())

arr2 = []
for i in range(M):
    arr2.append(input().strip())

# 2초. O(N^2) 가능
# 2중 for 돌리면 O(N^2)
# hash 쓰면 전처리시 O(N), 연산시 O(1)

hash = defaultdict(int)
cnt = 0

for i in arr:
    hash[i] = 1 # hash['startlink'] = 1

for i in arr2:
    if (hash[i] == 1):
        cnt += 1
    else:
        continue

print(cnt)