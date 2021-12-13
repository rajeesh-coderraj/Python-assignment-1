#fcatorial of n terms
f1=0
f2=1
n=int(input("Enter the number to find factorial of n series "))
print("The fibonocci series are")
print(f1)
print(f2)
for i in range(0,n):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3)
