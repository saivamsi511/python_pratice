def parking_slot(arr):
    count = 0
    for i in arr:
        if i =="x":
            print("it is occupied slot")
        elif i == "s":
            print("Empty slot")
            count +=1
            print(count)
        else:
            print("Invalid")
arr =["x","x",'x','s','x','x','s','x','x','s','s','x','x','s','x','x']
parking_slot(arr)