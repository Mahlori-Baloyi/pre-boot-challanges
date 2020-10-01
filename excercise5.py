def  AreaOfAtriangle(side_1,side_2,side_3):
    #semiperimeter = s
    s = (side_1 + side_2 + side_3)/2
    t = s * ((s - side_1) * (s - side_2) * (s - side_3))
    if s == side_1 or s == side_2 or s == side_3 or t < 0:
        return "imposible triangle"
    else:
        Area = t ** 0.5
        return Area
print(AreaOfAtriangle(1,2,5))