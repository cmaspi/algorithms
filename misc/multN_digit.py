x = 325422145
y = 431345189

"""
x*y = (a+b)*(c*d)
Here, a is the first n/2 digits of a and then appended with zeros, while b is last n/2 digits
x*y = a*c + b*d + (a-b)*(c-d)
"""

def multiply(x,y):
    x = str(x)
    y = str(y)
    n = x.__len__()
    if n <= 2:
        return int(x)*int(y)
    nBy2 = n//2
    a = x[:nBy2]
    c = y[:nBy2]
    b = x[nBy2:]
    d = y[nBy2:]

    a,b,c,d = int(a),int(b),int(c),int(d)
    p = multiply(a,c)
    q = multiply(a,d)
    r = multiply(b,c)
    s = multiply(b,d)
    return p*10**( (n-nBy2) * 2)+(q+r)*10**(n-nBy2)+s

print(multiply(x,y))
print(x*y)
    