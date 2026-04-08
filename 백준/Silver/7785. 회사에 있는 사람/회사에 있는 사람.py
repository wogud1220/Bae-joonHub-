import sys

input = sys.stdin.readline

from collections import deque
import heapq

n = int(input().strip())
hash = {}
for i in range(n):
    cmd = input().split()

    if cmd[1] == "enter":
        # 출근했으면
        hash[cmd[0]] = 1
    else:# 퇴근했으면 해시에서 삭제
        del hash[cmd[0]]

arr = []
for i in hash:
    arr.append(i)


# arr = sorted(arr, reverse=True)
arr.sort(reverse = True)
for i in arr:
    print(i)