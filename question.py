num  = int(input())
arr = list(map(int,input().split()))
sum=1

for i in arr:
    sum=sum*i
    print(sum)