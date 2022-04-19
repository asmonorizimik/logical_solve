# def backwardprime(i,m):
#     b=[]
#     while i<=m:
#         count=0
#         j=1
#         while j<i:
#             if i%j==0:
#                 count=count+1
#             j=j+1
#         if count==1:
#             if i>10:
#                 x=i%10
#                 y=i//10
#                 z=str(x)+str(y)
#                 b.append(int(z))
#             else:
#                 b.append(i)
#         i=i+1
#     print(b)
#     prime=[]
#     i=0
#     while i<len(b):
#         j=1
#         c=0
#         while j<b[i]:
#             if b[i]%j==0:
#                 c+=1
#             j+=1
#         if c==1:
#             prime.append(b[i])
#         i+=1
#     print(prime)
# backwardprime(i=int(input("enter start number:")),m=int(input("enter last number:")))








# prime=[]
# for k in b:
#     c=0
#     for l in range(1,k):
#         if k%l==0:
#             c+=1
#     if c==1:
#         prime.append(k)
# print(prime)










# n=int(input("enter starting:"))
# m=int(input("enter end:"))
# a=[]
# while n<=m:
#     j=1
#     sum=0
#     while j<n:
#         if n%j==0:
#             sum+=1
#         j+=1
#     if sum==1:
#         a.append(n)
#     n+=1
# print(a)








# b=[12,13,14,15,35,53,43,71,72,19,56,67,76,91]
# prime=[]
# i=0
# while i<len(b):
#     j=1
#     c=0
#     while j<b[i]:
#         if b[i]%j==0:
#             c+=1
#         j+=1
#     if c==1:
#         prime.append(b[i])
#     i+=1
# print(prime)


