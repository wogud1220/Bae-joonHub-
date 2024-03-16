a, b = input().split()
a, b = int(a), int(b)
if a > b:
    print('>')
elif b > a:
    print('<')
else:
    print('==')