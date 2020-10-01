string_1 = input("input first string: ")
string_2 = input("input second string: ")

def CommonCharactrs(string_1,string_2):
    my_str = " "
    for i in set(string_1):
        if i in string_2:
            my_str += i
    return  my_str
print(CommonCharactrs(string_1,string_2))
