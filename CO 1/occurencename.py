# Store a list of first names.Count the occurrences of ‘a’ within the list
lettercount=0
lettercounts=0
names=["Awshin","Adwaidth","Arya","arun"]
for x in names:
  lettercount=lettercount+x.count("a" and "A")
  lettercounts=lettercounts+x.count("A")
totalcount=lettercount+lettercounts
print("The Occurence of  of 'a' and 'A'=",totalcount)