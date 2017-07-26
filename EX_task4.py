def daylight_saving(month, week_day, day_of_month):
    m=1<=month<=12
    w=1<=week_day<=7
    d=1<=day_of_month<=31

    if m and w and d:
        if month == 3 :
            if week_day == 7:
                if 24< day_of_month <= 31:
                    print("clock adjustment need:")
                    return 1

        elif month == 10 :
            if week_day == 7 :
                if 24 < day_of_month <= 31:
                    print("clock adjustment need:")
                    return -1
        else:
            print("clock adjustment not needed")

    else:
        print("date input incorrect")

    return 0
m=int(input('enter month(1-12)'))
w=int(input("enter week day(1-7)"))
d=int(input("enter day itself(1-31)"))
print(daylight_saving(m,w,d))