arr =[]
string1 = "welcome to geeksforgeeks"
for i in range(97,123):
    arr.append(chr(i))
print(arr)
for i in arr:
    if i not in string1:
        print(i,end=" ")