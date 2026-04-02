import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [0] * (K + 1) # 키로별 가치의 배열
# [1]: 1키로일때 최대의 가치, [10]: 10키로 일때 최대 가치

for _ in range(N):
    W, V = map(int, input().split())

    for j in range(K, W - 1, -1):
        if dp[j] < dp[j - W] + V:
            dp[j] = dp[j - W] + V

print(dp[K])