num = 21
sum=0
for i in range(1,num):
    if num%i == 0:
        sum +=i
print(sum)
if sum>num:
    print("It is a Abundant number")
else:
    print("It is not a Abundant number")
    