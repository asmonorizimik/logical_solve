# def first(s):
#       d = {}
#       for i in s:
#          if i not in d:
#             d[i] = 1
#          else:
#             d[i] +=1
#       for i in range(len(s)):
#          if d[s[i]] == 1:
#             return s[i],":",i
#       return -1
# print(first(input("enter:")))









s="loveleetcode"
# s="aabbb"
# s=input("enter:  ")
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
for j in range(len(s)):
    if d[s[j]] == 1:
        print(s[j],":",j)
        break
else:
    print(-1)



