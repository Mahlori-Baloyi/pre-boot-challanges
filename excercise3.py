var_1 = int(input("enter the first variable : "))
var_2 = int(input("enter the second variable : "))

def check(var_1,var_2):

    sum = var_1 + var_2
    if var_1 == 65 or var_2 == 65 or sum == 65:
        return "true"
    return "false"
print(check(var_1,var_2))