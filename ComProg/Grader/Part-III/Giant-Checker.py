pos = input().strip()

row = ''
col = ''
if len(pos) <= 3:
    row = pos[0]
    col = pos[1:]
else:
    ri = pos.find('row')
    ci = pos.find('col')
    cmi = pos.find(',')
    if ri < ci:
        rei = pos.find('=',ri)
        row = pos[rei+1:cmi]
        cei = pos.find('=',ci)
        col = pos[cei+1:]
    else:
        rei = pos.find('=',ri)
        row = pos[rei+1:]
        cei = pos.find('=',ci)
        col = pos[cei+1:cmi]

row = row.strip()
col = col.strip()



valid_row = True
valid_col = True
if not 'a' <= row.lower() <= 'z':
    valid_row = False
if len(row) == 0 or len(row) > 1:
    valid_row = False
for c in col:
    if c not in '0123456789':
        valid_col = False
if len(col) == 0:
    valid_col = False
if valid_col:
    if not 1 <= int(col) <= 52:
        valid_col = False
   
   
   
if not valid_row and not valid_col:
    print('Invalid row and column')
elif not valid_row:
    print('Invalid row')
elif not valid_col:
    print('Invalid column')
else:
    r = 'abcdefghijklmnopqrstuvwxyz'.find(row.lower())
    if r%2 == int(col)%2 :
     print('Black')
    else:
     print('White')




