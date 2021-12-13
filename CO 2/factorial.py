# Python program to find the factorial of a number provided by the user.
n=int(input("Enter the number to find factorial:"))

f = 1

# check if the number is negative, positive or zero
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n + 1):
       f= f*i
   print("The factorial of",n,"is",f)