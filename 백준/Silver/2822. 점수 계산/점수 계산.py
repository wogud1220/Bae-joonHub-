import sys
input = sys.stdin.readline


cmd = [0]*8
for i in range(8): # 1~8
    score = int(input())
    cmd[i] = (score, i+1)


a = sorted(cmd,reverse=True)


real_arr=[0]*5
for i in range(5):
    real_arr[i] = a[i]

a = sorted(real_arr, key= lambda X:X[1])

hap = 0
hap = sum(t[0] for t in a)
print(hap)


print(' '.join(str(x[1]) for x in a))

