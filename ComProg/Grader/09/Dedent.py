for k in range(int(input())):
    line = input()
    for i in range(len(line)):
        if line[i] != '.':
            break
    print(line[i//2:])