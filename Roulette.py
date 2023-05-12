RouletteWheel=[0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
#odd index is red. Even is black. 0 is green
#Find number and determine odd/even, color, or 0
#Determine how player wants to bet
#check if player won
#update player purse

import random
import sys
import time

def GetWinningNumber():
    NumberIndex=random.randint(0, len(RouletteWheel)-1)
    WinningList=[]
    WinningOddOrEven=""
    WinningColor=""
    WinningNumber=RouletteWheel[NumberIndex]
    WinningList.append(WinningNumber)

    if NumberIndex==0:
        WinningColor="g"
        WinningList.append("g")
        WinningList.append(0)
        return WinningList

    if NumberIndex%2==0:
        WinningColor="b"
        WinningList.append(WinningColor)

    if NumberIndex%2!=0:
        WinningColor="r"
        WinningList.append(WinningColor)

    if WinningNumber%2==0:
        WinningOddOrEven="e"
        WinningList.append(WinningOddOrEven)

    if WinningNumber%2!=0:
        WinningOddOrEven="o"
        WinningList.append(WinningOddOrEven)

    return WinningList
                

def GetPlayerBet():
    while True:
        print()
        print("Would you like to select a number, odd/even, or color? (n/oe/c)")
        Answer=input()

        if Answer.lower()=="n":
            while True:
                print("Please select your number. (0 to 35)")
                Answer=int(input())
                if type(Answer)==int:
                    if 0<=int(Answer)<=36:
                        return Answer
                
            
        if Answer.lower()=="oe":
            while True:
                print("Would you like to bet Odd (o) or Even (e)?")
                Answer=input()
                if Answer=="e":
                    return Answer
                if Answer=="o":
                    return Answer

            
        if  Answer.lower()=="c":
             while True:
                print("Would you like to bet Red (r), Black (b), or Green (g)?")
                Answer=input()
                if Answer=="r":
                    return Answer
                if Answer=="b":
                    return Answer
                if Answer=="g":
                    return Answer
            

def GetBetAmount(MaxBet):
    while True:
        print("You have", MaxBet, "dollars. How much would you like to bet?")
        Bet=int(input())
        if type(Bet)==int:
            if 0<=Bet<=MaxBet:
                return Bet

def Main():
    key={"g": "green", "r": "red", "b": "black", "o": "odd", "e": "even"}

    print("Welcome to roulette! \nYou will select your bet and the amount you would like to bet and see if you win! \nPayouts are as follows:")
    print()
    print("Single Number: 35:1 \nOdd or Even: 1:1 \nBlack or Red: 1:1 \nGreen: 35:1")

    PlayerMoney=5000

    print()
    print("You have", PlayerMoney, "dollars!")
    print()
    print("Get gambling!")
    print()
    print("Quit at any time by pressing ctrl+c")
    while True:
        
        PlayerBet=GetPlayerBet()
        RandomWinner=GetWinningNumber()
        PlayerBetAmount=GetBetAmount(PlayerMoney)

        if PlayerBet in key.keys():
            print("You bet", PlayerBetAmount, "dollars on", key[PlayerBet],"!")
        else:
            print("You bet", PlayerBetAmount, "dollars on", PlayerBet,"!")
        time.sleep(1)
        print()
        time.sleep(1)
        print("Time to spin the roulette wheel!")
        print("Press Enter to give it a whirl! Good luck!")
        input()
        print("and now the winning number is!")
        time.sleep(.2)
        print(".")
        time.sleep(.2)
        print(".")
        time.sleep(.2)
        print(".")

        print(RandomWinner[0])
        time.sleep(.5)
        for i in RandomWinner:
            try:
                print("This number is:", key[i])
                time.sleep(.5)
            except:
                continue
        
        time.sleep(1)
        
        if PlayerBet not in RandomWinner:
            PlayerMoney=PlayerMoney - PlayerBetAmount
            print()
            print("Sorry, you lost! You now have", PlayerMoney, "dollars left!")
            
        if PlayerBet in RandomWinner:
            print()
            print("Congratulations, you won!")
            if PlayerBet=="e" or PlayerBet=="o" or PlayerBet=="r" or PlayerBet=="b":
                PlayerMoney=PlayerMoney + PlayerBetAmount
            if PlayerBet=="g":
                PlayerMoney=PlayerMoney + 35*PlayerBetAmount
            if PlayerBet is int():
                PlayerMoney=PlayerMoney + 35*PlayerBetAmount
            print("You now have", PlayerMoney, "dollars!")

        if PlayerMoney <= 0:
            print("Sorry, you are broke! Good thing this isn't real life!")
            sys.exit()

        if PlayerMoney>5000:
            print("You have won a total of", PlayerMoney-5000, "dollars!")

        if PlayerMoney<5000:
            print("You have lost a total of", 5000-PlayerMoney, "dollars!")
        
Main()
