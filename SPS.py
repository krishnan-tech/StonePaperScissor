import random

# This Stone-Paper-Scissor Game is made by Krishnan Navadia!

print("==========================")
print("Stone Paper Scissor GAME!!")
print("==========================")

total_chance = 5
your_chance = 0
human_value = 0
comp_value = 0
c = ["s","p","c"]
my_point = 0
comp_point = 0
while your_chance < total_chance:
    your_chance = your_chance + 1
    guess = input(("Select Stone(s), Paper(p), Scissor(c)")).lower()
    random_comp = random.choice(c)
    try:
        if guess == "s" and guess == random_comp:
            print("Draw this round!")
            print(f"Computer Selected {random_comp}")

        elif guess == "s" and random_comp == "c":
            my_point = my_point + 1
            print("====================================================================")
            print("|                              You Got 1 POINT!                    |")
            print("=====================================================================")
            print(f"|   Your point is now {my_point}      |      Computer Point is {comp_point}            |")
            print(f"|                    Computer Selected {random_comp}                           |")
            print("=====================================================================")

        elif guess == "s" and random_comp == "p":
            comp_point = comp_point + 1
            print("====================================================================")
            print("|                              Computer Got 1 POINT!               |")
            print("=====================================================================")
            print(f"|   Your point is now {my_point}      |      Computer Point is {comp_point}            |")
            print(f"|                    Computer Selected {random_comp}                           |")
            print("=====================================================================")

#======================================================================================================================================================
#---------------------------------------------------------- IF I GUESS PAPER --------------------------------------------------------------------------
#======================================================================================================================================================

        if guess == "p" and guess == random_comp:
            print("Draw this round!")
            print(f"Computer Selected {random_comp}")

        elif guess == "p" and random_comp == "s":
            my_point = my_point + 1
            my_point = my_point + 1
            print("====================================================================")
            print("|                              You Got 1 POINT!                     |")
            print("=====================================================================")
            print(f"|   Your point is now {my_point}      |      Computer Point is {comp_point}            |")
            print(f"|                    Computer Selected {random_comp}                           |")
            print("=====================================================================")

        elif guess == "p" and random_comp == "c":
            comp_point = comp_point + 1
            print("====================================================================")
            print("|                              Computer Got 1 POINT!               |")
            print("=====================================================================")
            print(f"|   Your point is now {my_point}      |      Computer Point is {comp_point}            |")
            print(f"|                    Computer Selected {random_comp}                           |")
            print("=====================================================================")

#======================================================================================================================================================
#---------------------------------------------------------- IF I GUESS SCISSOR --------------------------------------------------------------------------
#======================================================================================================================================================

        if guess == "c" and guess == random_comp:
            print("Draw this round!")
            print(f"Computer Selected {random_comp}")

        elif guess == "c" and random_comp == "p":
            my_point = my_point + 1
            print("====================================================================")
            print("|                              You Got 1 POINT!                     |")
            print("=====================================================================")
            print(f"|   Your point is now {my_point}      |      Computer Point is {comp_point}            |")
            print(f"|                    Computer Selected {random_comp}                           |")
            print("=====================================================================")

        elif guess == "c" and random_comp == "s":
            comp_point = comp_point + 1
            print("====================================================================")
            print("|                              Computer Got 1 POINT!               |")
            print("=====================================================================")
            print(f"|   Your point is now {my_point}      |      Computer Point is {comp_point}            |")
            print(f"|                    Computer Selected {random_comp}                           |")
            print("=====================================================================")


    except Exception as e:
        print(e)

    print(f"                      now your lives are {total_chance - your_chance}")
