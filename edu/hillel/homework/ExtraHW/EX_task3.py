# string=input("inter python_style text")
# def python_style2JavaStile(str):
#     str1= str.split("_")
#     str2="".join([str1[a].capitalize() for a in range(len(str1))])
#     return str2
# print(python_style2JavaStile(string))
#
#

a=input("enter text")
def reverse_no_slice_and_cycle(str):
    b=list(str)
    b.reverse()
    c="".join(b)
    return c
print(reverse_no_slice_and_cycle(a))