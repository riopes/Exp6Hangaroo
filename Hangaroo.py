import random
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
wordList = ['ruano','espana','dapitan','angkong','thomasian','benavides', 'medicine', 'carpark','paskuhan','varsitarian','engineering','tigers','pontifical']
secretWord = random.choice(wordList); length_word = len(secretWord); lettersGuessed =[]; guessWord =[]

def start():
    print ("Welcome to Hangaroo! Guess the word and win!")
    print ("CATEGORY: University of Santo Tomas")
start()

def secret():
    for character in secretWord:
        guessWord.append("_")
        
    print ("The word you have to guess is made up of ", length_word, "characters")
    print (' '.join(guessWord))
    print ("You have four tries!")
        
def guessing():
    turns = 0
    while turns < 4:
        print ("\n", ' '.join(alphabet))
        guess = input("Letter: \n").lower()
        
        if guess not in alphabet:
            print ("Not a Letter. Try Again.")
            turns +=1
            print("Mistakes Made: ", turns)
        elif guess in lettersGuessed:
            print("Already Used Letter, Please Try Again.")
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print ("Well Played")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guessWord[x] = guess
                        print(' '.join(guessWord))
                alphabet.remove(guess)
            else:
                print("Wrong guess. Please Try Again.")
                alphabet.remove(guess)
                turns += 1
                print("Mistakes Made: ", turns)
                if turns == 4:
                    print("You killed the kangaroo!.")
                    print("You lost! The secret word was:", secretWord)
                    print("GAMEOVER! PLAY AGAIN !")
                    break
        if '_' not in guessWord:
                        print("YOU WON! CONGRATULATIONS!")
                        break              
secret()
guessing()