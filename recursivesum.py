# def recursivesum(num):
#     if num>9:
#         i=0
#         s=0
#         while i<num:
#             rem=num%10
#             s=s+rem
#             num=num//10
#         return recursivesum(s)
#     else:
#         print(num)
# recursivesum(num=int(input("enter:")))




# def product( x , y ):
#     if x < y:
#         return product(y, x)
#     elif y != 0:
#         return (x + product(x, y - 1))
#     else:
#         return 0
# x = 3
# y = 5
# print( product(x, y))
 



def printNaturalNumbers(l, u):
  if l > u :
    return
  print(l)
  printNaturalNumbers(l + 1, u)
printNaturalNumbers(1, 5)


