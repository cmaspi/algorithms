from re import A


global a
a = [2,4,7,1,13,6,5,100,8,14,15]
a = [3,10,2,1,20]
n = a.__len__()

s = [[1 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        skip = s[i][j+1]
        take = s[j][j+1]+1
        if a[i]<a[j]:
            s[i][j] = max(skip,take)
        else:
            s[i][j] = skip


print(s[0][1])
