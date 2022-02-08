a = list("sunday")
s = list("saturday")

def ed(a,s):
    n = a.__len__()
    m = s.__len__()
    if n == 0:
        return m-n
    if m == 0:
        return n-m
    if a[0] == s[0]:
        return ed(a[1:],s[1:])
    else:
        add_ = 1 + ed(a,s[1:])
        replace_ = 1 + ed(a[1:], s[1:])
        delete_ = 1 + ed(a[1:],s)
        return min(add_,delete_,replace_)

print(ed(a,s))