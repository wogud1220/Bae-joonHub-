import sys

input = sys.stdin.readline



for i in range(1000):
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    if a == b == c:
        print("Equilateral")

    elif c >= a + b:
        print("Invalid")

    elif a == b or b == c or a == c: # 이등변
        print("Isosceles")

    else:
        print("Scalene")