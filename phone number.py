# create_phone_number([2,9,8,7,4,0,1,3,6,5])
# Sample Output 2:
# “(298) 740 1365”

# def create_phone_number(n):
#     cc=""
#     mid=""
#     end=""
#     res=""
#     for i in range(3):
#         cc=cc+str(n[i])
#     for i in range(3,6):
#         mid=mid+str(n[i])
#     for i in range(6,10):
#         end=end+str(n[i])
#     res="("+cc+")"+" "+mid+"-"+end
#     return res
# print(create_phone_number([2,9,8,7,4,0,1,3,6,5]))


def phone(n):
    first=""
    sec=""
    thrd=""
    all=""
    i=0
    while i<len(n):
        if i<3 :
            first=first+str(n[i])
        elif i<6:
            sec=sec+str(n[i])
        elif i<=len(n):
            thrd=thrd+str(n[i])
        i+=1
    all="("+first+")"+" "+sec+"-"+thrd
    print(all)
phone([2,9,8,7,4,0,1,3,6,5])