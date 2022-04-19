array=[1,2,3,4]
n=int(input("enter the number: "))
i=0
# k=[]
while i<len(array):
    j=0
    while j<len(array):
        sum=array[i]+array[j]
        if sum==n and i<j:
            # k.append((i,j))
            print((i,j),end='')
        j+=1
    i+=1
# print(k)