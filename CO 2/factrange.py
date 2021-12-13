
fact=1

print("Enter the limit")
ran=int(input())
for k in range(1,ran):
    for i in range(1,k):

        fact=fact*i
        print("The factorial is ",fact)

