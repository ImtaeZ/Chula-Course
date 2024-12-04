# enemy = {country : {enemy,...},..}
# Allies = [[a1],[a2],..]
# for c in enemy:
#    for ali in allies:
#        if c in ali:
#           for cn in ali:
#                if cn not in enemy:
#                    enemy[cn] = enemy[c]
#                else:
#                    enemy[cn].add(enemy[c])

allies = []
while True:
    x = input().split()
    if x[0] == 'Ally':
        allies.append(x[1:])
    if x[0] == 'Enemy':
        break

enemy = {}
enemy[x[1]] = {x[2],}
enemy[x[2]] = {x[1],}
countries = {x[1],x[2]}
while True:
    x = input().split()
    if x[0] == 'Enemy':
        if x[1] not in enemy:
            enemy[x[1]] = {x[2],}
        else:
            enemy[x[1]].add(x[2])
        if x[2] not in enemy:
            enemy[x[2]] = {x[1],}
        else:
            enemy[x[2]].add(x[1])
        countries.add(x[1])
        countries.add(x[2])
    if x[0] == 'Table':
        break
    
for c in countries:
    for ali in allies:
        if c in ali:
            for cn in ali:
                if cn not in enemy:
                    enemy[cn] = enemy[c]
                else:
                    enemy[cn].update(enemy[c])

# add allies of enemy
for cn in enemy:
    ene = sorted(enemy[cn])[0]
    for ali in allies:
        if ene in ali:
            enemy[cn].update(set(ali))

def can_sit(x):
    for i in range(1, len(x)):
        if x[i-1] in enemy:
            if x[i] in enemy[x[i-1]]:
                return False
    return True

if can_sit(x):
    print('Okay')
else: print('No')
while True:
    x = input().split()
    if x == ['End']:
        break
    if can_sit(x):
        print('Okay')
    else:
        print('No')
