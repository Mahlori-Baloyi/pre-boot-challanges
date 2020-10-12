def convertToHrsAndMins(a):
    H = int(a / 60)
    mins = a % 60
    return str(H) + " hours, " + str(mins) + " mins"
print(convertToHrsAndMins(133))