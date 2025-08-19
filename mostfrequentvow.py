string = "saivamsi"
vowels =['a','e','i','o','u']
count = 0
a=0
e=0
k=0
o=0
u=0
for i in string:
    # for j in string:
    if i == "a":
        a +=1
    elif i=="e":
        e+=1
    elif i=="i":
        k+=1
    elif i=="o":
        o+=1
    elif i=="u":
        u+=1
    else:
        pass
print(a,e,k,o,u)
if  a>e and a>k and a>o and a>u:
    print("a",a)
elif e>a and e>k  and e>o and a>u:
    print("e",e)
elif k>a and k>e and k>o and k>u:
    print("i",k)
elif o>a and o>e and o>k  and a>u:
    print("o",o)   
else:
    print("u",u)

        
