f_name = ['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah']
n_name = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
N = int(input())
for i in range(N):
    name = input()
    if name in f_name:
        print(n_name[f_name.index(name)])
    elif name in n_name:
        print(f_name[n_name.index(name)])
    else:
        print('Not found')