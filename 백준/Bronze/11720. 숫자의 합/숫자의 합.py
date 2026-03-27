import sys
input = sys.stdin.readline


N = int(input())
num = input()

result = 0

result = sum(int(num[i]) for i in range(N))

print(result)