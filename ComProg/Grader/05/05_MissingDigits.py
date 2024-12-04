num = input()
num_list = ['0','1','2','3','4','5','6','7','8','9']
for number in num:
    if number in num_list:
        num_list.remove(number)
        
if len(num_list) != 0:
    print(','.join(num_list))
else:
    print('None')
