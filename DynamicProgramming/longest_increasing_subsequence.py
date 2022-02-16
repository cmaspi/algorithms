# [IN]  : A sequence of numbers
# [OUT] : The length of the largest increasing subsequence

# recursion
# LIS[i,j] returns the longest increasing subsequence from j th index all of which are greater than a[i]
#               _
#              |  0 if j == n
#   LIS(i,j) = |  LIS(i,j+1) if a[i]>a[j]
#              |_ max(LIS(i,j+1), LIS(j,j+1)+1) otherwise

def brute(arr : list) -> int :
    """returns the length of the largest increasing subsequene"""
    n = arr.__len__()
    def LIS(i: int, j:int) -> int:
        """returns the longest increasing subsequence starting from index j,
        all of which are greater than arr[i]"""

        nonlocal arr,n
        if j == n: return 0
        if arr[i] > arr[j]: return LIS(i,j+1)
        return max(LIS(i,j+1), LIS(j,j+1)+1)
    return max((LIS(i,i+1) for i in range(n)))+1

# dynamic Programming
# So, what are we repeating?
# each time we want to find LIS(i,i+1), we have to find LIS(i,j) where j is greater than i+1
# also we will have to find LIS(j,j+1) and then it's subproblems
# So, instead we will store these in a 2 dimensional array
# base case
#               table[i][n] = 0


def dp(arr: list) -> int:
    """returns the length of the largest increasing subsequence"""
    n = arr.__len__()
    table = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # def LIS(i: int, j:int) -> int:
    #     """returns the longest increasing subsequence starting from index j,
    #     all of which are greater than arr[i]"""
    #     nonlocal n, table, arr
    for i in range(n-2,-1,-1):
        for j in range(n-1,i,-1):
            skip = table[i][j+1]
            take = table[j][j+1]+1
            if arr[i]<arr[j]:
                skip = max(skip,take)
            table[i][j] = skip
    return max(table[i][i+1] for i in range(n-1))+1

if __name__ == "__main__":
    a = [[50,3,10,7,40,80],[2,4,7,1,13,6,5,100,8,14,15],[3,10,2,1,20],[4,5,1,54,2,54,7,32,13],[1,2,3,4],[4,3,2,1]] 
    for arr in a:
        assert brute(arr) == dp(arr) ,"dp is wrong"
    a = [50,3,10,7,40,80]
    print(dp(a))
    
