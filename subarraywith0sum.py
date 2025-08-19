n=int(input())
arr=[-1,1,3,-2,2,-8,1,7]
s=set()
sum1=0
for i in range(n):
    sum1+= arr[i]
    if sum1 == 0 or sum1 in s:
        print(True)
    s.add(sum1)
print(False)
    