import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N, M = map(int, input().split())



A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = set(A)
B = set(B)

minus_A_len = len(A-B)
minus_B_len = len(B-A)

print(minus_A_len + minus_B_len)