import numpy as np

def get_column_from_bottom_to_top(A, c):
    return A[:, c][::-1]

def get_odd_rows(A):
    return A[1::2, :]

def get_even_column_last_row(A):
    return A[-1,::2]

def get_diagonal1(A):
    ir = np.arange(0,A.shape[0],1)
    return A[ir,ir]

def get_diagonal2(A):
    ir = np.arange(0,A.shape[0],1)
    return A[ir,ir[::-1]]

exec(input().strip())
