import sys
input = sys.stdin.readline
from collections import deque
import heapq


wait_stack = deque()

N = int(input().strip())  # 승환이 앞에 서있는 학생들의 수


arr = list(map(int,input().split()))

cnt = 1



for student in arr:

    if cnt == student:
        cnt += 1
        while wait_stack and wait_stack[-1] == cnt:
            wait_stack.pop()
            cnt += 1

    else:
        wait_stack.append(student)

if not wait_stack:
    print("Nice")
else:
    print("Sad")