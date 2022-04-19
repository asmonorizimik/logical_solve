def remainder(a,b):
    if a>0 and b>0:
        if a%b==0 or b%a==0:
         return True
        elif a>b and a!=0:
            if b!=0:
                return a%b
            else:
                return None
        elif b>a and b!=0:
            if a!=0:
                return b%a
            else:
                return None
        else:
            return "nothing"
    else:
        if a<0:
            return None
        elif b<0:
            return None
print(remainder(a=int(input("enter a: ")),b=int(input("enter b: "))))