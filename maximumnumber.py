# i=0
# a=[]
# while i<5:
#     user=int(input("enter:"))
#     a.append(user)
#     i+=1
# j=0
# l=0
# while j<len(a):
#     if a[j]>l:
#         l=a[j]
#     j+=1
# k=0
# s=a[k]
# while k<len(a):
#     if a[k]<s:
#         s=a[k]
#     k+=1
# print(l,s)




i=0
a=[]
while i<10:
    num=int(input("enter: "))
    a.append(num)
    i+=1
print(a)
j=0
l=0
s=a[j]
while j<len(a):
    if a[j]>l:
        l=a[j]
    elif a[j]<s:
        s=a[j]
    j+=1
    
print(s)
print(l)