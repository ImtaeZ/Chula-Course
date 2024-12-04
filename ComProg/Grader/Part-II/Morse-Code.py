filename = input().strip()
fn = open(filename, 'r')
code = fn.readline().strip()
pattern = fn.readline().strip()
if code == 'T2M':
    for line in fn:
        morse = ''

        for e in line.strip() :
            invalid = False
            j = pattern.find('[' + e + ']')
            if j == -1:
                morse = line
                invalid = True
                break
            j += 3
            k = pattern.find('[',j)
            morse += pattern[j:k] + ' '
        if not invalid:
            print(morse.strip())


        else:
            print('Invalid :', morse.strip())


elif code == 'M2T':
    for line in fn:
        morse = ''

        for e in line.strip().split() :
            invalid = False
            j = pattern.find(']' + e + '[')
            if j == -1:
                morse = line
                invalid = True
                break
            morse += pattern[j-1]
        if not invalid:
            print(morse.strip())


        else:
            print('Invalid :', morse.strip())


else:
    print('Invalid code')