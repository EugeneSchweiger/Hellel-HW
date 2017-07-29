def str2list(str):
    list = []
    for i in range(len(str)):
        list.append(str[i])
    return list

def encrypt_wiz_shift(str,shift = 5):
    str=list(str)
    crypo_tab = [" ", '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '/', '0', '1', '2', '3', '4', '5',
                 '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-','[', '\\', ']',
                 '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '—']
    crypted_text = ''
    for i in range(len(str)):
        char_id = crypo_tab.index(str[i])
        str[i] = crypo_tab[(char_id + shift) % len(crypo_tab)]
        crypted_text += str[i]
    return crypted_text

str = input("Ender some text for crytping")
print(encrypt_wiz_shift(str))

