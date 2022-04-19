# def largest_multiple(string):
#     length=len(string)
#     multiple=int(string[0])*int(string[1])
#     i=1
#     while i<length-1:
#         if multiple <int(string[i])*int(string[i+1]):
#             multiple=int(string[i])*int(string[i+1])
#         i+=1
#     return multiple
# print(largest_multiple(input("enter number string: ")))








def largest(string):
    l=len(string)
    if l<=1:
        return string
    elif int(string)<=0:
        return "invalid"
    m=int(string[0])*int(string[1])
    i=1
    while i<l-1:
        x=int(string[i])*int(string[i+1])
        if m <x:
            m=x
        i+=1
    return m
print(largest(input("enter number string: ")))
