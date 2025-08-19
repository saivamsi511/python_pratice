num = 6
sum=0
for i in range(1,6):
    if(num%i == 0):
        sum +=i
if sum == num:
    print("number is perfect")
else:
    print("not a perfect number")