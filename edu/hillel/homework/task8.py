import math
print("___________________________________")
print("Task8")
print("___________________________________")
txt1=input("Input first text block")
txt2=input("Input second text block")
print("You have entered %s and %s"
      %(txt1,txt2))
mid1 = len(txt1)//2
mid2 = len(txt2)//2
txt3=(txt2[:mid2]+txt1+txt2[mid2:])
txt4=(txt1[:mid1]+txt3+txt1[mid1:])
print(txt4)
