"""
test4
"""

mult=1
while True:
    n = input("Enter 5-digits number")
    if len(n)==5:
        for i in n:
            if int(i)%2!=0:
                mult = mult * int(i)
        break
    else:
        print("Wrong input.Enter 5!-digit number")
print(mult)
