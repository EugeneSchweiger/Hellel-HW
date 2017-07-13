writer=input("Enter writer's name*birthday date*death date \n date format: \"YYYY-MM-DD\"")
w_list1=writer.split("*")
b_date1=w_list1[1].split("-")
d_date2=w_list1[2].split("-")
if len(w_list1[1])==10 and len(w_list1[2])==10:
    a=0
    while a<len(b_date1):
        b_date1[a]= int(b_date1[a])
        a=a+1
    a=0
    while a<len(d_date2):
        d_date2[a]= int(d_date2[a])
        a=a+1
    age=d_date2[0]-b_date1[0]
    w_list1[0]="\""+w_list1[0]+"\"" #Предположим кон котэ нация.
    print(w_list1[0],",",age)
else:
    print("You have entered wrong writer's dates(year)", )
#Code is working but not complite
#There is a promlem of placing 8 more conditions after
#reformating inputed text. If month,days out of range of 0 and 12\31
#then code should give mesage of wrong date input. Problem is:
#Where is the place for those conditions?!