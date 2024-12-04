# fc_cn = {fc : cn}
# country = []
# fc1,fc2,fc3,fc4 loop : if fc in fc_cn: if not in country:.append else : return False if else: return False

fc_cn = {}
for i in range(int(input())):
    fc, cn = input().split()
    fc_cn[fc] = cn

def check(fcs):
    country = []
    for fc in fcs:
        if fc in fc_cn:
            if fc_cn[fc] not in country:
                country.append(fc_cn[fc])
            else:
                return False
        else:
            return False
    return True

while True:
    x = input().split()
    if x == ['q']:
        break
    if check(x):
        print('OK')
    else:
        print('Not Ok')
