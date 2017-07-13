import math
print("___________________________________")
print("Task8")
print("___________________________________")
print("Input first text block")
txt1=input()
print("Input second text block")
txt2=input()
print("You have entered %s and %s"
      %(txt1,txt2))
mid1=(round(len(txt1)/2))
mid2=(round(len(txt2)/2))
txt3=(txt2[:mid2]+txt1+txt2[mid2:])
txt4=(txt1[:mid1]+txt3+txt1[mid1:])
print(txt4)
#Лень усложнять код,но всё работает) Вроде бы.......
