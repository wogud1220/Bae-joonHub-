import sys; input=sys.stdin.readline

t=int(input())
for _ in range(t):
    a,b = map(int,input().split())
    a = str(a)
    a = int(a[-1])

    if a == 1 or a == 5 or a == 6: print(a)
    
    # 4 번씩 반복되는 값들
    elif a == 2 or a == 3 or a == 7 or a == 8 :
        b%=4
        if b == 0 : # b = 4
            print(a**4%10)
        else: 
            print(a**b%10)

    # 2 번씩 반복되는 값들
    elif a == 4 or a == 9 : 
        # 홀수일 때 4, 9 / 짝수일 때 6, 1
        if b % 2 != 0:
            print(a)
        else:
            print(a*a%10)
    elif a == 0 :
        print(10)