"""Given an array arr[], find the first repeating element. The element should occur more than once
   and the index of its first occurrence should be the smallest."""


def repeating(arr):
    arrrep=[]
    minindex=0
    for i in arr:
        if i not in arrrep:
            arrrep.append(i)
        else:
            if arr.index(i)<minindex:
                minindex=arr.index(i)
    return minindex

arr=[2, 5, 1, 2, 3, 5, 1, 4]
print(arr[repeating(arr)])