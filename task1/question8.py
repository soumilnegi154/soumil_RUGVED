"""Write a python program to divide a given string into equal parts containing n(user input)
   characters of same sequence. Example: string=“abcdabcdabcdabcd” n=4 output: “abcd”, “abcd”,
   “abcd”, “abcd” If the division is not possible or the sequence cannot be same, print out the
   appropriate error."""



def func(s, n):
    flag=True
    if len(s)%n!=0:
        print(f"Not able to divide in {n} equal parts")
        return False
    for i in range(0, len(s)-n, n):
        if s[i:i+n]!=s[i+n:i+(2*n)]:
            flag=False
    if flag:
        for i in range(0, len(s), n):
            print(s[i:i+n], end=" ")
    else:
        print("sequence cannot be same")
            
            
func("abcdabcdabcdabcd", 4)