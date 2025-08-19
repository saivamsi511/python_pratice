def gcd(x,y):
    result = min(x,y)   #min=10
    while result:
        if (x%result==0 and y%result==0):   
            break
        result -=1  #10,9,8,7,6,5
    return result
print(gcd(10,15))