import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
queue = deque()

cmd = []
for i in range(N):
    cmd = input().split()

    # 길이가 2이상이면 => push 1 처럼 뒤에 정수가붙으면
    if len(cmd) > 1:
        cmd[1] = int(cmd[1]) # 정수로 변환
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "front": # 맨 앞에 있느 ㄴ거출력
        if not queue: # 큐에 아무것도 없다면 -1
            print(-1)
        else:# 있다면 맨 앞 출력
            print(queue[0])


    elif cmd[0] == "back":
        if not queue: # 큐에 아무것도 없다면 -1
            print(-1)
        else:# 있다면 맨 뒤 출력
            print(queue[-1])

    elif cmd[0] == "empty":
        if not queue: # 큐에 아무것도 없다면 -1
            print(1)
        else:
            print(0)

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())

