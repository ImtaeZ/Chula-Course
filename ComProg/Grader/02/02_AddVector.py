x = input()[1:-1].split(',')
y = input()[1:-1].split(',')
x = [float(x[0]), float(x[1]), float(x[2])]
y = [float(y[0]), float(y[1]), float(y[2])]
z = [x[0]+y[0], x[1]+y[1], x[2]+y[2]]
print(f"{x} + {y} = {z}")