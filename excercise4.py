a = int(input("enter the first variable: "))
b = int(input("enter the second variable: "))
def CheckIfContains3(a,b):
    sum = a + b

    if a == 3 or b == 3:
        return "true"
    if ("3" in str(sum)):
        return "true"
    else:
        return "false"

print(CheckIfContains3(a,b))
