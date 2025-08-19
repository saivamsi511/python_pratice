'''a=10
b="vamsi"
c=10.5
d=True
e=(1,2,3)
f={1,2,3}
g=[1,2,3]
h={1:"vamsi",2:"sai"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(a,b,c,d,e,f,g,h)
a=float(10)#explict typecasting
print(a)
a,b="vamsi","sai"
print(a)
def myfun():
    global x
    x=10
    print('value of x is',x)
myfun()
print(x)
a=1j      #complex
print(type(a))
a="sai vamsi"
#print(a[-7:])
print(a.upper())
print(a.lower())
print(a.strip())
a=20
b=10
print(a/b)#arithmetic operatios
print(a%b)
print(a<=b)#comparison operator
#logical operators
print(a and b)
print(a or b)
#identity operator
print(a is b)
print(a is not b)
#membership operator 
#print(a in b)
#print(a not in b)
#bitwise operators
list=["sai","vamsi","pavan","praneeth","king","sai"]
list[1]="king"
list[4]="vamsi"
list.append("pspk")
list.insert(1,"vamsis")
list.remove("vamsis")
x=0
#print(list[-6])
for x in list:
    print(x)
while x<len(list):
    print(list(x))
    x=x+1
#tuple
t=("sai","vamsi","pavan","praneeth","king","sai")#ordered,unchangable,indexed,allow duplicates
x=list(t)
x.append("vamsi")
t=tuple(x)
print(t)
#sets
set={"sai","vamsi","pavan","praneeth","king","sai"}
set.add("pspk")
print(set)
#dictionari
dict={1:"sai",2:"vamsi",3:"pavan",4:"praneeth"}
print(dict)
a=dict.values()
print(a)
#if-else statements
a=10
b=20
c=30
if a>b and a>c:
    print("a id big")
elif b>a and b>c:
    print('b is big')
else:
    print("c is big")
#while loop
i=1
while i<10:
    print(i)
    if i == 5 :
        break
    i+=1
i=1
while i<6:
    print(i)
    if i==3:
        continue
    i+=1
for x in range(3,10,):         
    if x==5:                        
        break                       
    print(x)
for x in range(3,10,):
    if x==5:
        continue
    print(x)
i=100
while i>=1:
    print(i)
    i-=1

n=int(input("Enter the number:-"))
i=1
while i<=10:
    if i==3:
        i=i+1
        continue
    print(i)
    i=i+1
list=[1,4,9,25,36,49,64,81,100]
x=36
i=0
while i<len(list):
    if list[i]==x:
        print("found")
    i=i+1
n=int(input("Enter the number:-"))
for i in range(11):
    print(i*n)
n=int(input("Enter the Number:-"))#3
i=1
sum=1
while i<=n: #1<=3
    sum=sum*i    #1*1
    i+=1        
print(sum)
n=int(input("Enter the Number:-"))  #2
for i in range(0,n):#row 0,1
    for j in range(0,i+1):#column 0,2=0,1
        print(j+1,end=" ")#1,1,2
    print()
def myfun(list):
    print(len(list))
list=['1','2','3','4']
myfun(list)

list=['1','2','3','4']
def fun(list):
    for x in list:
        print(x,end=" ")
fun(list)

#5!=5*4*3*2*1=120
def fact(n):
    return 1 if (n==1 or n==0) else n*fact(n-1)#n=3  3*2*1
print(fact(5))

def convert(usd):
    if usd:
        return usd*83
u=100
print(u,"USD =",convert(u),"INR")

def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
a=5
print(sum(a))

def print_list(list,index=0):
    if(index==len(list)):
        return 
    print(list[index])
    print_list(list,index+1)
cars=["bmw","audi","benz","mg"]
print_list(cars)

f=open("vamsi.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

def check_for_line():
    word="vasi"
    data=True
    line=1
    with open("pratice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line)
                return
            line+=1
    return -1
print(check_for_line())

count=0
with open("vamsi.txt","r") as f:
    data=f.read()
    num=data.split(",")
    for i in num:
        if(int(i)%2==0):
            count+=1
print(count)

import os
os.remove("vamsi.txt")
#OOPS
class Student:
    name="vamsi"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi",s1.name, "your avg marks is:-",sum/3)

s1=Student("sai",[98,97,99])
s1.get_avg()

class Account:
    def __init__(self,bal,acc):
        self.balanc=bal
        self.acc_no=acc
    def debit(self,amount):
        self.balanc -=amount
        print("RS",amount,"has been debited")
        print("Total available balance is",self.balanc)
    def credit(self,amount):
        self.balanc +=amount
        print("RS",amount,"has been credited")
        print("Total available balance is",self.balanc)
    def get_bal(self):
        return self.balanc
s1=Account(100000,12345)
s1.debit(10000)
s1.credit(5000)
#Abstraction:-hiding the classes and objects and show the essential information to the user is know as Abstraction
#ENCAPSULATION:-wrapping the functions and classes into a single unit 

class car:
    def __init__(self):
        self.br=False
        self.acc=False
        self.clu=False
    def start(self):
        self.acc=True
        self.clu=True
        print("car started...")
    def stop(self):
        self.clu=False
        print("car stoped...")
car1=car()
car1.stop()
age=90
name="vamsi,sai {}"
print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace("v","m"))
print(name.split(","))
print(name.format(age))

txt="Sai Vamsi"
x=txt.find("sai")
print(x)

class student:
    def __init__(self,name):
        self.name=name
s1=student("saivamsi")
print(s1.name)
del s1
print(s1)

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def __acc1(self):
        print(self.__acc_pass)
    def wlcome(self):
        self.__acc1()
acc=account(123455,"abcfa")
print(acc.acc_no)
print(acc.wlcome())
#inheritence=copying all the properties of the parent to the child class 
#3 types=single inheritence ,multi level inheritence ,multiple inheritence

class car:
    @staticmethod
    def start():
        print("car started:..")
    @staticmethod
    def stop():
        print("car stoped:..")  
class toyatacar(car):
    def __init__(self,brand):
        self.brand=brand

class fortuner(toyatacar):
    def __init__(self, type):
        self.type=type

car1=fortuner("Disel")
car3=fortuner("petrol")
car2=fortuner("electric")
print(car2.start())

class A:
    var="Welcome to class a"
class B:
    var2="Welcome to class b"
class c(A,B):
    var3="Welcome to class c"
c1=c()
print(c1.var)
print(c1.var2)
print(c1.var3)
#super()
class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started:..")
    @staticmethod
    def stop():
        print("car stoped:..")  
class toyatacar(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()

car1=toyatacar("fortuner","disel")
print(car1.type)

#@classmethod
class person:
    name="vamsi"
    #def changename(self,name):
        #self.__class__.name=name
    @classmethod
    def changename(self,name):
        self.name=name
p1=person()
p1.changename("sai")
print(p1.name)
print(person.name)

#@property
class student:
    def __init__(self,phy,chem,soc):
        self.phy=phy
        self.chem=chem
        self.soc=soc
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.soc)/ 3) + "%"

s1=student(98,99,64)
print(s1.percentage)
s1.phy=67
print(s1.percentage)

#polymorphism

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownum(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,num2):
        newre=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newre,newimg)
    def __sub__(self,num2):
        newre=self.real-num2.real
        newimg=self.img-num2.img
        return complex(newre,newimg)
    def __mul__(self,num2):
        newre=self.real*num2.real
        newimg=self.img*num2.img
        return complex(newre,newimg)
num1=complex(3,4)
num2=complex(7,2)
num1.shownum()
num2.shownum()
num3=num1*num2
num3.shownum()


class circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius
c1=circle(21)
print(c1.area())
print(c1.perimeter())

from typing import Any


class employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def showdetails(self):
        print(self.role)
        print(self.dept)
        print(self.sal)
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("manager","it","483833")
    def showdetails(self):
        print(self.name)
        print(self.age) 
        print(self.role)
        print(self.dept)
        print(self.sal)
eng1=engineer("sai",30)
eng1.showdetails()

class order:
    def __init__(self,items,price):
        self.items=items
        self.price=price
    def __gt__(self,ord2):
        return self.price > ord2.price

ord1=order("chips",50)
ord2=order("drink",20)
print(ord1>ord2)


import random
num=random.randint(1,100)
while True:
    userinp=int(input("guess the number or quit"))
    if (userinp=="q"):
        break
    userinp=int(userinp)
    if(userinp==num):
        print("you guessed the corcted number")
        break
    elif(userinp>num):
        print("guess lower number..")
    else:
        print("guess higher number..")

import random
import string
pass_len=12
charvalues=string.ascii_letters+string.punctuation+string.digits
print(charvalues)
password=""
for i in range(pass_len):
    password+=random.choice(charvalues)
print(password)'''



