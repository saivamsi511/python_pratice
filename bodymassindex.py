weight = int(input("Enter weight:-"))
height = float(input("Enter height:-"))
formula  = weight/(height * height)
if formula<18:
    print("0")
elif 18<=formula<25:
    print("1")
elif 25<=formula<30:
    print("2")
elif 30<= formula <40:
    print("3")
elif formula>=40:
    print("4")
else:
    print("Invalid")