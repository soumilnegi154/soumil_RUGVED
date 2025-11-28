#Write a python function to encrypt a string using Ceasar’s Cipher


def cipher(message, shift):
    mnew=""
    for i in message:
        if (ord(i.upper())+shift)>90:
            i=chr((ord(i)+shift)-26)
        elif (ord(i.upper())+shift)<65:
            i=chr((ord(i)+shift)+26)
        else:
            i=chr(ord(i)+shift)
        mnew+=i
    return mnew

print(cipher("xyz", 3))