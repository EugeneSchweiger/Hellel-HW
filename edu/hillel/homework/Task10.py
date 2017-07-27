writer=input("Enter writer's name*birthday date*death date \n date format: \"YYYY-MM-DD\"")
w_list=writer.split("*")

if len(w_list[1])==10 :
    b_year = int(w_list[1][:4])#b_year= Birthday_year
    d_year = int(w_list[2][:4])#d_year= Death year

else:
    print("Incorrect date")
b_month= int(w_list[1][5:7])
b_day=int(w_list[1][8:10])
d_month=int(w_list[2][5:7])
d_day=int(w_list[2][8:10])
#Next code blosk cam be smaller by double-comparing like 0>= var>=13 ,
# but seems I'm doing something wrong and code not working with me/
if b_month <= 0:
    print("wrong birthday month")
elif b_month >=13:
    print("wrong birthday month")
elif d_month <=0:
    print("wrong death month")
elif d_month >=13:
    print("wrong death month")
elif b_day <= 0:
    print("wrong birthday day")
elif b_day >= 31:
    print("wrong birthday day")
elif d_day <= 0:
    print("wrong death day")
elif d_day >= 31:
    print("wrong death day")
else:
    age=(d_year-b_year)
    if age <=0:
        print("Wrong age!Absolutely wrong!Check carefully inputing years.")
    else:
        w_list[0] = "\"" + w_list[0] + "\""  # Предположим кон котэ нация.
        print(w_list[0], ",", age)
