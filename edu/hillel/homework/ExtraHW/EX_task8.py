import string

input_text=input("Enter some text to check if it's Pangram")

def is_pangram(txt):
    alphabet = string.ascii_lowercase
    letters_count = 0
    if len(txt)<=25:
        return False
    else:
        txt="".join(list(set(txt.lower())))
        for i in range(len(txt)):
            if len(txt)<25:
                return False
            if  txt[i] in alphabet:
                letters_count+=1
        if letters_count==26:
            return True
        else: return False

import timeit
def test():
    return is_pangram(input_text)

print("overall time",timeit.timeit("test()", setup="from __main__ import test", number=1),"seconds")

if is_pangram(input_text):
    print("It IS pangram")
else:
    print("It's NOT pangram")

