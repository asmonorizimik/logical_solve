# list=[1,2,4,7]
#### o/p= [12,14,17,24,27,47]







### o/p=>['11', '14', '13', '19', '41', '44', '43', '49', '31', '34', '33', '39', '91', '94', '93', '99']
list=[1,4,3,9]
i=0
combine_list=[]
while i<len(list):
    j=0
    while j<len(list):
        combine=str(list[i])+str(list[j])
        combine_list.append(int(combine))
        j+=1
    i+=1
print(combine_list)









# l1=[1,2,3]
# l2=[5,6,9]
# #### o/p=[15,16,19,25,26,29,35,36,39]
# i=0
# x=[]
# while i<len(l1):
#     j=0
#     while j<len(l2):
#         c=str(l1[i])+str(l2[j])
#         x.append(c)
#         j+=1
#     i+=1
# print(x)


