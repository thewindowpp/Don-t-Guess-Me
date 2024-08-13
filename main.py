from time import sleep
from os import system
from random import randint


#Game start
def start():
    #ASCII art
    print("""
  _____              _ _      _____                       __  __      _ 
 |  __ \            ( ) |    / ____|                     |  \/  |    | |
 | |  | | ___  _ __ |/| |_  | |  __ _   _  ___  ___ ___  | \  / | ___| |
 | |  | |/ _ \| '_ \  | __| | | |_ | | | |/ _ \/ __/ __| | |\/| |/ _ \ |
 | |__| | (_) | | | | | |_  | |__| | |_| |  __/\__ \__ \ | |  | |  __/_|
 |_____/ \___/|_| |_|  \__|  \_____|\__,_|\___||___/___/ |_|  |_|\___(_)
                                                                                                                                          
""")
    
    #Start/quit game, in future leaderboard
    print("Welcome to Don't Guess Me!")
    sleep(1)

    quitcheck = input("Please type 'quit' if you would like to exit, respond with anything else to continue: ")

    if quitcheck.lower() == "quit":
        exit()

    #Ask for rules
    global needrule
    rulecheck = input("Would you like to see the rules? (y/n): ")
    if rulecheck.lower() == "y":
        needrule = "true"
    elif rulecheck.lower() == "n":
        needrule = "false"
    else:
        print("Please restart the program and enter a valid response (y/n)")
        exit()


#Game Rules
def game_rule(): 
  if needrule == "true":
      print("\nWelcome to the rules!")
      sleep(2)
      print("\nEach round there will be three options, I will pick one of them.")
      sleep(2)
      input("Press Enter/Return to continue")
      print("\nIf you select the same option as me, you are eliminated")
      sleep(2)
      input("That's all the rules, press Enter/Return to continue")
      sleep(2)
      
  elif needrule == "false":
      print("Good luck with the game!")
  else:
      print("Error has occured, please contact the owner")

#Level
def lvl_1():
    #Objects

    obj = ["hack", "club", "ship"]

  
    print("Welcome to the first level, there will be three rounds")
    sleep(2)
    input (f"The three options for this round are: '{obj[0]}', '{obj[1]}', and '{obj[2]}'. Please press Enter/Return to continue.")

    #Round repeater

    lvl_round = 1

    for lvl_round in range(3):
        round_ans = input(f"Object selection for round {lvl_round}: ")
        if round_ans.lower() == obj[randint(0,2)]:
          print("You selected the same as me. Game over :(")
          exit()
        #Make check that is valid
        lvl_round += 1








system("clear")

start()
game_rule()
lvl_1()