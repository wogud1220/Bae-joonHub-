import sys

input = sys.stdin.readline


n = int(input())

cnt = 0

while True:

    # 5로 나누어떨어진다면
    if n % 5 == 0:
        cnt += (n//5)
        print(cnt)
        break


    # 5로 안나누어떨어진다면
    n -= 2
    cnt += 1

    if n < 0:
        print(-1)
        break