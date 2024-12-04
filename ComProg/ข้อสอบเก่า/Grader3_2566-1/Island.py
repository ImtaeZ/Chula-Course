next_island = {}
for i in range(int(input())):
    cur_island, travel_island, t = input().split()
    next_island[cur_island] = (travel_island, t)
    
def Check_path(island1, island2):
    time_travel = []
    travel_island = [island1]
    current_island = island1
    
    while current_island != island2:
        if current_island in next_island: # ขาด
            island, t = next_island[current_island]
        else:
            return -1
        
        if island in travel_island: # วนกลับมาที่เดิม
            return -1
        
        time_travel.append(int(t))
        travel_island.append(island)
        current_island = island
        
    return sum(time_travel)

for i in range(int(input())):
    l1, l2 =input().split()
    if Check_path(l1,l2) != -1 and Check_path(l1,l2) != 0:
        print(Check_path(l1,l2))
    else:
        print('Route not found')
