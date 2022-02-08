s = "butterfly"

def isword(i,j):
    if i==0 and j==8:
        return True
    elif i==0 and j==5:
        return True
    elif i==1 and j==5:
        return True
    elif i == 0 and j == 2:
        return True
    elif i ==0  and j ==3:
        return True
    elif i==6 and j==8:
        return True
    else :
        return False
n = len(s)

splittable = [False]*n
splittable.append(True)

def splitable():
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if splittable[j+1] and isword(i,j):
                splittable[i] = True
                break
splitable()
print(splittable)

