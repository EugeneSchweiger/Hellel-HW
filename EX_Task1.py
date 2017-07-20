#Ex1
string=input("Enter string")
def reverse(str):
    st2 = "".join([str[len(str)-a-1] for a in range(len(str))])
    return st2
print(reverse(string))
#Ex2
string=input("Enter string")
def reverse(str):
    return str[::-1]
print(reverse(string))


#same Ex2 but shorter
string=input("Enter string")
reverse = lambda str: str[::-1]
print(reverse(string))