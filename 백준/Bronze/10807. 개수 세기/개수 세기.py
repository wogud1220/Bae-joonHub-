n = int(input())  #총 배열의 길이

arr = []
arr = input().split()  #입력 받은 배열

find_num = input()  #내가 찾는 수

cnt = 0
for i in range(n):
    if(find_num == arr[i]):
        cnt+=1
print(cnt)