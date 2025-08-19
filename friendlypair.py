num1=int(input())
num2=int(input())
sum1=0
sum2=0
for i in range(1,num1):
    if num1%i == 0:
        sum1 +=i
print(sum1)
for i in range(1,num2):
    if num2%i == 0:
        sum2 +=i
print(sum2)
if(sum1==num1 and sum2 == num2):
    print("friendly pair")
else:
    print("not friendly pair")

