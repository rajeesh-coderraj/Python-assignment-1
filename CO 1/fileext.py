#Show the extension of file
print("Enter the file name with extension")
file=str(input())
filename=file.split(".")
#print(filename)
print("File name:",filename[0])
print("File extension:",filename[1])