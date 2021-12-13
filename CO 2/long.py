#Accept a list of words and return length of longest word
list1=[]
check=[]
for x in range(0,4):
    word=input("Enter the word:")
    check.append(len(word))
    list1.append(word)
print(list1)
print("length of longest word:",max(check))