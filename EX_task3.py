string=input("inter python_style text")
def python_style2JavaStile(str):
    str1= str.split("_")
    str2="".join([str1[a].capitalize() for a in range(len(str1))])
    return str2
print(python_style2JavaStile(string))



