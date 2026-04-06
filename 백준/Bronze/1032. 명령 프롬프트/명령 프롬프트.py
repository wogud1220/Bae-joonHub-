import sys

input = sys.stdin.readline


N = int(input())

arr = []



for i in range(N):
    a = input().strip()
    arr.append(list(a))

result = arr[0]

for i in range(N):
    for j in range(0, len(arr[0])):
        if result[j] != arr[i][j]:
            result[j] = '?'
        else:
            continue


print(''.join(result))


