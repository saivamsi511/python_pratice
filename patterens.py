'''
* * * *
* * * *
* * * *
* * * *
def pattern():
    n=int(input())
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end=" ")
        print("\n")
pattern() '''

''' 
* 
* *
* * * 
* * * *

def pattern():
    n=int(input("enter num"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("\n")
pattern()
'''
'''
* * * *
* * *
* * 
* 

def pattern():
    n=int(input("enter num"))
    for i in range(0,n+1):
        for j in range(1,n+1-i):
            print("*",end=" ")
        print("\n")
pattern()
'''
'''
      *
    * *
  * * *
* * * *

def pattern():
    n=int(input("enter num"))
    for i in range(0,n+1):
        for j in range(n,0,-1):
            if j>i:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print("\n")
pattern()
'''
'''
* * * 
  * * 
    * 
      

def pattern():
    n=3
    for i in range(n):#0,1,2
        for j in range(i+1):#0,1,2,3
            print(" ",end=" ")
        for j in range(i,n):#(0,3)
                print("*",end=" ")          
        print(" ")
pattern()
'''

'''
   *
  *  *    
 *  *  *

def pyramid(rows):
    for i in range(rows):#0,1,2
        print(''*(rows-i-1)+"*"*(i+1))
pyramid(5)'''
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end="")
    print()







