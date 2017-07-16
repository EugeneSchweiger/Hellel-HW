number=int(input("Enter some number.Let's check,is it even."))
def is_even(int):
    if (int % 2)== 0:
        return True
    else:
        return False
print(is_even(number))
#Returning boolen is optional,I think... More user-friendly is returning some text