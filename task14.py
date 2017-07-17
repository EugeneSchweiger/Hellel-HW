number=int(input("Enter some number.Let's check,is it even."))
def is_even(a):
    if not a%2:
        return True
    else:
        return False
print(is_even(number))