import cmath
a=1
b=5
c=6
d=b*b - 4*a*c
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print(sol1,sol2)