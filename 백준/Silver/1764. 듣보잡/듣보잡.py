import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N, M = map(int, input().split())


no_see = set()
no_listen = set()
for _ in range(N): # 3번, 듣도 못한사람
    no_listen.add(input().strip())

for j in range(M): # 4번 , 보도 못한사람
    no_see.add(input().strip())

result = no_see.intersection(no_listen)

print(len(result))

result = list(result)
result.sort()

for _ in result:
    print(_)
