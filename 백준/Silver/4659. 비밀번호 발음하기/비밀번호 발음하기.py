import sys
input = sys.stdin.readline

vowels = "aeiou"

while True:
    v_count = 0
    c_count = 0
    no = 0

    cmd = input().strip()
    if cmd == "end":
        break

    if not ('a' in cmd or 'e' in cmd or 'i' in cmd or 'o' in cmd or 'u' in cmd):
        print(f"<{cmd}> is not acceptable.")
        no +=1
        continue


    if no == 0:
        for i in range(len(cmd)):
            if cmd[i] in vowels:
                v_count +=1
                c_count = 0
            else:
                c_count +=1
                v_count = 0
            if v_count == 3 or c_count == 3:
                print(f"<{cmd}> is not acceptable.")
                no += 1
                break

    if no == 0:
        for i in range(len(cmd)):
            if len(cmd) == 1:
                break
            if i > 0 and cmd[i] == cmd[i - 1] and cmd[i] not in ("e", "o"):
                print(f"<{cmd}> is not acceptable.")
                no += 1
                break
    if no == 0:
        print(f"<{cmd}> is acceptable.")







