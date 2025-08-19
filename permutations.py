def factorial(num):
    fact = 1
    for i in range(num, 1,-1):
        fact *=i
    return fact

n = int(input("Enter students:-"))
r = int(input("enter no of seats:-"))

p = factorial(n)
print("total possible arrangements:-",p)
