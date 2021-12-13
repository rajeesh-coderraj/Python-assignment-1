#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’
string=input("enter a string:")
if string[-3:]=="ing":
    print(string+"ly")
else:
    print(string+"ing")
