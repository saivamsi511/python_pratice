x,y = map(int,list(input("Enter").split("")))
if (x>0 and y>0):
    print("First quadrant")
elif(x<0 and y>0):
    print("second quadrant")
elif(x<0 and y<0):
    print("third quadrant")
elif(x>0 and y>0):
    print("fourth quadrant")
elif x==0 :
    print("origin")
elif y==0 :
    print("origin")
elif(x!=0 and y==0):
    print("x-axis")
else:
    print("y-axis")