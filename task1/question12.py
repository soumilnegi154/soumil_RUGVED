#WAP a code to print the following patters.



def diamond(rows):
    for i in range(1, rows+1):
        for j in range(rows-i, 0, -1):
            print(" ", end="")
        for k in range(1, i+1):
            print("* ", end="")
        print()
    for i in range(rows, 0, -1):
        for j in range(0, rows-i):
            print(" ", end="")
        for k in range(i+1, 1, -1):
            print("* ", end="")
        print()

def butterfly(n):
    n2=n
    for i in range(1, n+1):
        for j in range(0, i):
            if j!=(n-1):
                print("*", end="")
        for k in range(0, 1+2*(n-i-1)):
            print(" ", end="")
        for j in range(0, i):
            print("*", end="")
        print()
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            print("*", end="")
        for k in range(1+2*(n-i-1), 0, -1):
            print(" ", end="")
        for j in range(0, i):
            print("*", end="")
        print()

diamond(4)
butterfly(4)