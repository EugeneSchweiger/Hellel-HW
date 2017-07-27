print("___________________________________")
print("Task7")
print("___________________________________")
date = input("Enter date You want to convert to in format(DD.MM.YYYY):");
print("You entered date:", date,"start converting(yes/no)?")
answer=input()
if answer == "yes":
    print("Let's get started!")
    if len(date) == 10:
        date2 = date.split(".") #Тут нехватает условия else при котором выполнение кода
        #останавливается,либо сразу перескакивает на 34-ю строку.
        #Но,поскольку при несоблюдении условия "len(date) == 10:"
        #выкидывает ошибку,будем считать что всё ок :-)
    a = 0
    while a < len(date2):
        date2[a] = int(date2[a])
        a = a + 1
    month=date2[1]
    if date2[0] >= 32:
        print("Incorrect day's data!")
    elif date2[0]<=00:
        print("Incorrect day's data!")
    elif date2[1] >= 13:
            print("Incorrect month's data!")
    elif date2[1] <= 00:
            print("Incorrect month's data!")
    else:
        date2.insert(0,month)
        date2.pop(2)
        a = 0
        while a < len(date2):
            date2[a] = str(date2[a])
            a = a + 1
        print("Enother date format is:%s.%s.%s"
              %(date2[0],date2[1],date2[2]))
else:
    print("newer mind...")