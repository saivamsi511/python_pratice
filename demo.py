'''
print("hello bro")
print("hello" , end =" ")
print("world")

a = 10
print(a)

a = "vamsi"
print(a)

print("king\nsai")
print("king\tsai")



a,b = 10,20
c = a + b
print("a = ",a)
print("b = ",b)
print(c)

d,e = 30,2
print("d = ",d)
print("e = ",e)
print("Product : ",d * e)


a = 10
b = "python"
c = 20.5
d = True
e = None
f = 10 + 20j
g = [1, 2, 3, 4, 5]
h = (1, 2, 3, 4, 5)
i = {1, 2, 3, 4, 5}
j = {"name": "vamsi", "age": 25, "city": "hyderabad"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))



a = "vamsi"
b = 'vamsi'
c = """vamsi
is a
bad boy"""
d = ''vamsi
is
a
good boy''
print(type(a))
print(type(b))
print(type(c))
print(type(d))


a = "saivamsi"
print(a[1])
print(a[0])
print(a[-1])
print(a[-5])
print(a[1:5])
print(a[1:5:2])  # Slicing with step
print(a[1:])  
print(a[:5])
print(a[:3])  
print(a[::-1])
print(a[3:])


a = "saivamsi"
b = "vamsi"
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.count('a'))
print(a.find('vamsi'))
print(b.replace('vamsi', 'sai'))
print(a.startswith('sai'))
print(a.endswith('vamsi'))
print(a.split('a'))
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(a.islower())
print(a.isupper())
print(a.isnumeric())
print(a.strip())
print(a.lstrip())
print(a.rstrip())
b=[1,2,3,4]



# functions in python
# 1. no parametrers - no return type
def greet():
    print("Hello, welcome to Python programming!")

greet()

# 2. with parameters - no return type
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming!")
greet_user("Vamsi")

# 3. no parameters - with return type
def get_greeting():
    return "Hello, welcome to Python programming!"
greeting = get_greeting()
print(greeting)

# 4. with parameters - with return type
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print(f"The sum of 10 and 20 is: {result}")



l = [12,3,4,5,6,76]
print(l)
print(type(l))
l.append(90)
print(l)
l.remove(90)
print(l)

t = (1, 2, 3, 4, 5)
print(t)
print(t.index(3))
print(t.count(2))
print(t)

s = {1, 2, 3, 4, 5}
s.add(6)
print(s)
s.add(1)
print(s)
s.pop()
print(s)
s.remove(2)
print(s)


l1 = [1,2,3,45,6,7,8]
print(l1[1])
print(l1[-1])
print(l1[4])
print(l1[1:])
print(l1[:3])
print(l1[::-1])
print(l1[1:7])
del l1[2]
print(l1)
l1[1] = 11
l1.append(20)
l1.insert(2, 15)
l1.index(6)
l1.pop()
l1.remove(45)
l1.sort()
print(l1)


l1 = list(map(int,input().split()))
print(l1)

for i in l1:
    print(i, end=" ")
print()
l2 = [i * 2 for i in l1]
print(l2)

l1 = [] # or l1 = list()
print(l1)
print(type(l1))

l2 = () # or l2 = tuple()
print(l2)
print(type(l2))

l3 = {} # or l3 = dict()
print(l3)
print(type(l3))

l4 = set() # or l4 = set()
print(l4)
print(type(l4))


# class creation
class car:
    # constructor
    def __init__(self,name,colour,brand,mileage):
        self.name = name
        self.colour = colour
        self.brand = brand
        self.mileage = mileage

# object Creation
car_obj = car("BMW","blue","x4",9)
print("Name: ",car_obj.name)
print("colour: ",car_obj.colour)
print("brand: ",car_obj.brand)
print("mileage: ",car_obj.mileage)

'''

class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    def dis(self):
        print("Name: ",self.name)
        print("Subject: ",self.subject)

class Student(Teacher):
    def __init__(self,name,subject,rollno):
        super().__init__(name,subject)
        self.rollno = rollno

    def dis(self):
        super().dis()
        print("Roll No: ",self.rollno)

# object creation
std = Student("vamsi","python",101)
std.dis()