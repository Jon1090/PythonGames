import random, sys, time

print("Mash the Enter button as fast as you can to get the fastest presses per second")
input('Press Enter to begin...')
HighScore=100
while True:
    print()
    print("Start in 3.")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Go!")
    DrawTime=time.time()
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    print("Halfway!")
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    TimeElapsed=time.time()-DrawTime

    if TimeElapsed<1:
        print("You Cheated!")
    else:
        TimeElapsed=round(TimeElapsed, 4)
        print("You took", TimeElapsed, 4, "seconds to press 20 times.")
        print("You pressed Enter", round(TimeElapsed/20, 4), "times per second")
    if TimeElapsed<HighScore:
        HighScore=TimeElapsed
    print("Your HighScore is", HighScore, "seconds.")
    time.sleep(5)
    print("Enter 'Quit' to stop or press Enter to play again.")
    response=input('> ').upper()
    if response=="QUIT":
        print("Thanks for playing!")
        sys.exit()
