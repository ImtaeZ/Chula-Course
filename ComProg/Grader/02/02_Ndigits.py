num = input()
n = int(input())
zero = max(len(num), n) - len(num)
print("0"*zero + num)