def convertToHrsAndMins(num):
    Hours_mins = int(num / 60)
    minutes = num % 60
    return str(Hours_mins) + " hours, " + str(minutes) + " mins"
print(convertToHrsAndMins(133))