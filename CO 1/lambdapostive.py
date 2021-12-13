print("Enter the list limit")
lst=[]
n=int(input("Enter the intergers to list:"))
for i in range(0, n):
        element=int(input())
        lst.append(element)
list2=[x for x in lst if x>0]
print(list2)