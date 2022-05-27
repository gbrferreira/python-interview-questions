#Palindrome checker
print("Hi! Welcome to the Palindrome Checker!")
#We transform the string into a list and remove all blank spaces with .split and .join functions so we can compare the string backwards.
phrase= str(input("Type a string! \n")).strip().upper()
words= phrase.split()
together= "".join(words)
inverse= ""
#Loop that runs the list backwards and stores its index number in the Letter variable.
for letter in range(len(together) -1, -1, -1):
    inverse+= together[letter]
    #We'll use the Inverse variable to compare the stored string in the Together variable with itself, but using Letter as a index to run the string backwards.
if inverse == together:
    print("We have a palindrome!")
else:
    print("The inputted string is not a palindrome.")



