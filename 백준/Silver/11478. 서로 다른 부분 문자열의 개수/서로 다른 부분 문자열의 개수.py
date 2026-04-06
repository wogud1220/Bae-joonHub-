import sys
input = sys.stdin.readline
from collections import deque, defaultdict


S = input().strip()
len_S = len(S)

result = set()

for i in range(len_S):
    for j in range(i+1, len_S+1):
        result.add(S[i:j])

#a, b, c, ab, ba이런식으로 추가하는게 아니라 a, ab, abc, aba, abab, ababc이렇게 추가
print(len(result))