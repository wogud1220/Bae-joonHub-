import sys

input = sys.stdin.readline


N = input().strip()
answer = ''
cnt = 0
for ch in N:
    if ch == 'X':
        cnt += 1


    else:
        answer += 'AAAA' * (cnt//4)
        cnt = cnt % 4

        if cnt == 2:
            answer += 'BB'
            cnt = 0

        if cnt != 0:
            print(-1)
            exit()

        answer += '.'
        cnt = 0



if cnt > 0:
    if cnt % 2 != 0:
        print(-1)
        exit()
    answer += 'AAAA' * (cnt // 4)
    if cnt % 4 == 2:
        answer += 'BB'

print(answer)