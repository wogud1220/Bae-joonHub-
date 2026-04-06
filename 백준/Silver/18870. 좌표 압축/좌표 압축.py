import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N = int(input().strip())
arr = list(map(int, input().split()))

no_duplicate_arr = set(arr)# 1000 999


sorted_arr = sorted(list(no_duplicate_arr)) #NlogN
# 999 1000

hash = {}

for i,j in enumerate(sorted_arr, start=0): # I가 인덱스 j가 배열 값
    hash[j] = i
    # hash[999] = 0



for i in range(N):
    print(      hash[arr[i]]     ,end = ' ')

