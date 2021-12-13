#Check the vowels in the string
word=input("Enter the word:")
vowels=["A","E","I","O","U","a","e","i","o","u"]
checkvowel=[x for x in word if x in vowels ]
print(checkvowel)