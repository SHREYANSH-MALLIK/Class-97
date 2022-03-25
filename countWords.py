introString = input("Enter your introduction : ")

#print (introString)

characterCount = 0

wordCount = 1

for i in introString :
    characterCount = characterCount+1
    print (characterCount)

    if (i == " "):
        wordCount = wordCount+1

print ("Number of words in the string = ", wordCount)
print (wordCount)
print ("Number of character in the string = ", characterCount)
print (characterCount) 

