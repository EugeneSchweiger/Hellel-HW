string=input("Enter something")
indx=input("Enter index inside \"< >\"")
def return_something_inside_thml_teg(str,tag_letter):
    tag_open="<"+tag_letter+">"
    tag_close="</"+tag_letter+">"
    str2=str[(str.find(tag_open[:])+len(tag_open)):(str.find(tag_close[:]))]
    return str2
print(return_something_inside_thml_teg(string,indx))

