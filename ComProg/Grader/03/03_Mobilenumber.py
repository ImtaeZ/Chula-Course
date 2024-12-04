n = input()
if len(n) == 10 and (n[:2] == '06' or n[:2] == '08' or n[:2] == '09'):
    print('Mobile number')
else:
    print('Not a mobile number')
    
# func ver
def is_mobile_number(n):
    if len(n) == 10 and (n[:2] == '06' or n[:2] == '08' or n[:2] == '09'):
        return True
    else:
        return False
    
exec(input())