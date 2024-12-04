N = int(input())
win = set()
lose = set()
for i in range(N):
    w, l = input().split()
    win.add(w)
    lose.add(l)
    
print(sorted(list(win-lose)))
