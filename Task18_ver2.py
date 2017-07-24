
chr1=ord(input("Enter first character end press \"Enter\""))
chr2=ord(input("Enter second character end press \"Enter\""))

def sum(a, b):
    if chr1 > chr2:
        sum = 0
        for i in range(b, (a + 1)):
            sum += i
        return sum
    else:
        sum = 0
        for i in range(a, (b + 1)):
            sum += i
        return sum
print(sum(chr1,chr2))

