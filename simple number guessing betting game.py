
import random
import time
import sys

print("Welcome to simple number betting game.\nI will choose a number from 1 to 100 and you will be able to pick 5 numbers. \nIf you guess my number you will win 50 times your bet. \nIf you don't, you will forfeit your bet! \nGood luck!")
print()
def GetRandomNumber():
    RandomNumber=random.randint(1,100)
    return RandomNumber

def GetPlayerNumber(AlreadyGuessed):
    while True:
        while len(AlreadyGuessed)<5:
            print("Guess a number, 1 to 100")
            PlayerNumber=int(input())
            if type(PlayerNumber)!=int:
                print("Please type a number!")
            if PlayerNumber<1 or PlayerNumber>100:
                print("Guess must be between 1 and 100")
            if PlayerNumber in AlreadyGuessed:
                print("You already guessed this number!")
            else:
                AlreadyGuessed.append(PlayerNumber)
        return AlreadyGuessed

def Bet(Money):
    while True:
        print("Please Enter a bet")
        Bet=int(input())
        if Bet>PlayerMoney:
            print("You don't have that much money.")
            continue
        if Bet<0:
            print("You can't bet negative money.")
        else:
            return Bet

def PlayAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

PlayerMoney=1000
AlreadyGuessed=[]

GameIsDone=False

while True:
    print("You have", PlayerMoney, "dollars.")
    print()
    PlayerGuess=GetPlayerNumber(AlreadyGuessed)

    SecretNumber=GetRandomNumber()

    PlayerBet=Bet(PlayerMoney)
    print("And the winning number is...")
    time.sleep(1)
    print(SecretNumber, "!")
    print()
    
    if SecretNumber in AlreadyGuessed:
        print("Congratulations! You guessed it correctly!")
        print("You won", PlayerBet*50, "monies!")
        PlayerMoney=PlayerMoney + PlayerBet*50
        print("You have", PlayerMoney, "dollars.")
        GameIsDone=True
    else:
        print("You lost and lost", PlayerBet, "dollars!")
        PlayerMoney=PlayerMoney-PlayerBet
        print("You have", PlayerMoney, "dollars.")
        if PlayerMoney==0:
            print("You are broke! You have been kicked out of the casino!")
            sys.exit()
        GameIsDone=True

    if GameIsDone:
        if PlayAgain():
              AlreadyGuessed=[]
              GameIsDone=False
        else:
              break
              
