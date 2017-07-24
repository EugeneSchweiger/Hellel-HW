
chr1=ord(input("Enter first character end press \"Enter\""))
chr2=ord(input("Enter second character end press \"Enter\""))

def sum(a,b):
    sum=0
    for v in range(a,b+1):
        sum += v
    print(sum)
if chr1 > chr2:
    sum(chr2,chr1)
else:
    sum(chr1,chr2)


# def sum(a, b):
#     if chr1 > chr2:
#         sum = 0
#         for i in range(b, (a + 1)):
#             sum += i
#         return sum
#     else:
#         sum = 0
#         for i in range(a, (b + 1)):
#             sum += i
#         return sum


