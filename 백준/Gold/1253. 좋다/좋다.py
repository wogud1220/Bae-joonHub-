import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0

for i in range(N):
    target = arr[i]
    left = 0
    right = N-1

    while left < right:
        # 합은 같은데
        if arr[left] + arr[right] == target:

            # 자기 자신을 사용했을 때
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            # 같은데 자기 자신을 사용안했따면
            else:
                count += 1
                break

        elif arr[left] + arr[right] < target:
            left +=1
        else:
            right -= 1



print(count)
