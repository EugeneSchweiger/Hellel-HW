"""
program can calculate unicodes whatever you entered: from a to z and vice wersa
"""
chr1=input("Enter first character end press \"Enter\"")
chr2=input("Enter second character end press \"Enter\"")

def alphabet_unicodes_sum(a,b):
    chars = "abcdefghijklmnopqrstuvwxyz"

    def foo(chars):
        str2 = chars[(chars.find(a)):((chars.find(b)) + 1)]
        alphabet = (list(str2))
        for i in range(len(alphabet)):
            alphabet[i] = ord(alphabet[i])
        sum = 0
        for n in alphabet:
            sum += n
        return sum

    if ord(a) > ord(b):
        chars=chars[::-1]
        return foo(chars)

    else:
        return foo(chars)





# def alphabet2unicode(chrs):
#     alphabet = (list(chrs))
#     for i in range(len(alphabet)):
#         alphabet[i]=ord(alphabet[i])
#     return alphabet



# def sum_of_croped_unicode_alphabet(a,b):
#     new_str2 = alphabet_unicodes_crop_plus_if_reverse(a,b)
#     new_alphabet = alphabet2unicode(new_str2)
#     sum=0
#     for i in new_alphabet:
#         sum+=i
#     return sum

print("Sum of unicodes between \"%s\" and \"%s\" is:"%(chr1,chr2),alphabet_unicodes_sum(chr1,chr2) )


