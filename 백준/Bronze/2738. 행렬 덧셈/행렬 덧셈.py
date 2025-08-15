N, M = map(int, input().split())

# 첫 번째 행렬 입력
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 두 번째 행렬 입력
arr_2 = []
for _ in range(N):
    arr_2.append(list(map(int, input().split())))
    
# 행렬 합 계산 및 출력
for i in range(N):
    for j in range(M):
        print(arr[i][j] + arr_2[i][j], end=' ')
    print()