def SumOfAllMultiples(a,b,c):
    sum = 0
    for i in range(1,c):
        if (i % a == 0 or i % b == 0):
            sum += i
    return sum
print(SumOfAllMultiples(3,5,1000))

