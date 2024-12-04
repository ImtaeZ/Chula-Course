# 1 first_case = {idol_name : vote}
# 2 nd_case = {idol : {ota1,ota2}}
# 2 --> res = [-len(nd_case[idol]), idol].sort()
# 3 rd_case = {ota : {idol : vote}].sort()[0][1]}
# kami = {idol : kami_no}
# res = [-kami_no, idol][:3][1]


first_case = {}
nd_case = {}
rd_case = {}

while True:
    x = input().split()
    if len(x) == 1:
        break
    ota, idol, votes = x
    if idol not in first_case:
        first_case[idol] = -int(votes)
    else:
        first_case[idol] -= int(votes)
    if idol not in nd_case:
        nd_case[idol] = {ota,}
    else:
        nd_case[idol].add(ota)
    if ota not in rd_case:
        rd_case[ota] = {idol : int(votes)}
    else:
        if idol not in rd_case[ota]:
            rd_case[ota][idol] = int(votes)
        else:
            rd_case[ota][idol] += int(votes)
    
        
if x == ['1']:
    result = []
    for idol in first_case:
        result.append([first_case[idol],idol])
    result.sort()
    print(result[0][1]+', '+result[1][1]+', '+result[2][1])
    
if x == ['2']:
    result = []
    for idol in nd_case:
        result.append([-len(nd_case[idol]), idol])
    result.sort()
    print(result[0][1]+', '+result[1][1]+', '+result[2][1])
    
if x == ['3']:
    result = {}
    for ota in rd_case:
        kami = []
        for idol in rd_case[ota]:
            kami.append([-rd_case[ota][idol],idol])
            if idol not in result:
                result[idol] = 0
        kami.sort()
        nonkami = kami[0][1]
        if nonkami in result:
            result[nonkami] += 1
    ans = []
    for idol in result:
        ans.append([-result[idol],idol])
    ans.sort()
    print(ans[0][1]+', '+ans[1][1]+', '+ans[2][1])
