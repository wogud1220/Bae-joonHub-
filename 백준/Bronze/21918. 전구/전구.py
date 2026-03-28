import sys
input = sys.stdin.readline


N, M = map(int,(input().split())) # 전구의 개수, 명령어의 개수


# 두번째 줄은 N개의 전구가 어떤 상태인지 s
arr = list(map(int, input().split())) # N개의 전구 생성해서 배열로 나타냄
# [0, 0, 0, 0, 0, 0, 0, 0]

# 3번재 줄부터 M+2줄까지 정수 a,b,c 입력

for i in range(M):
    a, b, c = map(int, input().split())


    if a == 1:
        arr[b-1] = c

    elif a == 2:
        for i in range(b-1,c): # b~ c-1까지
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0

    elif a == 3:
        for i in range(b-1,c):
            arr[i] = 0

    elif a == 4:
        for i in range(b-1, c):
            arr[i] = 1


arr = map(str,arr)

print(' '.join(arr))