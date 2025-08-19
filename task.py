list=[]
def weights():
    ele=input("Enter the element:-")
    list.append(ele)
    print(list)
while True:
    weights()

for i in range(list):
    if i%2==0:
        print("Even")
    else:
        print("Odd")
