import sys
from collections import deque

T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))


    #(1, 0), (1, 1), (9, 2), (1, 3)]
    # 인덱스도 같이 넣기
    Q = deque([(p, i) for i, p in enumerate(priorities)])

    cnt = 0
    while Q:
        # 0번째 있는거 뽑고
        current = Q.popleft()

        # 나머지 문서들 중 현재보다 중요도가 높은 게 있는지 확인
        if any(current[0] < item[0] for item in Q):
            # 더 중요한 게 있다면 뒤로 보냄
            Q.append(current)
        else:
            # 현재 문서가 가장 중요하다면 인쇄
            cnt += 1
            # 인쇄한 문서가 내가 찾던 M번째 문서라면 종료
            if current[1] == M:
                print(cnt)
                break