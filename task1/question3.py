#Write a python program to check if given number is a hill number


"""hill number:
   A hill number is a number that has the same digit in the first & the last, but that's not all.
   In a hill number the first digits are strictly increasing until the largest digit,
   and after the largest digit, the last digits are strictly decreasing.
   The largest digit can be repeated but consecutively only, meaning no gaps by smaller numbers."""


def hillnumber(num):
    num=str(num)
    if (num[-1] == num[0]):
        for i in num:
            if(eval(i)>eval(i)-1):
                maxnum=eval(i)
                if
            else:
                return False





