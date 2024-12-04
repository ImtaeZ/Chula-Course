eq = input()
op = []
for num in eq:
    if num in ['-','+']:
        op.append(num)
eq = eq.replace('-',' ')
eq = eq.replace('+',' ')
nums = [int(e) for e in eq.split()]
if len(nums) == len(op):
    sum = -nums[0]
    for i in range(1,len(op)):
        if op[i] == '+':
            sum += nums[i]
        else:
            sum -= nums[i]
            
else:
    sum = nums[0]
    for i in range(len(op)):
        if op[i] == '+':
            sum += nums[i+1]
        else:
            sum -= nums[i+1]
print(sum)
