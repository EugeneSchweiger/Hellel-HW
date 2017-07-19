print("There are two spherical null-trains in vacuum"
      "\nFirst with speed=V1,Second speed=V2"
      "\nDistance brtween them is 10km."
      "\nFirst train will turn in 4km to extra railway")
V1=int(input("Enter first train speed(V1)"))
V2=int(input("Enter second train speed (V2)"))

def if_crash(v1,v2,d=10,d1=4):
    if d1/v1>=(d-d1)/v2:
        return True
    else:
        return False
result=if_crash(V1,V2)
print("Wiil they crash?:",result)

