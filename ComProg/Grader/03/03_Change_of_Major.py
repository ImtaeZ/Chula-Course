s1 = input().split()
s2 = input().split()

s1_ok = s1[2] == "A" and s1[3] <= 'C' and s1[4] <= 'C'
s2_ok = s2[2] == "A" and s2[3] <= 'C' and s2[4] <= 'C'

if not s1_ok and not s2_ok:
    print('None')
elif not s1_ok:
    print(s2[0])
elif not s2_ok:
    print(s1[0])
elif s1[1:] == s2[1:]:
    print('Both')
else:
    if [-float(s1[1]), s1[3:]] < [-float(s2[1]), s2[3:]]:
        print(s1[0])
    else:
        print(s2[0])
        
# func ver
# def choose(s1, s2):
#     s1_ok = s1[2] == "A" and s1[3] <= 'C' and s1[4] <= 'C'
#     s2_ok = s2[2] == "A" and s2[3] <= 'C' and s2[4] <= 'C'

#     if not s1_ok and not s2_ok:
#         return []
#     elif not s1_ok:
#         return [s2[0]]
#     elif not s2_ok:
#         return [s1[0]]
#     elif s1[1:] == s2[1:]:
#         return [s1[0],s2[0]]
#     else:
#         if [-float(s1[1]), s1[3:]] < [-float(s2[1]), s2[3:]]:
#             return [s1[0]]
#         else:
#             return [s2[0]]
        
# exec(input())