# snakewatergun

# snake drinks water
# gun shrinks in water
# gun kills snake

import random
print("Game begins!!")
print("Maximum number of chances to play the game 10")
i = 1
while i <= 10:
    print("make a selection: snake, water, gun")
    me_selection = input()
    choice_computer = ["snake", "water", "gun"]
    selection_comp = random.choice(choice_computer)
    print(f"computer chooses : {selection_comp}")
    i = i+1
    if me_selection == selection_comp:
        print("Both of u made same choices !! \n game draw")
    else:
        if selection_comp == "snake":
            if me_selection == "water":
                print("computer won")
            elif me_selection == "gun":
                print("You won the game")
        elif selection_comp == "water":
            if me_selection == "snake":
                print("You are winner")
            elif me_selection == "gun":
                print("computer won")
        elif selection_comp == "gun":
            if me_selection == "snake":
                print("computer won the game")
            elif me_selection == "water":
                print("Yoo u won the game")
