num=21
temp = num
l=[]
sum1 = 0
while(num>0):
    x=num%10
    l.append(x)
    num=num//10
sum1=sum(l)
if temp%sum1 == 0:
    print("harshad number")
else:
    print("not a harshad number")
    

