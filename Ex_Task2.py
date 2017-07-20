string=input("Enter something")
indx=input("Enter index inside \"< >\"")
def return_something_inside_thml_teg(str,index):
    indx_open="<"+index+">"
    indx_close="</"+index+">"
    str2=str[(str.find(indx_open[:])+3):(str.find(indx_close[:]))]
    return str2
print(return_something_inside_thml_teg(string,indx))

