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
            return 0

    else:
        if not m and not w:
            raise ValueError("Invalid input: Incorrect date(month and week day)")
        elif not m and not d:
            raise ValueError("Invalid input: Incorrect date(month and day)")
        elif not w and not d:
            raise ValueError("Invalid input: Incorrect date(week day and day)")
        elif not m:
            raise ValueError("Invalid input: Incorrect date(month)")
        elif not w:
            raise ValueError("Invalid input: Incorrect date(week day)")
        elif not d:
            raise ValueError("Invalid input: Incorrect date(day)")

        else:
            raise ValueError("Invalid input:Incorrect date")

month=int(input('enter month(1-12)'))
week_day=int(input("enter week day(1-7)"))
day=int(input("enter day itself(1-31)"))
print(daylight_saving(month,week_day,day))