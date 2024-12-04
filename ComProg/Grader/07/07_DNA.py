dna = input().upper().strip()
cmd = input().strip()
invalid = False
for c in dna:
    if c not in 'AGCT':
        invalid = True
        break
if invalid:
    print('Invalid DNA')
elif cmd == 'R':
    dna_reverse = ''
    for d in dna:
        if d == 'A':
            dna_reverse += 'T'
        elif d == 'T':
            dna_reverse += 'A'
        elif d == 'G':
            dna_reverse += 'C'
        elif d == 'C':
            dna_reverse += 'G'
    print(dna_reverse[::-1])    

elif cmd == 'F':
    a = t= g = c = 0
    for char in dna:
        if char == 'A':
            a += 1
        elif char == 'T':
            t += 1
        elif char == 'G':
            g += 1
        elif char == 'C':
            c += 1
    print(f"A={a}, T={t}, G={g}, C={c}")

elif cmd == 'D':
    pair = input().strip()
    pair_counter = 0
    for i in range(len(dna)-1):
        if dna[i:i+2] == pair:
            pair_counter += 1
    print(pair_counter)
        
else:
    print('Invalid operator')

