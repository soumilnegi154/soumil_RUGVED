#Write a python program to sort a string alphabetically and print the count of each character



def sortncount(s):
    for i in sorted(set(list(s))):           #traversing a set of sorted and unique elements of list of string
        print(i, ": ", list(s).count(i))     #printing each letter and its count

sortncount(input("Enter string: "))          #taking input string