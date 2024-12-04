def to_Thai(N):
    num = {0:'soon', 1:'neung', 2:'song', 3:'sam', 4:'si', 5:'ha', 6:'hok', 7:'chet', 8:'paet', 9:'kao', 10:'sip', 20:'yi'}
    out = ''
    if N >= 1000:
        out += num[N//1000] + ' ' + 'pun'
        N %= 1000
        if N >= 100:
            out += ' ' + num[N//100] + ' ' + 'roi'
        N %= 100
        if N >= 10:
            if N < 20:
                out += ' sip'
            elif N < 30:
                out += ' yi' + ' ' + 'sip'
            else:
                out += ' ' + num[N//10] + ' ' + 'sip'
        N %= 10
        if N == 1:
            out += ' et'
        elif N != 0:
            out += ' ' + num[N]
        return out
    if N >= 100:
        out += num[N//100] + ' ' + 'roi'
        N %= 100
        if N >= 10:
            if N < 20:
                out += ' sip'
            elif N < 30:
                out += ' yi' + ' ' + 'sip'
            else:
                out += ' ' + num[N//10] + ' ' + 'sip'
        N %= 10
        if N == 1:
            out += ' et'
        elif N != 0:
            out += ' ' + num[N]
        return out
    if N >= 10:
        if N < 20:
            out += 'sip'
        elif N < 30:
            out += 'yi' + ' ' + 'sip'
        else:
            out += num[N//10] + ' ' + 'sip'
        N %= 10
        if N == 1:
            out += ' et'
        elif N != 0:
            out += ' ' + num[N]
        return out
    else:
        out += num[N]
        return out
        
        
exec(input().strip())