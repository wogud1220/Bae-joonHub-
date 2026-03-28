import sys
input = sys.stdin.readline


N = int(input())
arr = [-1]* 11 #관찰 안된경우 -1
cnt = 0


for i in range(N):
    num, location = map(int,(input().split()))

    if arr[num] == -1: # 처음들어온 소일때
        arr[num] = location

    else: # 이미 들어온 소일때
        if arr[num] != location: # 들어온 소가 위치가 다르면 = 다리를 건넌다면
            cnt += 1
        arr[num] = location
        
print(cnt)