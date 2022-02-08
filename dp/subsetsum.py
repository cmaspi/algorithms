def ss(a,t):
    if t==0:
        return True
    elif t<0:
        return False
    if not a:
        return False
    n = a.__len__()
    if ss(a[:n-1],t) or ss(a[:n-1],t-a[n-1]):
        return True
    else: return False

a = [3,34,4,12,5,2]
t = 30

print(ss(a,t))
