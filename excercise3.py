a = int(input("enter the first variable : "))
b = int(input("enter the second variable : "))

def check(a,b):

    c = a + b
    if a == 65 or b == 65 or c == 65:
        return "true"
    return "false"

print(check(a,b))

