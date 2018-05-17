#Jamie Harris
#CSC 109.103
#April 28, 2018
#

import random
import time


def welcome():


    print(" __        __   _                            _        ")
    print(" \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___  ")
    print("  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ ")
    print("   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |")
    print("    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ ")
                                                          

            
            
    print("    [....                             [.....                           [..                                                  [..         ")
    print(" [..    [..                          [..   [..  [.                    [..                                                  [..          ")
    print("[..        [..[.. [..     [..         [..    [..      [..              [..   [..       [..    [. [..     [..    [. [...     [..[..   [..")
    print("[..        [.. [..  [.. [.   [..      [..    [..[.. [.   [..           [.. [.   [..  [..  [.. [.  [..  [..  [..  [..    [.. [.. [.. [.. ")
    print("[..        [.. [..  [..[..... [..     [..    [..[..[..... [..          [..[..... [..[..    [..[.   [..[..   [..  [..   [.   [..   [...  ")  
    print("  [..     [..  [..  [..[.             [..   [.. [..[.             [.   [..[.         [..  [.. [.. [.. [..   [..  [..   [.   [..    [..  ")
    print("    [....     [...  [..  [....        [.....    [..  [....         [....    [....      [..    [..       [.. [...[...    [.. [..   [..   ") 
    print("                                                                                              [..                               [..     ") 
    print()
    print()
    print("Here is how the game works.\n")
    time.sleep(1)
    print("You are player 1. You will be rolling first.\n")
    time.sleep(1)
    print("                                                  ___                                                       ")
    print("At the begining of your turn you will roll a die | ● | it's face value will then be added to your turn score.")  
    print("                                                 |_●_|                                                      ")
    print("                                                                                                            ") 
    time.sleep(1)
    print("During your turn\n")
    print("You will have the option to roll as many times as you wish in order to increase your turn score")
    time.sleep(1)
    print("or you may end you turn at any time and add your current turn total to your overall game score.")
    time.sleep(1)
    print("                            ___                                                                                 ")
    print("However, If you roll a one | ● |  at any point during your turn your score will be reset and your turn will end.")
    print("                           |___|                                                                            ")                    
    print()
    time.sleep(2)
    print("Your misssion, if you chose to accept it, is to reach a total game score of |100| before the computer can.")
    time.sleep(1)
    print("                                                 ")
    print("           Ready to play?             ")
    time.sleep(3)
    print("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧Good Luck ✧ﾟ･: *ヽ(◕ヮ◕ヽ)")
    time.sleep(2)
    print()
    



def roll():
    faceValue=random.randint(1,6)
    return faceValue
                
                    
def playerTurn(player,computer_points):
    faceValue=roll()
    totalPoints=0
    keepGoing=True
    while keepGoing:
        if faceValue==1:
            totalPoints=0
            print("Rolling the die (ﾉ◕ヮ◕)ﾉ*:･ﾟ                  ")
            print("                             _______         ")
            print("                            /\       \       ")     
            print("                           /()\   ()  \      ")    
            print("                          /    \_______\     ")    
            print("                          \    /()     /     ")   
            print("                           \()/   ()  /      ")   
            print("                            \/_____()/       ")
            print("                                             ")
            time.sleep(2)

            print("   ___   ")
            print("  | ● |  ")
            print("  |___|  ")
            print("┗(⊙ .⊙)┛")
            time.sleep(2)
            print()
            print(" You have rolled a 1!\n")
            time.sleep(1)
            print("(╯°□°）╯︵ ┻━┻.\n")
            time.sleep(1)
            print("Your turn is over and your score for this turn has been reset to zero ಥ_ಥ\n")
            keepGoing=False
            break
        else:
            totalPoints=totalPoints+faceValue
            player_points=totalPoints+player
            print()
            print("Rolling the die (ﾉ◕ヮ◕)ﾉ*:･ﾟ                  ")
            print("                             _______         ")
            print("                            /\       \       ")     
            print("                           /()\   ()  \      ")    
            print("                          /    \_______\     ")    
            print("                          \    /()     /     ")   
            print("                           \()/   ()  /      ")   
            print("                            \/_____()/       ")
            print("                                              ")
            time.sleep(2)
            print("\nYou rolled a(~˘▾˘)~",faceValue,"\n")
            time.sleep(1)
            print("                                    ╔══╗             ")
            print("Your current total for this turn is ",totalPoints,"  ~(˘▾˘~)")
            print("                                    ╚══╝             ") 
            if winner(player_points,computer_points):
                break
            time.sleep(1)
            Roll=input("Would you like to roll again? (Y/N) : ")
        if Roll== "Y" in Roll or Roll == "y":
            faceValue=roll()
        
        else: 
            keepGoing=False
            print("You have decided to end your turn.\n")
            print("Your current turn total will be added to your gamescore\n")
           
             

                
           
        
        
    return totalPoints

def computerTurn(player_points,computer):
    faceValue=roll()
    comTotalPoints=0
    keepGoing=True

    while keepGoing:
        faceValue = roll()
        if faceValue==1:
            comTotalPoints=0
            print("Rolling the die (ﾉ◕ヮ◕)ﾉ*:･ﾟ                  ")
            print("                             _______         ")
            print("                            /\       \       ")     
            print("                           /()\   ()  \      ")    
            print("                          /    \_______\     ")    
            print("                          \    /()     /     ")   
            print("                           \()/   ()  /      ")   
            print("                            \/_____()/       ")
            print("                                             ")
            time.sleep(2)
        
            print("   ___   ")
            print("  | ● |  ")
            print("  |___|  ")
            print("┗(⊙ .⊙)┛")
            time.sleep(2)
            print("The computer has rolled a one. ಥ_ಥ its turn score is reset.\n")
            keepGoing=False
            break
        else:
           
            print("Rolling the die (ﾉ◕ヮ◕)ﾉ*:･ﾟ                  ")
            print("                             _______         ")
            print("                            /\       \       ")     
            print("                           /()\   ()  \      ")    
            print("                          /    \_______\     ")    
            print("                          \    /()     /     ")   
            print("                           \()/   ()  /      ")   
            print("                            \/_____()/       ")
            print("                                             ")
            time.sleep(2)
            print("The computer rolled a(~˘▾˘)~",faceValue,"\n")
            comTotalPoints=comTotalPoints+faceValue
            computer_points=comTotalPoints+computer
            time.sleep(1)
            print("                                              ╔══╗             ")
            print("The Computer's current total for this turn is " ,comTotalPoints,"   ~(˘▾˘~)")
            print("                                              ╚══╝             ")
            if winner(player_points,computer_points):
                break
            computerT=random.randint(1,75)
            
            if computerT<30:
                keepGoing=False
                time.sleep(2)
                print("Computer has chosen to end its turn\n")
                print("It's current turn total will be added to it's gamescore.\n")

            
    return comTotalPoints   
    
def winner(player,computer):
    winner=False
    if player >=100:
        time.sleep(1)
        print("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧You have reached 100 points!✧*:･ﾟヽ(◕ヮ◕ヽ)")
        print()
        time.sleep(1)
        print("Player has won the game!")
        print()
        print("WOOHOO DANCE PARTY!")
        print()
        time.sleep(1)
        print("♪┏(・o･)┛♪┗ ( ･o･) ┓♪")
        print("♪°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸♪")
        time.sleep(1)
        print("♪┗ ( ･o･) ┓♪┏(・o･)┛♪")
        print("♪°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸♪")
        time.sleep(1)
        print("♪┏(・o･)┛♪┗ ( ･o･) ┓♪")
        print("♪°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸♪")
        time.sleep(1)
        print("♪┗ ( ･o･) ┓♪┏(・o･)┛♪")
        print("♪°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸♪")
        winner=True
    if computer>=100:
        time.sleep(2)
        print("⚆ _ ⚆ The computer has reached 100 points...")
        print()
        time.sleep(2)
        print("You have lost the game. Computer wins.(ʘ_ʘ)")
        print()
        time.sleep(3)
        print("┬─┬ノ( º _ ºノ)")
        print()
        time.sleep(2)
        print("(╯°□°）╯︵ ┻━┻")
        time.sleep(1)
        print()
        print()
        time.sleep(2)
        print("(づ｡◕‿‿◕｡)づ Don't give up! Play again.\(•◡•)/\n")
        winner=True


    return winner

def main():
    player_points=0
    computer_points=0
    while player_points < 100 and computer_points <100:
        player_points=player_points+playerTurn(player_points,computer_points)
        if player_points >= 100:
            break
        time.sleep(1)
        print("                                            ╔══╗             ")
        print("The Current Game score is: Player (☞ﾟヮﾟ)☞ ",player_points,)
        print("                                            ╚══╝              ")
        time.sleep(1)
        print("            ╔══╗             ")
        print("   Computer:",computer_points," ☜(ﾟヮﾟ☜)")
        print("            ╚══╝              ")
        time.sleep(2)
        print("It is the computers turn.\n")
        computer_points=computer_points+computerTurn(player_points,computer_points)
        if computer_points >= 100:
            break
        time.sleep(1)
        print("                                              ╔══╗             ")
        print("The Current Game score is Computer: (☞ﾟヮﾟ)☞ " ,computer_points, )
        print("                                              ╚══╝              ")
        time.sleep(1)
        print("            ╔══╗             ")
        print("    Player: ",player_points, "  ☜(ﾟヮﾟ☜)")
        print("            ╚══╝             ")
        time.sleep(2)
        print("It is player's turn\n")

        

   
    
            
            
########main code########

welcome()
keepGoing=True
while keepGoing:
    main()
    response=input("Would you like to play another game? (Y/N): ")
    if response != "Y" and response != "y":
        print("Thanks For Playing One Die Jeopardy!")
        time.sleep(1)
        print("May the schwartz be with you")
        print("Live long and prosper")
    
        keepGoing=False


    
