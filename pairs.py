# array=[10, 20, 20, 10, 10, 30, 50, 10, 20]
array=[1, 1 ,3, 1, 2 ,1, 3, 3, 3, 3]
i=0
occurance={}
while i<len(array):
    if array[i] not in occurance:
        occurance[array[i]]=1
    else:
        occurance[array[i]]+=1
    i+=1
print(occurance)
pair_count=0
pair=0
for value in occurance:
    if occurance[value]//2==1 or occurance[value]%2==0:
        pair_count+=1
    if occurance[value]//2==2:
        pair+=1
print(pair_count+pair,"pairs")




# def pair(i,array): 
#     occurance={}
#     while i<len(array):
#         if array[i] not in occurance:
#             occurance[array[i]]=1
#         else:
#             occurance[array[i]]+=1
#         i+=1
#     print(occurance)
#     pair_count=0
#     pair=0
#     for value in occurance:
#         if occurance[value]//2==1 or occurance[value]%2==0:
#             pair_count+=1
#         if occurance[value]//2==2:
#             pair+=1
#     return pair_count+pair,"pairs"
# print(pair(0,[1,1,2,2,3,3,4,4,5,4,4,3,3,2,2]))
