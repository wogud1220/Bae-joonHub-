import sys
input = sys.stdin.readline
from collections import deque, defaultdict
N = int(input().strip())
for _ in range(N):
    stack = []
    flag = 0
    answer = input().strip()

    for i in answer: # answer 한글자씩 읽으면서
        if (i == '(') or (i == '['): # 왼쪽 괄호라면
            stack.append(i)

        elif (i == ')'): # 오른쪽 괄호 나오면 팝해서 ( 뽑아야됨

            if not stack: #스택이 비어있으면
                print('NO')
                flag = 1
                break
            else: # 스택에는 있는데
                if stack.pop() != '(': # ( 뽑아야되는데 [ 뽑으면
                    print('NO')
                    flag = 1
                    break

        elif(i == ']') : # 오른쪽 괄호라면 스택 팝 시키고
            # 오른쪽이 나왓는데 뽑ㅇ르게 없다면
            if not stack:
                print('NO')
                flag = 1
                break
            else: # 스택에는 있는데
                if stack.pop() != '[': # [ 뽑아야되는데 다른 거 뽀ㅃ으면
                    print('NO')
                    flag = 1
                    break

        else: # 영어라면 그냥 컨티뉴
            continue

    if flag == 1:
        continue
    elif not stack:
        print('YES')
    else:
        print('NO')


