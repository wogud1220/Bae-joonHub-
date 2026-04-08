import sys
input = sys.stdin.readline
from collections import deque
import heapq


N, M = map(int,input().split())
second_cmd = list(map(int,input().split()))
arr = []

for i in range(1,N+1):
    arr.append(i)


Q = deque(arr)
cnt = 0
while second_cmd:

    if Q[0] == second_cmd[0]:
        # print(Q[0],"을 뽑고았습니다.")
        Q.popleft()
        del second_cmd[0]
        continue

    else:
        pivot = len(Q)//2 # 5
        if pivot < Q.index(second_cmd[0]):
            Q.rotate(1)
            cnt += 1
            # print("오른쪽으로 한번 돌려서 현재 모양새는", Q, "cnt = ", cnt)
        else:

            Q.rotate(-1)
            cnt+=1
            # print("현재 모양새는", Q, "cnt = ", cnt)

print(cnt)

