#oops-object oriented programming language
#to map with real world scenarios,we started using objects in code. This is called oops
#procedural programming language means - executing the code in a sequence line by line
#functions - resuability of code or block of code
#redundancy (decrese) resuability (increase)
# functional programming

"""
class:-blueprint of an object
object:-Real world entity or thing
abstraction:-hidding the implementation of a class and only showing the essential features to the user
encapsulation:-wrapping data and functions into a single unit(object)
inheritence:-when one class(child/derived) derives the properties and methods of another class(parent/base)
types of inheritence:-
1)single inheritence
2)multi-level inheritence
3)multiple inheritence 
class attributes
object attributes
 @staticmethod-decarator changes the behaviour and returns it
 del keywoard is used to delete the class that is not used 
 ex:-class Student:
s1=student("vamsi",21,"male")
del s1
Private class :- (__ defore attribute)
private attributes and methods are meant to be used only within the class and are not accessible from outside the class
super method :- it is used to access methods of the parent class
class method:- A class method is bound to the class and receives the class as an implicit first argument
Note:-static method can't access or modify class state and generally for utility

class student:
    college="N.B.K.R"
    def __init__(self,name,age,gender):#__init__=constructor python will automatically create this 
        self.name=name
        self.age=age
        self.gender=gender

        
    
s1=student("vamsi",21,"male")
s2=student("sai",20,"male")
s3=student("mithun",21,"male")
s4=student("srinadh",21,"male")

print(s1.gender)


class Student:
    college="N.B.K.R"
    
    @staticmethod
    def hello():
        print("hello")

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1=Student("Vamsi",[32,34,97])
s2=Student("sai",[22,64,47])
s=sum(s1.marks)
print(s/3)


#example for abstraction
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def car_start(self):
        self.clutch=True
        self.acc=True
        print("car started...")

car1=Car()
car1.car_start()


class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amount):
        debit=self.balance-amount
        self.balance=debit
        print("Total balance After debit:-",debit)

    def credit(self,amount):
        credit=self.balance+amount
        self.balance=credit
        print("Total balance after credit :-",credit)

acc1=Account(100000,34742310001006)
acc1.debit(100000)
acc1.credit(10)


#example for single inheritence
class Car:
    colour="black"
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def car_start(self):
        self.clutch=True
        self.acc=True
        print("car started...")

    def car_stop(self):
        self.clutch=False
        print("car stoped...")

class Toyatocar(Car):
    def __init__(self,name):
        self.name=name
car1 = Toyatocar("forthuner")
car2 = Toyatocar("prius")

print(car1.colour)
car1.car_start()


#multi level inheritence

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def car_start(self):
        self.clutch=True
        self.acc=True
        print("car started...")

    def car_stop(self):
        self.clutch=False
        print("car stoped...")

class Toyatocar(Car):
    def __init__(self,brand):
        self.brand=brand

class fortuner(Toyatocar):
    def __init__(self, type):
        self.type=type
    
car1=fortuner("disel")
car1.car_start()



#example for multiple inheritence
class A:
    vara="welcome to class 1"

class B:
    varb="welcome to class 2"

class C(A,B):
    varc="welcome to class 3"

c1=C()
print(c1.vara)
print(c1.varb)
print(c1.varc)

"""

# a=10
# b=5
# c=a.__add__(b)
# c=a.__sub__(b)
# c=a.__mul__(b)
# c=a.__truediv__(b)
# c=a.__mod__(b)
# print(c)

