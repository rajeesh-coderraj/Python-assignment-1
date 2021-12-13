#Write lambda functions to find area of square, rectangle and triangle


rec=lambda l,b:l*b
tri=lambda b,h:(b*h)/2
square=lambda side:side*side
side=int(input("enter the side of square:"))
l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
br=int(input("enter the breadth of triangle:"))
h=int(input("enter the height of triangle:"))


print("area of rectangle=",rec(l,b))
print("area of square=",square(side))
print("area of triangle:",tri(br,h))