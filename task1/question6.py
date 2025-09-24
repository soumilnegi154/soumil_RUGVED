#Create a function that checks whether given string is an anagram or not?


def anagram(s1, s2):
    if sorted(list(s1))==sorted(list(s2)):
        return True
    else:
        return False
    
print(anagram("rescue", "secure"))