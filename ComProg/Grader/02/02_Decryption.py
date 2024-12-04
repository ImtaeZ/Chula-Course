code = input()
x1 = code[3::7]
x2 = code[7::5]
x3 = int(x1) + int(x2) + 10000
x4 = str(x3)[-4:-1]
x5 = (int(x4[0]) + int(x4[1]) + int(x4[2])) % 10 + 1
alphabet = " ABCDEFGHIJ"
ans = x4 + alphabet[x5]
print(ans)

# code = input()
# alphabet = {'1':'A','2':'B','3':'C','4':'D','5':'E','6':'F','7':'G','8':'H','9':'I','10':'J'}
# x1 = code[3::7]
# x2 = code[7::5]
# x3 = int(x1) + int(x2) + 10000
# x4 = str(x3)[-4:-1]
# x5 = 0
# for num in x4:
#     x5 += int(num)
# x6 = int(str(x5)[-1]) + 1
# x7 = alphabet[str(x6)]
# ans = x4 + x7
# print(ans)