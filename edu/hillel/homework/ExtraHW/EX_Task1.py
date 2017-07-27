#Ex1
string=input("Enter string")
def str_reverse1(str):
    st2 = "".join([str[len(str)-a-1] for a in range(len(str))])
    return st2
print(str_reverse1(string))
#Ex2
string=input("Enter string")
def str_reverse2(str):
    return str[::-1]
print(str_reverse2(string))


#same Ex2 but shorter
string=input("Enter string")
str_reverse3 = lambda str: str[::-1]
print(str_reverse3(string))