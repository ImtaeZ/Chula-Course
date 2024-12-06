w,rw = input().split('/')
w = w.lower()
N = int(input())
x = ''
for i in range(N):
  x += input() + '\n'
  
x = x[:-1]
y = x.replace('\n', ' ')
y = y.lower()
m = y.find(w)
while True:
    if m == -1:
        break
    x = x[:m] + rw + x[m+len(w):]
    y = y[:m] + rw + y[m+len(w):]
    m = y.find(w, m + len(rw))
  
print(x)
