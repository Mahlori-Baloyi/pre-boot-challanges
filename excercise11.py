a = input("input first string: ")
b = input("input second string: ")

def CommonCharactrs(a,b):
    my_str = " "
    for i in set(a):
        if i in b:
            my_str += i
    return  my_str
print(CommonCharactrs(a,b))
