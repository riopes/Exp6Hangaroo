ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lettersGuessed = list(input("Please list the set of letters: "))

def getAvailableLetters(lettersGuessed):
    AL = []
    for x in ABC:
        AL = ["" if x in lettersGuessed else x for x in ABC]
    print (''.join(AL))
    return x
getAvailableLetters(lettersGuessed)