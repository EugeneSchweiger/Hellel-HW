chr1=input("Enter first character end press \"Enter\"")
chr2=input("Enter second character end press \"Enter\"")


def alphabet_unicodes_sum(a,b):
    chars = [0]*114112#maximum length of unicodes table
    for i in range(len(chars)):
        chars[i]=i

    def sum(chars):
        sum = 0
        for n in alphabet:
            sum += n
        return sum

    if ord(a) > ord(b):
        chars.reverse()
        alphabet = chars[chars.index(ord(a)):(chars.index(ord(b)) + 1)]
        return sum(alphabet)

    else:
        alphabet = chars[ord(a):(ord(b) + 1)]
        return sum(alphabet)

print("Sum of unicodes between \"%s\" and \"%s\" is:"%(chr1,chr2),alphabet_unicodes_sum(chr1,chr2) )


