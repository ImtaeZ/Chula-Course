def no_lowercase(t):
    for pasw in t:
        if 'a' <= pasw <= 'z':
            return False
    return True

def no_uppercase(t):
    for pasw in t:
        if 'A' <= pasw <= 'Z':
            return False
    return True

def no_number(t):
    for pasw in t:
        if '0' <= pasw <= '9':
            return False
    return True

def no_symbol(t):
    for pasw in t:
        if not ('a' <= pasw.lower() <= 'z' or '0' <= pasw <= '9'):
            return False
    return True

def character_repetition(t):
    for i in range(len(t)-3):
        if t[i] == t[i+1] == t[i+2] == t[i+3]:
            return True
    return False

def check_sequence(t, seq):
    for i in range(len(t)-3):
        if t[i:i+4].lower() in seq:
            return True
    return False

def number_sequence(t):
    seq = '01234567890'
    if check_sequence(t, seq):
        return True
    return check_sequence(t, seq[::-1])

def letter_sequence(t):
    seq = 'abcdefghijklmnopqrstuvwxyz'
    if check_sequence(t, seq):
        return True
    return check_sequence(t, seq[::-1])

def keyboard_pattern(t):
    seq = '!@#$%^&*()_+ qwertyuiop asdfghjkl zxcvbnm'
    if check_sequence(t, seq):
        return True
    return check_sequence(t, seq[::-1])

passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")

if no_lowercase(passw):
    errors.append("No lowercase letters")
    
if no_uppercase(passw):
    errors.append("No uppercase letters")

if no_number(passw):
    errors.append("No numbers")

if no_symbol(passw):
    errors.append("No symbols")
    
if character_repetition(passw):
    errors.append("Character repetition")
    
if number_sequence(passw):
    errors.append("Number sequence")

if letter_sequence(passw):
    errors.append("Letter sequence")
    
if keyboard_pattern(passw):
    errors.append("Keyboard pattern")
    
if len(errors) == 0:
    print('OK')
else:
    for error in errors:
        print(error)