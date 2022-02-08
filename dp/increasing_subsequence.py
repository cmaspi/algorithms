global a
a = [2,4,7,1,13,6,5,100,8,14,15]
a = [3,10,2,1,20]
a = [3,2]
a = [50,3,10,7,40,80]
n = len(a)
# 2 4 7 8 14
# 2 4 6 8 14
# 2 4 5 8 14
# so max size is 5

def s():
    m = 0
    for i in range(n):
        if m < s_util(i,i+1)+1:
            m = s_util(i,i+1)+1
    return m

def s_util(i,j):
    global a
    if j>=n:
        return 0
    if a[i]<a[j]:
        return max(s_util(i,j+1), s_util(j,j+1)+1)
    else:
        return s_util(i,j+1)

print(s())