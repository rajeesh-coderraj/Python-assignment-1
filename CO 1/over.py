print("Enter the list limit")
lst=[]
n=int(input("Enter the intergers to list:"))
for i in range(0, n):
        element=int(input())
        lst.append(element)
a=len(lst)
for i in lst:
    if lst[i] > 100:
        print("Over")
    else:
        print(i)
