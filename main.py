word=input("Enter a word:")
letter=input("Enter a letter:")

i=0
count=0

while i<len (word):
    if word[i]==letter:
       count=count+1
    i=i+1

print("Total number of",letter,"is",count)