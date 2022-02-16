# [IN]  : A sequence of numbers a[0..n-1], and a number t
# [OUT] : Check if the number t, can be represented as a sum of numbers from a subset of given numbers

# recursion
#            _
#           |   True   if t==0
#  ss(j,t) =|   False  if j==n
#           |_  ss(j+1,t) or ss(j+1,t-a[j])  otherwise
#

def brute(arr : list, t : int) ->bool :
    """returns true if t can be represented as subset sum"""
    n = arr.__len__()
    def ss(j:int, t:int) -> bool:
        nonlocal arr,n
        if t == 0: return True
        if j == n or t<0: return False
        return ss(j+1,t) or ss(j+1, t-arr[j])
    return ss(0,t)

# dynamic programming
# The time complexity is 2^n
# can we do better here?
# What about storing the results in a 2d array for each t in range (0,t) and all j
# base case:
#               table[i][0] = True

def dp(arr: list, t: int)->bool:
    """returns true if t can be represented as subset sum"""
    n = arr.__len__()
    table = [[False for _ in range(1+t)] for _ in range(n)]

    for i in range(n-1,-1,-1):
        for s in range(t+1):
            if s-arr[i]==0 or s==0:
                table[i][s] = True
                continue
            if i==n-1: continue

            if table[i+1][s]:   table[i][s] = True

            if s-arr[i]<0: 
                continue         

            if table[i+1][s-arr[i]]:
                table[i][s] = True
            
    return table[0][t]
            
if __name__ == '__main__':
    a = [3,34,4,12,5,2]
    
    for t in range(50):
        assert dp(a,t) == brute(a,t), "fuck"