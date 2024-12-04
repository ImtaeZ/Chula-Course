def hide_vowel(w): # ฟังกช์ นั นี้เขยีนใหแ้ลว้ เรยี กใชไ้ดเ้ลย
# รับ w เป็นสตริง
# คืน สตริงที่เหมือน w แต่ตัวอักษรใดใน w ที่เป็นสระจะถูกแทนด้วยเครื่องหมายดอกจัน *
    h = ""
    for c in w:
        if c.lower() in 'aeiou':
            c = '*'
        h += c
    return h

def less_offensive(t, oword):
    t_l = t.lower()
    for i in range(len(t)-len(oword)):
        if t_l[i:i+len(oword)] == oword.lower():
            t = t[:i] + hide_vowel(t[i:i+len(oword)]) + t[i+len(oword):]
    return t

Owords = input().split()
text = input()

for ow in Owords:
    text = less_offensive(text, ow)
    
print(text)