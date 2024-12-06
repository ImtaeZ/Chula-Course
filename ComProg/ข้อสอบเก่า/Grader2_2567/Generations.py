gens = {'A':[],'Z':[],'Y':[],'X':[],'B':[],'S':[]}

def check_gen(all_info):
    y = int(all_info[-4:])
    if y >= 2556: gens['A'].append(all_info)
    elif y >= 2540: gens['Z'].append(all_info)
    elif y >= 2524: gens['Y'].append(all_info)
    elif y >= 2508: gens['X'].append(all_info)
    elif y >= 2489: gens['B'].append(all_info)
    elif y >= 2468: gens['S'].append(all_info)
    
while True:
    all = input().strip()
    if all == '-1':break
    check_gen(all)
    
def older(gen):
    check = []
    for ppl in gen:
        name, dmy = ppl.split()
        dmy = dmy.split('/')
        dmy = [int(e) for e in dmy[::-1]]
        dmy += [name]
        check.append(dmy)
    check.sort()
    check.reverse()
    names = []
    for n in check: names.append(n[-1])
    return ' '.join(names)

for i in range(int(input())):
    g = input().strip()
    if older(gens[g]) != '':
        print(g+' : '+older(gens[g]))
    else: print(g+' : Not found')
