def password(l,u,p,d):
    s = input("Enter a Password: ")
    if (len(s) >= 8): 
        for i in s:  
            if (i.islower()): 
                l+=1 
            if (i.isupper()): 
                u+=1			 
            if (i.isdigit()): 
                d+=1
            if i.isalnum():		
            # if(i=="@"or i=="$" or i=="_" or i=="#" or i=="%" or i=="^" or i=="&" or i=="*"): 
                p+=1		
    if (l>=1 or u>=1 or p>=1 or d>=1 and l+p+u+d==len(s)): 
        print("Valid Password") 
    else: 
        print("Invalid Password")
password(0,0,0,0)