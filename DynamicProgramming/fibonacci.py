# recursion
def f(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else :
        return f(n-1)+f(n-2)

# dp -1
def fib(n):
    arr = [0,1]
    for i in range(2,n+1):
        arr.append(arr[-1]+arr[-2])
    return arr[n]

print(fib(100))

def fibL(n):
    l2 = (0,1)
    for i in range(2,n+1):
        # temp = l2[1]
        # l2[1] += l2[0]
        # l2[0] = temp
        l2[0],l2[1] = l2[1], l2[0]+l2[1]
    return l2[1]

print(fib(98))

