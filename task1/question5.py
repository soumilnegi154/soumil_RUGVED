#Find the fabonacci of a given number using recursion.

def rfib(n):
    if (n==1):
        return 0
    elif (n==2):
        return 1
    return rfib(n-1)+rfib(n-2)

terms=5
for i in range(1, terms+1):
    print(rfib(i), end=" ")