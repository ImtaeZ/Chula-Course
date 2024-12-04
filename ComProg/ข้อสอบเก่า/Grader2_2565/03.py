cfile = input()
sfile = input()
cf = open(cfile, 'r')
sf = open(sfile, 'r')
colors = []
for color in cf:
    c = color.split()
    colors += c
colors = [c.lower() for c in colors]

t = ''
for s_lines in sf:
    past = s_lines # HIGHLIGHTS!!!
    for color in colors:
        line = past.lower()
        if color in line:
            i = line.find(color)
            line = past[:i] + '<' + color + '>' + past[i:i+len(color)] + '</>' + past[i+len(color):]
            past = line
    t += past
    
print(t)