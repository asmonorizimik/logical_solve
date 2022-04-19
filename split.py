s = 'my name is Manory Zimik'
a = []
x = ''
i=0
while i<len(s):
    if s[i] != ' ':
        x += s[i]
    else:
        a.append(x)
        x =""
    i+=1
a.append(x)
print(a)