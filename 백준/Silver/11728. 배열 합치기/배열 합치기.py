import sys

input = sys.stdin.readline


N, M = map(int, input().split())


A = list(map(int, input().split()))

B = list(map(int, input().split()))

answer = []
left = 0
right = 0



while left < N and right < M:
    if A[left] <= B[right]:
        answer.append(A[left])
        left += 1
    elif A[left] > B[right]:
        answer.append(B[right])
        right += 1


if left < N:
    answer.extend(A[left:])
else:
    answer.extend(B[right:])



print(*(answer))
