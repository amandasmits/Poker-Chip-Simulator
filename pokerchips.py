print("Welcome to the digital alternative to poker chips")
print("Be warned, there's nothing stopping you from going into debt, so don't get yourself into digital debt you're going to have to pay off later!")

while True: 
    #this takes string input for how many players are playing, and checks to make sure there's no non-alphabetical
    #characters in it, then once we know it's a valid int it casts the int value to a new variable to use in the 
    #rest of the program
    players = (input("Please enter how many players are playing (and remember poker can only have 2-10 players): "))
    if (("." in players) or (players.isdigit()== False)):
        print("That's not a nice whole number of players, try again")
    elif (int(players) <2 or int(players) >10):
        print("that's not a valid number of players, please try again")
    else:
        numberofplayers = int(players)
        break

while True:
    #this takes input for how much money each player starts with, starting as a string and then
    #once it checks that there's no alphabetical characters it converts the string to an int variable
    #to be used for the rest of the program
    startingamount = input("Please enter how much money each player starts with: ")
    if ("." in startingamount):
        print("sorry, there's no cents in poker, please enter a whole dollar value")
    elif (startingamount.isdigit() == False):
        print("sorry, those aren't all numbers, please try again")
    else:
        startingmoney = int(startingamount)
        break


#this initializes the player names to null strings because some of the functions used later
#are written for 10 players and then just don't have output for less than that, but the strings
#still need to exist for the functions to work (and yes Steven I am aware this is not an optimal use of memory)
player1=player2=player3=player4=player5=player6=player7=player8=player9=player10=""

#this initializes all of the players to have the same starting amount of money regardless of how many
#players there are for the same reason as above, easier to reuse functions in this case than to optimize the memory use
#(note to self make a version that gives you extra money lol)
player1total=player2total=player3total=player4total=player5total=player6total=player7total=player8total=player9total=player10total=startingmoney

def bet():
    '''this function is for subtracting the money from the account of whoever is betting, it checks to make sure that 
    the name of the player betting is a valid player, and it outputs that player's current total and adds the amount that was 
    bet to the pot, so that amount can later be added to the balance of whoever wins the pot'''

    while True:
        #this asks whose turn it is so we know who is making the bet, and checks to make sure
        #that the name entered is actually a player
        turn = input("please enter whose turn it is to bet")
        if (turn == player1 or turn == player2 or turn==player3 or turn==player4 or turn==player5 or turn==player6 or turn==player7 or turn == player8 or turn==player9 or turn==player10):
            break
        else:
            print("not a valid player name, please try again")

    while True:
        #this takes the amount that was bet and checks to make sure that it is a valid amount
        #this works the same way as checking the input bet does
        betattempt = input("Please enter how much money the bet is: ")
        if ("." in betattempt):
            print("sorry, there's no cents in poker, please enter a whole dollar value")
        elif (betattempt.isdigit() == False):
            print("sorry, those aren't all numbers, please try again")
        else:
            betnumber = int(betattempt)
            break

    #this section of if statements subtracts the amount that was bet from the player's total, it already checked that 
    #the name entered was a valid player earlier, then it outputs the player's name and total
    #and returns the amount that was bet to be added to the pot, which is counted in the game function
    if (turn == player1):
        global player1total #makes player global because otherwise it can't be accessed
        player1total -=betnumber #takes the amount they're betting out of the account
        print(player1, "your current balance is" , player1total) #prints current balance
    elif (turn == player2):
        global player2total
        player2total -= betnumber
        print(player2, "your current balance is" , player2total)
    elif (turn == player3):
        global player3total
        player3total -= betnumber
        print(player3, "your current balance is" , player3total)
    elif (turn == player4):
        global player4total
        player4total -=betnumber
        print(player4, "your current balance is" , player4total)
    elif (turn == player5):
        global player5total
        player5total -=betnumber
        print(player5, "your current balance is" , player5total)
    elif (turn == player6):
        global player6total
        player6total -= betnumber
        print(player6, "your current balance is" , player6total)
    elif (turn == player7):
        global player7total
        player7total -= betnumber
        print(player7, "your current balance is" , player7total)
    elif (turn == player8):
        global player8total
        player8total -=betnumber
        print(player8, "your current balance is" , player8total)
    elif (turn == player9):
        global player9total
        player9total -=betnumber
        print(player9, "your current balance is" , player9total)
    else:
        global player10total
        player10total -= betnumber
        print(player10, "your current balance is" , player10total)
    return (betnumber) #returns the bet so that it can be added to the pot
    

def win():
    '''this is for adding money to the account of whoever won the hand'''
    while True:
        #this asks whose turn it is so we know who is making the bet, and checks to make sure
        #that the name entered is actually a player, and it uses the same variable as the other one because
        #I copied the structure of the code, but turn is a local variable so it's fine
        turn = input("please enter the name of the winner")
        if (turn == player1 or turn == player2 or turn==player3 or turn==player4 or turn==player5 or turn==player6 or turn==player7 or turn == player8 or turn==player9 or turn==player10):
            break
        else:
            print("not a valid player name, please try again")


    #this section of if statements adds the total of the pot to the player's total 
    if (turn == player1):
        global player1total
        player1total += pot
    elif (turn == player2):
        global player2total
        player2total += pot
    elif (turn == player3):
        global player3total
        player3total += pot
    elif (turn == player4):
        global player4total
        player4total += pot
    elif (turn == player5):
        global player5total
        player5total += pot
    elif (turn == player6):
        global player6total
        player6total += pot
    elif (turn == player7):
        global player7total
        player7total += pot
    elif (turn == player8):
        global player8total
        player8total += pot
    elif (turn == player9):
        global player9total
        player9total += pot
    else:
        global player10total
        player10total += pot 
    finaloutput()

def finaloutput():
    '''this outputs the totals balance each player is at'''
    #I did end up using this other times than just the end of game final output but whatevs
    print(player1, "your total is", player1total)
    print(player2, "your total is", player2total)
    if (numberofplayers >= 3):
        print(player3, "your total is", player3total)
    if (numberofplayers >=4):
        print(player4, "your total is", player4total)
    if (numberofplayers >=5):
        print(player5, "your total is", player5total)
    if (numberofplayers >=6):
        print(player6, "your total is", player6total)
    if (numberofplayers >=7):
        print(player7, "your total is", player7total)
    if (numberofplayers >= 8):
        print(player8, "your total is", player8total)
    if (numberofplayers >= 9):
        print(player9, "your total is", player9total)
    if (numberofplayers == 10):
        print(player10, "your total is", player10total)

def printwinner():
    '''this defines and prints the winner, and it keeps it so that if nobody bets it's only the players that played that were defined as winners'''
    totallist = [player1total, player2total, player3total, player4total, player5total, player6total, player7total, player8total, player9total, player10total]
    winnertotal = max(totallist) #this gets the highest value to determine the winner
    tiecounter=0 #this counts how many winners there are
    if (winnertotal == player1total):
        print(player1, "is the winner, congrats!!! You had", player1total, "dollars")
        tiecounter+=1
    if (winnertotal == player2total):
        print(player2, "is the winner, congrats!!! You had", player2total, "dollars")
        tiecounter+=1
    if ((winnertotal == player3total) and (player3 !="")):
        print(player3, "is the winner, congrats!!! You had", player3total, "dollars")
        tiecounter+=1
    if ((winnertotal == player4total) and (player4 !="")):
        print(player4, "is the winner, congrats!!! You had", player4total, "dollars")
        tiecounter+=1
    if ((winnertotal == player5total) and (player5 !="")):
        print(player5, "is the winner, congrats!!! You had", player5total, "dollars")
        tiecounter+=1
    if ((winnertotal == player6total)and (player6 != "")):
        print(player6, "is the winner, congrats!!! You had", player6total, "dollars")
        tiecounter+=1
    if ((winnertotal == player7total) and (player7 != "")):
        print(player7, "is the winner, congrats!!! You had", player7total, "dollars")
        tiecounter+=1
    if ((winnertotal == player8total) and (player8 !="")):
        print(player8, "is the winner, congrats!!! You had", player8total, "dollars")
        tiecounter+=1
    if ((winnertotal == player9total) and (player9 !="")):
        print(player9, "is the winner, congrats!!! You had", player9total, "dollars")
        tiecounter+=1
    if ((winnertotal == player10total) and (player10 !="")):
        print(player10, "is the winner, congrats!!! You had", player10total, "dollars")
        tiecounter+=1
    
    #these get printed if there's ties
    if (tiecounter ==2):
        print("danggggg you tied! Guess you're gonna have to brawl this one out")
    if (tiecounter ==3):
        print("I think there might have been some collusion here, no way all 3 of you ended up with the same amount...")
    if (tiecounter >3):
        print("I guess you're all bad at poker that a lot of ties")

def game():
    '''this is the function for the actual playing of the game that calls all the other functions'''
    play = True  #keeps track of if whole game is still going
    while (play == True):
        round = True #keeps track of if current hand is still going (or round)
        global pot
        pot = 0 #initializes the pot to 0 for the start of every round
        while (round == True):
            addamount= bet() #bet() returns the amount that was bet and that variable just holds
            pot+=addamount #keeps track of the total of all the bets to add to someone's hand
            keepgoing = input("did someone win the pot yet? ")
            if (keepgoing == "yes" or keepgoing == "y" or keepgoing == "yeah" or keepgoing == "yee haw" or keepgoing == "yes please"):
                round = False
                win()
        keepplaying = input("would you like the game to continue? ")
        if (keepplaying == "no" or keepplaying == "n" or keepplaying == "nope" or keepplaying == "no thanks"): #means the game is over, there are no more rounds of betting
            play = False
    finaloutput()
    printwinner()

#below is essentially the main function where the game is played, it's just the game function 
#and the inputs for all the player names depending on how many players there are
namelist = [] #this holds all the names so we can check and make sure two people don't have the same name
def nameget(playernumber):
    '''this gets the input for the player names, and checks to make sure it's a valid input'''
    while True:
        print("please enter the name of player", playernumber)
        person = input()
        person.strip() #this gets rid of whitespace in case they enter a space, because then they'd
                       #have to enter the same thing every time and that would get frustrating fast
        if (person in namelist):
            print("sorry, that name is already taken, please try again")
        elif (person == ""): #if this was the name the person would never win
            print("sorry, you need to enter a real name, try again")
        else:
            break
    namelist.append(person)#adds the person's name to the list
    return (person) #returns the name so it can be assigned to the variable

#this set of if statements sets names depending on how many players there are, if
#one doesn't get set it stays as the "" that was initialized at the start
player1 = nameget(1)
player2 = nameget(2)
if (numberofplayers >= 3):
    player3 = nameget(3)
if (numberofplayers >=4):
    player4 = nameget(4)
if (numberofplayers >=5):
    player5 = nameget(5)
if (numberofplayers >=6):
    player6 = nameget(6)
if (numberofplayers >=7):
    player7= nameget(7)
if (numberofplayers >= 8):
    player8= nameget(8)
if (numberofplayers >= 9):
    player9= nameget(9)
if (numberofplayers == 10):
    player10 = nameget(10)
game()