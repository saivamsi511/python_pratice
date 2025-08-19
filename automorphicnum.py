# an automorphic number is an integer whose square ends with the given integer

num = 25
squ = pow(num , 2)
mod = pow(10,len(str(num)))
if squ% mod == num:
    print("automorphic number")
else:
    print("not automorphic number")