import random   # for selecting champions
import os       # for the clear function

# Pretty self explanatory, clears the console to make everything cleaner and prints the logo.
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    print(" _                                          __   _                            ")
    print("| |                                        / _| | |                           ")
    print("| |     ___  __ _  __ _ _   _  ___    ___ | |_  | |     __ _ _ __   ___  ___  ")
    print("| |    / _ \/ _` |/ _` | | | |/ _ \  / _ \|  _| | |    / _` | '_ \ / _ \/ __| ")
    print("| |___|  __/ (_| | (_| | |_| |  __/ | (_) | |   | |___| (_| | | | |  __/\__ \ ")
    print("\_____/\___|\__,_|\__, |\__,_|\___|  \___/|_|   \_____/\__,_|_| |_|\___||___/ ")
    print("                   __/ |                                                      ")
    print("                  |___/                                                       ")

champions = {   'Darius':'top',
                'Draven':'bot',
                'Ahri':'mid',
                'Dr. Mundo':'top',
                'Elise':'jungle',
                'Corki':'mid',
                'Evelynn':'jungle',
                'Thresh':'support',
                'Ivern':'jungle',
                'Yorick':'top',
                'Zed':'mid',
                'Yasuo':'mid',
                'Ezreal':'bot',
                'Skarner':'jungle',} 

loop = 10
score = 0

cls()

# Game Menu
menu = input("Welcome to the League of Lanes.\nLet's see if you can remember where all these champions go.\n  Type S to start.\n  Type E to exit.\n").lower()

# GAME LOOP
if menu == 's':
    while loop > 0:
        cls()
        d = random.choice(list(champions))
        response = input("What role is " + d + " played in \nValid Answers are : Top, Jungle, Mid, Bot and Support\n").lower()
        
        if response == champions[d] :
            input("Correct! Press Enter to continue.\n")
            score += 1
        else:
            input("Incorrect, the answer is " + champions[d] + ". Press Enter to continue")
        
        del champions[d]
        loop -= 1
    if loop == 0:
        cls()
        input("You got " + str(score) + " out of 10 correct!\nThank you for playing. Press Enter to exit")
        exit()

# Quit
if menu == 'e':
    exit()