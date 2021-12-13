#Biggest of 3 number
print("Enter the 3 numbers")
a=int(input("First Number"))
b=int(input("Second Number"))
c=int(input("Third Number5"))

if a > b and a > c:
    big=a
elif b > a and b > c:
    big=b
else:
    big=c
print("The biggest number :",big)

