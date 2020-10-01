def SumOfAllMultiples(value_1,value_2,value_3):
    sum = 0
    for i in range(1,value_3):
        if (i % value_1 == 0 or i % value_2 == 0):
            sum += i
    return sum
print(SumOfAllMultiples(3,5,1000))

