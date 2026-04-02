import sys

input = sys.stdin.readline


N, M = map(int, input().split())


arr = list(map(int, input().split()))

left = 0
right = 0
cnt = 0

sum_value = 0


while True:

#left increase -> break -> right increase!!!
    if sum_value >= M:
        sum_value -= arr[left]
        left +=1
    elif right == N:
        break
    elif sum_value < M:
        sum_value +=arr[right]
        right += 1



    if sum_value == M:
        cnt += 1

print(cnt)