import sys
input = sys.stdin.readline


def GCD(a, b):
    while b:
        a, b = b, a%b
    return a


cmd = list(map(int, input().split()))


yaksu = GCD(cmd[0],cmd[1])
basu = cmd[0]*cmd[1]/yaksu

print(int(yaksu), int(basu))