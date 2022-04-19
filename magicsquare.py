list=[[1,2,3],
      [3,4,5],
      [1,2,2]]
# list=[[8, 3, 4],
#       [1, 5, 9],
#       [6, 7, 2]]
i=0
while i<len(list):
    j=0
    columns=0
    row=0
    while j< len(list[i]):
        columns+=list[i][j]
        row+=list[j][i]
        j+=1
    print(columns,"column",i+1)
    print(row,"rows",i+1)
    i+=1
    c=0
    d=0
    f=(len(list)-1)
    d1=0
    d2=0
    while c<len(list):
        d1=d1+list[c][d]
        d2=d2+list[c][f]
        c+=1
        d+=1
        f-=1
print(d1,"diagonal 1")
print(d2,"diagonal 2")
if row==columns==d1==d2:
    print("magic-square")
else:
    print("not magic-square")
