# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end='')
#         j+=1
#     k=5
#     n=1
#     while k>=i:
#         print(n,end='')
#         k-=1
#         n+=1
#     i+=1
#     print()





# 1
# 1*2
# 1**3
# 1***4
# 1****5
# 1*****6

i=0
x=1
a=1
while i<=5:
    b="*"*i
    if x==1:
        print(a)
    else:
        print(str(a)+b+str(x))
    i+=1
    x+=1





























# def intToRoman(num):
#     m = ["", "M", "MM", "MMM"]
#     c = ["", "C", "CC", "CCC", "CD", "D",
#          "DC", "DCC", "DCCC", "CM "]
#     x = ["", "X", "XX", "XXX", "XL", "L",
#          "LX", "LXX", "LXXX", "XC"]
#     i = ["", "I", "II", "III", "IV", "V",
#          "VI", "VII", "VIII", "IX"]
#     thousands = m[num // 1000]
#     hundreds = c[(num % 1000) // 100]
#     tens = x[(num % 100) // 10]
#     ones = i[num % 10]
  
#     ans = (thousands + hundreds +
#            tens + ones)
  
#     return ans
# print(intToRoman(int(input("enter the integer number:"))))