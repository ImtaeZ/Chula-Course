w = input().lower()
N = int(input())
x = ''
for i in range(N):
  x += input() + '\n'
  
x = x[:-1]
y = x.replace('\n', ' ')
y = y.lower()
m = y.find(w)
while True:
  x = x[:m] + '<found>' + x[m:m+len(w)] + '</found>' + x[m+len(w):]
  y = y[:m] + '<found>' + y[m:m+len(w)] + '</found>' + y[m+len(w):]
  m = y.find(w, m + len(w) + 15)
  if m == -1:
    break
  
print(x)