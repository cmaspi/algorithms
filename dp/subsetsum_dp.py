
a = [3,34,4,12,5,2]
T = 30

def ss(a,T):
    n = a.__len__()
    table = [[False for _ in range(T+1)] for _ in range(n)]
    for i in range(n):
        for t in range(T+1):
            # print(i,t)
            if i == 0:
                if a[i] == t:
                    table[i][t] = True
                continue
            if t == 0:
                table[i][t] = True
                continue
            if table[i-1][t]:
                table[i][t] = True
                continue
            if t-a[i]>=0 and table[i-1][t-a[i]] :
                table[i][t] = True
            
    return table[n-1][T]

print(ss(a,T))