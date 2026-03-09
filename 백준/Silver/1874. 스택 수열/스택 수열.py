import sys
input = sys.stdin.readline
num = int(input())
stack = []
current = 1 # 오름차순이니깐 절대 안 내려감
result = []

for _ in range(num):
    target = int(input()) # 처음에 4, 3들어옴, 6들어옴


    while current <= target: # 1<=4, 5<=3 만족 X, 5<=6만족6
        stack.append(current)# (1,2,3,4), (1256),
        result.append("+") # (++++)(++++--+)(++++--++)
        current += 1        # (5),(7)
    # 4까지 넣었음

    if stack[-1] == target: # 4빼내고, 3빼내고, 6빼내고
        stack.pop()
        result.append("-")# (++++-), (++++--)
    else:
        print("NO")
        exit()


for r in result:
    print(r)

