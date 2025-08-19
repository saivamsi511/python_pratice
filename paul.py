arr = [1,2,3,4,5]
avg = (arr[-1]+arr[-2])/2
print(avg)
for i in arr:
    if i<avg:
        i = 0
        print(i)
    elif i>=avg:
        print(i)
        pass
print(avg+i)

