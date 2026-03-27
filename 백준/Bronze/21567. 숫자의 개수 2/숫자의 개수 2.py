import sys
input = sys.stdin.readline


A = int(input())
B = int(input())
C = int(input())


result = A*B*C
result = str(result)


dap = [0] * 10


for i in range(len(result)):
    if result[i] == "0":
        dap[0] += 1

    elif result[i] == "1":
        dap[1] += 1

    elif result[i] == "2":
        dap[2] += 1

    elif result[i] == "3":
        dap[3] += 1

    elif result[i] == "4":
        dap[4] += 1

    elif result[i] == "5":
        dap[5] += 1

    elif result[i] == "6":
        dap[6] += 1

    elif result[i] == "7":
        dap[7] += 1

    elif result[i] == "8":
        dap[8] += 1

    elif result[i] == "9":
        dap[9] += 1


for i in range(10):
    print(f"{dap[i]}")