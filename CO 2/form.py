#Display the given pyramid with step number accepted from user.
#Eg: N=4
#1
#2 4
#3 6 9
#4 8 12 16
n=int(input("enter the row number"))
for x in range(1, n+1):
    for y in range(1, x+1):
        print(x*y, " ", end="")
    print()