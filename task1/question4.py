#Write a python function to perform selection sort on a given string


def selectionsort(s):               
    l=list(s)
    for i in range(0, len(l)-1):
        minindex=i
        for j in range(i, len(l)):
            if l[j]<l[minindex]:
                minindex=j
        temp=l[i]
        l[i]=l[minindex]
        l[minindex]=temp
    return l



print(selectionsort("hello"))