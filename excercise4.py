var_1 = int(input("enter the first variable: "))
var_2 = int(input("enter the second variable: "))
def CheckIfContains3(var_1,var_2):
    sum = var_1 + var_2
    print("the sum is : ",sum)
    if var_1 == 3 or var_2 == 3:
        return "true"
    if ("3" in str(sum)):
        return "true"
    else:
        return "false"
print(CheckIfContains3(var_1,var_2))