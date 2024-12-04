n = int(input())
id_city = {}
order = []
for i in range(n):
    s = input().split(': ')
    city = s[1].split(', ')
    id_city[s[0]] = set(city)
    order.append(s[0])
cmd = input().strip()

found = False
for ids in order:
    if cmd != ids and len(id_city[ids] & id_city[cmd]) > 0:
        print(ids)
        found = True
        
if not found:
    print('Not Found')