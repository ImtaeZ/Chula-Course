n = int(input())
ids = []
ids_ind = 0
time = []
call_ind = 0
dts = []
for k in range(n):
    c = input().split()
    if c[0] == 'reset':
        ids.append(int(c[1]))
    elif c[0] == 'new':
        print('ticket', ids[ids_ind])
        time.append(int(c[1]))
        ids.append(ids[ids_ind] + 1)
        ids_ind += 1
    elif c[0] == 'next':
        print('call', ids[call_ind])
        call_ind += 1
    elif c[0] == 'order':
        dt = int(c[1]) - time[call_ind-1]
        print('qtime', ids[call_ind-1], dt)
        dts.append(dt)
    elif c[0] == 'avg_qtime':
        avg = sum(dts)/len(dts)
        print('avg_qtime', round(avg,4))