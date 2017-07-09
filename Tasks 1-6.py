import math
print("____________________________________________");
print("Task #1");

a=10;
b=20;
c=30;
print("a=",a);
print("b=",b);
print("c=",c);
print("Result of a+b*(c/2) is" , a + b *(c/2));
print("End of Task 1");
print("____________________________________________");

i = 1
while i<6:
    print("*");
    i=i+1;
    if i==6:
        break
print("____________________________________________");
print("Task #2");
a=5;
b=8;
print("a=",a);
print("b=",b);
print("Result of (a2+b2)%2 is",(a**2+b**2)%2); #что то трудновато с математикой вечером.
                                               #Так понимаю оператов "%" возвращает остаток от
                                               #цельного деления на указанное число после оператора?
                                               # Например (2**2)+(2**2)=4+4=8....8 % 2=0,то есть оно целиком поделилось.
                                               #Предположим у нас выходит результат 75:
                                               # .....75 %2 = 74\2(делится целиком) и 1 в остатке,т.к. целиком не делится
print("End of Task #2");
print("____________________________________________");
i = 1
while i<6:
    print("*");
    i=i+1;
    if i==6:
        break


print("____________________________________________");
print("Task #3");
a=15;
b=20;
c=30;
print("a=",a);
print("b=",b);
print("c=",c);
print("Result of (a+b)/12*c%4+b is:", (a+b)/12*c%4+b)
print("End of Task #3");
i = 1
while i<6:
    print("*");
    i=i+1;
    if i==6:
        break
print("____________________________________________");
print("Task #4");
a=15;
b=20;
c=30;
print("a=",a);
print("b=",b);
print("c=",c);
print("Result of (a-b*c)/(a+b)%c is:", round((((a-b*c)/(a+b)%c)),5));
print("End of Task #4");
i = 1
while i<6:
    print("*");
    i=i+1;
    if i==6:
        break
print("____________________________________________");
print("Task #5");
a=25;
b=-100;
c=60;
print("a=",a);
print("b=",b);
print("c=",c);
print("Result of |a-b|/(a+b)3-cos(c)is:", round(((math.fabs(a-b))/(math.fabs(a+b))**3-math.cos(c)),5));
print("End of Task #5");
i = 1
while i<6:
    print("*");
    i=i+1;
    if i==6:
        break
print("____________________________________________");
print("Task #6");
a=150;
b=14;
c=22000000;
print("a=",a);
print("b=",b);
print("c=",c);
print((math.log1p(c)/-b)**4)
print("Result of (ln(1+c)/-b)**4+|a| is", round(((((math.log1p(c)/-b)**4))+math.fabs(a)),5));
print("End of Task #6");