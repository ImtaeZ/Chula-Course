sum = 0
i = 0
while True:
    n = input()
    if n == 'q':
        break
    sum += float(n)
    i += 1

if i != 0:
    print(round(sum/i,2))
else:
    print("No Data")
