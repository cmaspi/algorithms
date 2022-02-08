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
def splitable(i):
    if i>=n:
        return True
    else:
        for j in range(i,n):
            if isword(i,j) and splitable(j+1):
                return True
        return False

print(splitable(6))