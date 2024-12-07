st_power = {}
for i in range(int(input())):
    st, power = input().split(',')
    st_power[st] = int(power)

c_n_st = []
for i in range(int(input())):
    county,state = input().split(',')
    c_n_st.append(county+state)
    
st_rep = {}
st_demo = {}
for i in range(int(input())):
    c,st,rep,dem = input().split(',')
    if (c+st) in c_n_st:
        if st not in st_rep: st_rep[st] = 0
        if st not in st_demo: st_demo[st] = 0
        st_rep[st] += int(rep)
        st_demo[st] += int(dem)
        
reps = 0
demos = 0
for state in st_power:
    if st_rep[state] > st_demo[state]: reps += st_power[state]
    else: demos += st_power[state]
    
print(str(reps)+':'+str(demos))
if reps > demos:
    print('Republican wins')
elif demos > reps:
    print('Democrat wins')
else:
    print('Undecided')
