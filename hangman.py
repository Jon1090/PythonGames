import random
Art = ['''
+---+
    |
    |
    |
   ===''','''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

WordList="""ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra""".split()
def GetRandomWord(Words):
    x=random.randint(0, len(WordList)-1)
    return WordList[x]

def DisplayBoard(MissedLetters, CorrectLetters, SecretWord):
    print(Art[len(MissedLetters)])
    print()

    print("Missed Letters:", end=" ")
    for letter in MissedLetters:
        print(letter, end=" ")
    print()

    Blanks="_" *len(SecretWord)

    for i in range(len(SecretWord)):
        if SecretWord[i] in CorrectLetters:
            Blanks=Blanks[:i]+SecretWord[i]+Blanks[i+1:]
    for letter in Blanks:
        print(letter, end=" ")
    print()

def GetGuess(AlreadyGuessed):
    while True:
        print("Guess a letter.")
        Guess=input()
        Guess=Guess.lower()
        if len(Guess)!=1:
            print("Please enter a single letter.")
        elif Guess in AlreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif Guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER!")
        else:
            return Guess

def PlayAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

print("HANGMAN!")
MissedLetters=""
CorrectLetters=""
SecretWord=GetRandomWord(WordList)
GameIsDone=False

while True:
    DisplayBoard(MissedLetters, CorrectLetters, SecretWord)

    Guess=GetGuess(MissedLetters + CorrectLetters)

    if Guess in SecretWord:
        CorrectLetters=CorrectLetters + Guess

        FoundAllLetters = True
        for i in range(len(SecretWord)):
            if SecretWord[i] not in CorrectLetters:
                FoundAllLetters = False
                break
        if FoundAllLetters:
            print("Yes! The secret word is ", SecretWord, "! You have won!")
            GameIsDone=True
    else:
        MissedLetters= MissedLetters + Guess

        if len(MissedLetters)== len(Art)-1:
            DisplayBoard(MissedLetters, CorrectLetters, SecretWord)
            print("You have run out of guesses after ", str(len(MissedLetters)), "missed guesses!")
            print("The secret word was:", SecretWord)
            GameIsDone=True
    if GameIsDone:
        if PlayAgain():
            MissedLetters=""
            CorrectLetters=""
            GameIsDone=False
            SecretWord=GetRandomWord(WordList)
        else:
            break
    
       
