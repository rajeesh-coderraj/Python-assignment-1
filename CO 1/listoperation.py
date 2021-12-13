list1=[1,2,3,4,5]
list2=[3,4,1,4,6]
print(list1)
print(list2)

print("The List are equal or not in length")
if len(list1)==len(list2):
    print("lists having  same length")
else:
    print("Lists not in same length")


print("check whether list sums to same value ")
s1=sum(list1)
s2=sum(list2)
print("SUm of first list and second",s1,s2)
if s1==s2:
    print("Sum are equal")
else:
    print("sum are not equal")

print("check  whether any value occur in both")
list3=[x for x in list1 if x in list2]
if len(list3)<1:
    print("No value occure in both")
else:
    print("common values:",list3)