num = input().split()
num = [int(items) for items in num]
num.sort()
num_check = [num[0]]
for i in range(1, len(num)):
    if num[i] != num[i-1]:
        num_check.append(num[i])        
print(len(num_check))
print(num_check[:10])

# x = input().split()
# d = []
# for e in x:
#     d.append(int(e))
# d.sort()
# unique = [d[0]]
# for i in range(1, len(d)):
#     if d[i] != d[i- 1]:
#         unique.append(d[i])
        
# print(len(unique))
# print(unique[:10])