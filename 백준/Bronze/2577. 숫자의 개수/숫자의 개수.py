a = int(input())
b = int(input())
c = int(input())
result = a*b*c

result = str(result)
num_arr = [0]*10

for i in result:
    if(i == '0'):
        num_arr[0] = num_arr[0] + 1
    elif(i == '1'):
        num_arr[1] = num_arr[1] + 1
    elif(i == '2'):
        num_arr[2] = num_arr[2] + 1
    elif(i == '3'):
        num_arr[3] = num_arr[3] + 1
    elif(i == '4'):
        num_arr[4] = num_arr[4] + 1
    elif(i == '5'):
        num_arr[5] = num_arr[5] + 1
    elif(i == '6'):
        num_arr[6] = num_arr[6] + 1
    elif(i == '7'):
        num_arr[7] = num_arr[7] + 1
    elif(i == '8'):
        num_arr[8] = num_arr[8] + 1
    elif(i == '9'):
        num_arr[9] = num_arr[9] + 1

for i in num_arr:
    print(i)
