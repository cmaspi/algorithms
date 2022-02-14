a = list("sunday")
s = list("saturday")

def ed(a,s):
    n = a.__len__()
    m = s.__len__()

    table = [[0 for _ in range(m)] for _ in range(n)]
    # table[i][j] means that a[:i],s[:j]
