# Write a python function to check if a given credit card number is valid or not using Luhn’s Algorithm

"""Starting from the rightmost digit, double the value of every second digit.
   f doubling of a number results in a two digit number i.e greater than 9, then add the digits of the product to get a
   single digit number. Now take the sum of all the digits.If the total modulo 10 is equal to 0  then the number is 
   valid according to the Luhn formula; else it is not valid."""


def check(num):
    l, sum =[], 0
    for i in str(num)[::-1]:
        l.append(eval(i))
    if len(l)!=16:
        print("Not a valid card")
        return False
    for i in l:
        if l.index(i)%2!=0:
            j=i*2
            if j>=10:
                while(j>0):
                    digit=j%10
                    i+=digit
                    j=j//10
            sum+=i
        else:
            sum+=i
    if sum%10==0:
        print("Card is valid")
        return True
    else:
        print("Card is invalid")
        return False
    

check(4444333322221111)
            


