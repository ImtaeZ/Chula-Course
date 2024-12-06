total_distance = float(input())
jump_factor = float(input())
end_gap = float(input())
pit_start = float(input())
pit_end = float(input())

traveled = 0
jump = 0
while True:
    traveled += jump_factor * (total_distance-traveled)
    jump += 1
    if (pit_start != -1) and (pit_start <= traveled <= pit_end):
        traveled = pit_end
        
    if (total_distance - traveled) <= end_gap:break
    
print(jump)
