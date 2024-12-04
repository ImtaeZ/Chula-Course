# arabic = ['zero','one','two','three','four','five','six','seven','eight','nine']
# n = int(input())
# print(f"{n} --> {arabic[n]}")

#func ver

def number_name(n):
    arabic = ['zero','one','two','three','four','five','six','seven','eight','nine']
    return arabic[int(n)]

exec(input())