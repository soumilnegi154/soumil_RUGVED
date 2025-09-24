#Write a program to print the Fibonacci Sequence till n-values where n is user input


def fibonacci(n):
    c1=0
    c2=1
    if (n<=1):
        print(1)
    elif (n==2):
        print(1,1)
    else:
        for i in range(n):
            print(c1)
            temp=c1+c2
            c1=c2
            c2=temp

fibonacci(10)