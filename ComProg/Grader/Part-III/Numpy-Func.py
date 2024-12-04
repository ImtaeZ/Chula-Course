import numpy as np

def eq(A, B, p):
     n = (A == B)
     percen = np.mean(n) * 100
     if percen >= p:
         return True
     return False

def closest_point_indexes(points, p):
    dis_x = points[:,0] - p[0]
    dis_y = points[:,1] - p[1]
    distance = (dis_x**2 + dis_y**2)**0.5
    closest = np.min(distance)
    return np.arange(0,len(distance))[closest == distance]

def number_of_inversions(A):
    pair = 0
    for i in range(len(A)-1):
        pair += np.sum(A[i] > A[i+1:])
    return pair

exec(input().strip())
