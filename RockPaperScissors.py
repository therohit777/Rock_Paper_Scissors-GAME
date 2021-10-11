import random
ask="y"
while(ask=="y" or ask=="y"):
    a=0
    b=0
    l={}
    print("---------------------ROCK_PAPER_SCISSORS GAME---------------------")
    print("RULES OF GAME.")
    print("There will be five rounds out of which who wins the max is considered to be the winner !")
    print("1. ROCK")
    print("2. PAPER")
    print("3. SCISSORS")
    print("If any other number is choosed accept the above mentioned the round is terminated and the Player has to play the same round once again with the valid input!!")
    round=0
    while(round<5):
        c=random.randint(1,3)
        d=int(input("Enter your Material serial No. that is Above: "))
        if(d>3 or d<1):
         print("Your choice is not valid , please try again and the same round is played once again")
         continue
        if(c==1):
            print("Computer choosed ROCK")
            if(d==1):
                print("You choosed ROCK")
                l[round]="DRAW"
                print("This round is a DRAW")
            elif(d==2):
                print("You choosed PAPER")
                l[round]="PLAYER"
                b+=1
                print(" PLAYER won this Round")
            elif(d==3):
                print("You choosed Scissors")
                l[round]="COMPUTER"
                a+=1
                print("COMPUTER won this Round")
          
                   
        elif(c==2):
            print("Computer choosed PAPER")
            if(d==1):
                print("You choosed ROCK")
                l[round]="COMPUTER"
                a+=1
                print("COMPUTER won this Round")
            elif(d==2):
                print("You choosed PAPER")
                l[round]="DRAW"
                print("This round is a DRAW")
            elif(d==3):
                print("You choosed Scissors")
                l[round]="PLAYER"
                b+=1
                print("PLAYER won this Round")
        elif(c==3):
            print("Computer choosed SCISSORS")
            if(d==1):
                print("You choosed ROCK")
                l[round]="PLAYER"
                b+=1
                print("PLAYER won this Round")
            elif(d==2):
                print("You choosed PAPER")
                l[round]="COMPUTER"
                a+=1
                print("COMPUTER won this Round")
            elif(d==3):
                print("You choosed Scissors")
                l[round]="DRAW"
                print("This round is a DRAW")  
        round+=1 
    print("Five rounds completed")
    print("-------------------------RESULTS OF THE MATCH-------------------------")
    print("ROUNDWISE WINNER")
    for i in l:
        print(i+1,l[i])
    print("Player's Score is:",b)    
    print("Computer's Score is:",a)
    if(a>b):
        print("COMPUTER IS THE WINNER.")
    elif(b>a):
        print("PLAYER IS THE WINNER.")
    elif(b==a):
        print("IT IS A DRAW MATCH.")   
    print("\n")
    play=input("Do you wanna Play again (Y/N): ")
    if(play=="y" or play=="Y"):
        ask=play
    else:
        break

