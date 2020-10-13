a = int(input("enter the first variable: "))
b = int(input("enter the second variable: "))
def CheckIfContains3(a,b):
    c = a + b

    if ("3" in str(c)) and (a == 3 or b == 3):
        return "true"

    else:
        return "false"
print(CheckIfContains3(a,b))
