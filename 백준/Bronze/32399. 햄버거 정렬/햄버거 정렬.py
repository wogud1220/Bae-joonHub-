import sys


input = sys.stdin.readline

S = input().strip()

if S == "(1)":
    print("0")
elif S == ")1(":
    print("2")
else:
    print("1")