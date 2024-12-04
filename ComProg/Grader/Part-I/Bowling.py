result = input().strip()
target = int(input())
i = 0
total_score = 0
for f in range(1,11):
    if result[i:i+3] == 'XXX':
        score_in_frame_f = 30
        i += 1
    elif result[i:i+2] == 'XX':
        score_in_frame_f = 20 + int(result[i+2])
        i += 1
    elif result[i] == 'X' and result[i+2] == '/':
        score_in_frame_f = 20
        i += 1
    elif result[i] == 'X':
        score_in_frame_f = 10 + int(result[i+1]) + int(result[i+2])
        i += 1
    elif result[i+1:i+3] == '/X':
        score_in_frame_f = 20
        i += 2
    elif result[i+1] == '/':
        score_in_frame_f = 10 + int(result[i+2])
        i += 2
    else:
        score_in_frame_f = int(result[i]) + int(result[i+1])
        i += 2
        
    total_score += score_in_frame_f
    if f == target:
        print(score_in_frame_f)
        
if not 1 <= target <= 10:
    print(total_score)
