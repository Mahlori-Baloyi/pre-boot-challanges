def SumOfAllMultiples(a,b,c):
    multiples = 0
    for i in range(1,c):
        if (i % a == 0 or i % b == 0):
            multiples += i
    return multiples
print(SumOfAllMultiples(3,5,1000))

