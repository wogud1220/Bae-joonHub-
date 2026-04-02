import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0

for i in range(N):
    val = arr[i]
    left = 0
    right = N - 1

    # 합이 val이더라도 인덱스가 i와 겹치면 계속 돌아야 하므로 조건을 수정합니다.
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == val:
            # 합은 맞는데, 사용하는 숫자가 자기 자신(인덱스 i)인지 확인
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                # 둘 다 자기 자신이 아니라면 "좋은 수" 확정!
                count += 1
                break # 이 숫자는 확인 끝났으니 다음 i로 넘어감
        
        elif current_sum < val:
            left += 1
        else:
            right -= 1

print(count)