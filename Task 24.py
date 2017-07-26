import random
rand_int=random.randint(1,10)
while True:
    choice = int(input("Now guess an number!(between 1 and 10)"))
    if choice==rand_int:
        print("Yep!It's my number")
        break
    if 1<=choice<=10:
        if choice<rand_int:
            print("Lesser")
        if choice>rand_int:
            print("Bigger")
    else: print("Wrong number")
