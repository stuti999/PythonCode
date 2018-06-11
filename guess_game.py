import random
while input("\n\n press any key to continue:"):
    comGuess=random.randint(1,50)
    c=1
    for c in range(1,7):
        if c==6:
            print("\ncomputer guess was",comguess)

        userGuess=int(input("enter a number(1-50)"))
        if userGuess>=1 and comGuess<=50:
            if userGuess > comGuess:
                print("think lower")
            elif userGuess < comGuess:
                print("think big")
            elif userGuess==comGuess:
                print(" correct chosses")
                break
        else:
            print("worng chosses")
            print("chosses from 1 to 50")
    n =input(" do you want to play again . y or n:").strip()
    n = ch.lower()
    if n=='y' or n== "yes":
        continue
    else:
        break



    
    

