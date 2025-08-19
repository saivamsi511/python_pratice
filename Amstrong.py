#cubes of a number = number ex:153

num=153
temp=num    #153
order = len(str(num))   #3
sum = 0
while num!= 0:
    digit = num % 10    #153%10 =3,15%10=5,1%10=1
    sum = sum +(digit**order) #3*3=27,5*3=125,1*3=1
    num=num//10     #15,1,0
if temp == sum:
    print("Amstrong")
else:
    print("not Amstrong")