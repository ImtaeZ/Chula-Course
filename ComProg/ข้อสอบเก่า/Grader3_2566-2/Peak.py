def read_data():
    dat = []
    R = int(input())
    for r in range(R):
        dat.append([int(e) for e in input().strip().split()])
    return dat
def count_peak(data):
    p = 0
    for r in range(1,len(data)-1):
        for c in range(1,len(data[0])-1):
            if data[r][c] > data[r-1][c] and data[r][c] > data[r+1][c] and \
               data[r][c] > data[r][c-1] and data[r][c] > data[r][c+1]:
                p += 1
    return p

exec(input().strip())
