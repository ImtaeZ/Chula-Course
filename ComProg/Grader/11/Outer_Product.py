import numpy as np

def mult_table(nrows, ncols):
    m = np.ndarray((nrows,ncols), int)
    for r in range(nrows):
        for c in range(ncols):
            m[r][c] = (r+1)*(c+1)
            
    return m

exec(input().strip())
