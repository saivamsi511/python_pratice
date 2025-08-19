intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
ans =[]
for [x,y] in intervals:
    if not ans or x>ans[-1][1]:
        ans.append([x,y])
    elif ans[-1][1]<y:
        ans[-1][1] = y
print(ans)