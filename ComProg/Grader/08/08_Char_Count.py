letters = input().strip().lower()
l_map = {}
for let in letters:
    if let in 'abcdefghijklmnopqrstuvwxyz':
        if let in l_map:
            l_map[let] += 1
        else:
            l_map[let] = 1

l_list = []
for char in l_map:
    l_list.append([-l_map[char], char])

l_list.sort()
# for i in range(len(l_list)):
#     print(l_list[i][1], '->', -1*l_list[i][0])
for count, char in l_list:
    print(char, '->', -count)