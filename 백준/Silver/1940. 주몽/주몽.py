import sys

input = sys.stdin.readline


N = int(input())
M = int(input())

arr = list(map(int, input().split()))

left = 0
right = len(arr) - 1
cnt = 0



arr.sort()

while left < right:

    if arr[left] + arr[right] < M:
        left += 1

    elif arr[left] + arr[right] > M:
        right -= 1

    elif arr[left] + arr[right] == M:
        cnt += 1
        right -= 1


print(cnt)