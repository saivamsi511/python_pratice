head = 2
tail = -2
arr = "HHTTT"
headcount=0
tailcount=0
for i in arr:
    if i =="H":
        headcount +=2
    elif i =="T":
        tailcount -=2
    else:
        print("invalid")
print(headcount)
print(tailcount)
if headcount == "HHH":
    print("head won",headcount)
elif tailcount == "TTT":
    print("tail won",tailcount)