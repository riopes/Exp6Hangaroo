secretWord = str(input("Enter Secret Word: "))
lettersGuessed = input("Guess a Letter: ")

def isWordGuessed (secretWord, lettersGuessed):
        for a in secretWord:
            x = a in lettersGuessed
            if x == ("False"):
                break
            return x
print (isWordGuessed(secretWord, lettersGuessed))