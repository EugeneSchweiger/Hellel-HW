import string

input_text=input("Enter some text to check if it's Pangram")

def is_pangram(txt):
    alphabet = string.ascii_lowercase
    letters_count = 0
    if len(txt)<=25:
        return False
    else:
        txt="".join(list(set(txt)))
        for i in range(len(txt)):
            if len(txt)<25:       
                return False
            if  txt[i] in alphabet:
                letters_count+=1
        if letters_count==26:
            return True
        else: return False
"""
To speed up code working I add 2 length checkings
First check owerall input text length. If it's small-expecting result
Second check only unique symbols. If they are not 26- also expecting result.
However printeble symbols count from keyboard is not so big 
"""


if is_pangram(input_text):
    print("It IS pangram")
else:
    print("It's NOT pangram")