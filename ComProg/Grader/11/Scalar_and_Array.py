import numpy as np

def toCelsius(f):
    return (f-32)/9*5

def BMI(wh):
    w = wh[:,0]
    h = wh[:,1]
    return w/(h/100)**2

def distanceTo(p, Points):
    x = Points[:,0] - p[0]
    y = Points[:,1] - p[1]
    d = (x**2+y**2)**0.5
    return d

exec(input().strip())
