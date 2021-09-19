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
    round=0
    while(round<5):
        c=random.randint(1,3)
        d=int(input("Enter your Material serial No. that is Above: "))
        if(c==1):
            if(d==1):
                l[round]="DRAW"
                print("This round is a DRAW")
            elif(d==2):
                l[round]="PLAYER"
                b+=1
                print("PLAYER won this Round")
            elif(d==3):
                l[round]="COMPUTER"
                a+=1
                print("COMPUTER won this Round")
        elif(c==2):
            if(d==1):
                l[round]="COMPUTER"
                a+=1
                print("COMPUTER won this Round")
            elif(d==2):
                l[round]="DRAW"
                print("This round is a DRAW")
            elif(d==3):
                l[round]="PLAYER"
                b+=1
                print("PLAYER won this Round")
        elif(c==3):
            if(d==1):
                l[round]="PLAYER"
                b+=1
                print("PLAYER won this Round")
            elif(d==2):
                l[round]="COMPUTER"
                a+=1
                print("COMPUTER won this Round")
            elif(d==3):
                l[round]="DRAW"
                print("This round is a DRAW")  
        round+=1 
    print(round)
    print("-------------------------RESULTS OF THE MATCH-------------------------")
    print("ROUNDWISE WINNER")
    for i in l:
        print(i+1,l[i])
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

