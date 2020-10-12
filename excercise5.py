def  AreaOfAtriangle(a,b,c):
    #semiperimeter = s
    s = (a + b + c)/2
    t = s * ((s - a) * (s - b) * (s - c))
    if s == a or s == b or s == c or t < 0:
        return "imposible triangle"
    else:
        Area = t ** 0.5
        return Area
print(AreaOfAtriangle(5,4,5))