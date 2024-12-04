def get_repeat_count(data, pattern):
    if len(data) <= len(pattern):
        return 1
    count = 0
    for i in range(len(data)-len(pattern)):
        if pattern == data[i:i+len(pattern)]:
            first_i = i
            break
    while pattern == data[first_i:first_i+len(pattern)]:
        count += 1
        first_i += len(pattern)
    return count

patt = input()
N = int(input())
for i in range(N):
    datas = input()
    if get_repeat_count(datas, patt) > 1:
        print(get_repeat_count(datas, patt))
    else:
        print(0)