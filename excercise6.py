def maximum_number(array):
    #high stands for highest number(maximum)
    high = array[0]
    for i in array:
        if high < i:
            high = i
    return(high)
print(maximum_number([1,5,2]))
