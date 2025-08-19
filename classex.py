class student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)

std = student("vamsi",20,"hyderabad")
std.display()
std1 = student("sai",21,"hyderabad")
std1.display()