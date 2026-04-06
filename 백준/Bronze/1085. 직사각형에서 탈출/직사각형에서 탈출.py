import sys
input = sys.stdin.readline
from collections import deque, defaultdict


x, y, w, h = map(int, input().split())


up_sero = h - y
right_garo = w - x
sero_result = 0
garo_result = 0


if up_sero < y:
    sero_result = up_sero
else:
    sero_result = y

if right_garo > x:
    garo_result = x
else:
    garo_result = right_garo

result = min(sero_result, garo_result)
print(result)
