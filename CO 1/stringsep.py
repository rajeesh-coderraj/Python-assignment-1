#create a single string separated with space in two string by swapping the character at the postion 1
string=str(input("Enter the string"))
print(string)
stringnew=string.split(" ")
a=list(stringnew[0])
b=list(stringnew[1])
rp1=a[0]
rp2=b[0]
print(a,b)
print("After swapping")
replace=[sub.replace(rp1, rp2) for sub in a]
print(replace)
replace1=[sub.replace(rp2, rp1) for sub in b]
print(replace1)