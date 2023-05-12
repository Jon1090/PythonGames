import time
import random
Scores=["000","000","000","000","000","000","000","000","000","000","000","000","000"]
Dice = ['''
 ---
| O |
 ---  ''','''
 ---
|0  |
|  0|
 --- ''','''
 ___
|0  |
| 0 |
|  0|
 --- ''','''
 ____
|0  0|
|    |
|0  0|
 ----  ''','''
 _____
|0   0|
|  0  |
|0   0|
 ----- ''','''
 _____
|0   0|
|0   0|
|0   0|
 -----''']

print("Welcome to Yahtzee!")
for i in range(6):
    print(Dice[i])
    time.sleep(.1)
time.sleep(2)
print("Let's get started!")
time.sleep(1)
print("\n \n \n \n \n \n ")

def GetDiceRoll():

    
    DicetoKeep=[]

    for i in range(5):
        i=random.randint(0, 5)
        DicetoKeep.append(i+1)
        print(*Dice[i])

    print("Your dice!")
    print(DicetoKeep)
    time.sleep(1)

    print("Type the dice you would like to reroll one at a time and press enter! \nOnce you have selected your dice, type 'finished' or press enter again to reroll or move on! \nYou will have one more chance to reroll.")

    x=True    
    while x==True:
        Keeper=input("Dice: ")
        try:
            if int(Keeper) not in DicetoKeep:
                    print("This isn't a valid die")
            if int(Keeper) in DicetoKeep:
                DicetoKeep.remove(int(Keeper))
        except:
            x=False
       
    

    print("You are keeping:", DicetoKeep)
    time.sleep(.5)
    if len(DicetoKeep)==5:
        return DicetoKeep
    if len(DicetoKeep)<5:
        print("Getting your new dice.")
        for i in range(len(DicetoKeep), 5):
            i=random.randint(0,5)
            DicetoKeep.append(i+1)
            print(*Dice[i])
        print("Your dice after 1 reroll:")
        print(DicetoKeep)

        print("Type the dice you would like to reroll! \nOnce you have selected your dice, type 'finished' or press enter to reroll or move on!")
        
        x=True    
        while x==True:
            Keeper=input("Dice: ")
            try:
                if int(Keeper) not in DicetoKeep:
                    print("This isn't a valid die")
                if int(Keeper) in DicetoKeep:
                    DicetoKeep.remove(int(Keeper))
            except:
                x=False
        print("You are keeping:", DicetoKeep)
        time.sleep(.5)
        if len(DicetoKeep)==5:
            return DicetoKeep
        if len(DicetoKeep)<5:
            print("Getting your new dice.")
            for i in range(len(DicetoKeep), 5):
                i=random.randint(0,5)
                DicetoKeep.append(i+1)
            print(*Dice[i])
            print("Your dice after 2 rerolls:")
            print(DicetoKeep)
    return DicetoKeep

def InsertScore():
    while True:
        print("Where would you like to submit your score? \nType the number of the corresponding category (ie. '1').")
        Slot=input("Number 1-13: ")
        if Slot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:
            print("Please enter a number from 1 to 13")
        else:
            Slot=int(Slot)
            return Slot
        

        

def YahtzeeBoard():
    GameCounter=0
    while GameCounter<13:
        
        DiceforRound=GetDiceRoll()
        DiceforRound=sorted(DiceforRound)
        
        print("""
        1) Aces={}
        2) Twos={}
        3) Threes={}
        4) Fours={}
        5) Fives={}
        6) Sixes={}
        7) 3 of a kind={}
        8) 4 of a kind={}
        9) Full House={}
        10) Small Straight={}
        11) Large Straight={}
        12) Yahtzee={}
        13) Chance={}""".format(Scores[0], Scores[1], Scores[2], Scores[3], Scores[4], Scores[5], Scores[6], Scores[7], Scores[8], Scores[9], Scores[10], Scores[11], Scores[12]))
        Total=sum(int(i) for i in Scores)
        print("Total={}".format(Total))
        print()
    
        print("Your Dice:", DiceforRound)
        Dict={}
        for i in DiceforRound:
            Dict.setdefault(i,0)
            Dict[i]=Dict[i]+1
        time.sleep(1)

        WhichSlot=InsertScore()
        while Scores[WhichSlot-1]!="000":
            print("This slot is already taken!")
            time.sleep(1)
            WhichSlot=InsertScore()
        
        if WhichSlot==1:
            try:
                Scores[0]=Dict[1]
            except:
                Scores[0]=0           
        if WhichSlot==2:
            try:
                Scores[1]=Dict[2]*2
            except:
                Scores[1]=0
        if WhichSlot==3:
            try:
                Scores[2]=Dict[3]*3
            except:
                Scores[2]=0
        if WhichSlot==4:
            try:
                Scores[3]=Dict[4]*4
            except:
                Scores[3]=0
        if WhichSlot==5:
            try:
                Scores[4]=Dict[5]*5
            except:
                Scores[4]=0
        if WhichSlot==6:
            try:
                Scores[5]=Dict[6]*6
            except:
                Scores[5]=0
        if WhichSlot==7:
            if 3 in Dict.values() or 4 in Dict.values() or 5 in Dict.values():
                Scores[6]=sum(DiceforRound)
            else:
                Scores[6]=0
        if WhichSlot==8:
            if 4 in Dict.values() or 5 in Dict.values():
                Scores[7]=sum(DiceforRound)
            else:
                Scores[7]=0
        if WhichSlot==9:
            if 2 in Dict.values() and 3 in Dict.values():
                Scores[8]=sum(DiceforRound)
            else:
                Scores[8]=0
        if WhichSlot==10:
            if 1 and 2 and 3 and 4 in DiceforRound:
                Scores[9]=sum(DiceforRound)
            if 2 and 3 and 4 and 5 in DiceforRound:
                Scores[9]=sum(DiceforRound)
            if 3 and 4 and 5 and 6 in DiceforRound:
                Scores[9]=sum(DiceforRound)
            else:
                Scores[9]=0
        if WhichSlot==11:
            if 1 and 2 and 3 and 4 and 5 in DiceforRound:
                Scores[10]=sum(DiceforRound)
            if 2 and 3 and 4 and 5 and 6 in DiceforRound:
                Scores[10]=sum(DiceforRound)
            else:
                Scores[11]=0
        if WhichSlot==12:
            if 5 in Dict.values():
                Scores[11]=50
            else:
                Scores[11]=0
        if WhichSlot==13:
            Scores[12]=sum(DiceforRound)
        time.sleep(1)   
        print("""
        1) Aces={}
        2) Twos={}
        3) Threes={}
        4) Fours={}
        5) Fives={}
        6) Sixes={}
        7) 3 of a kind={}
        8) 4 of a kind={}
        9) Full House={}
        10) Small Straight={}
        11) Large Straight={}
        12) Yahtzee={}
        13) Chance={}""".format(Scores[0], Scores[1], Scores[2], Scores[3], Scores[4], Scores[5], Scores[6], Scores[7], Scores[8], Scores[9], Scores[10], Scores[11], Scores[12]))
        Total=sum(int(i) for i in Scores)
        print("Total={}".format(Total))
        print()
        time.sleep(2)
        print()
        GameCounter+=1
        if GameCounter<13:
            print("Time to go again!")
            print("Here are your new dice!")
        time.sleep(1)
    print("Game Over!")
    print("Your score was: ", Total,"!")
    print("Would you like to play again? (y/n)")
    Restart=input("y/n:")
    if Restart=="y":
        YahtzeeBoard()
YahtzeeBoard()
