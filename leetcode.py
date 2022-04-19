ransom_note="typhon"
megazine="python"
d = {}
for i in megazine:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for j in ransom_note:
    if j in d and d[j]==1:
        print(True)
        break
    else:
        print(False)
        break