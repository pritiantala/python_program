import random
from select import select
#team selection
#--------------------------------------------------
print("------------------SECTION OF TEAM-----------------------------")
list=["csk","kkr","kxip","rcb","rr","gt","lsg","dc","sh","mi"]
select_team=input("enter one team:")
i=list.index(select_team)
print(i)
list.pop(i)
print(list)

second_team=random.choice(list)
print(select_team ,"VS",second_team)

#TOSS FOR TEAM---------------------------------

print("\nHere comes the Toss")
toss = (input("Choose heads or tails: ")).lower()
 
random_toss = random.randint(1,2)            # In random_toss (1 = Heads) and (2 = Tails)
random_opt = random.randint(1,2)             # In random_opt (1 = bat) and (2 = ball)
 
u_opt = 0
c_opt = 0
 
if random_toss == 1 and toss == "heads":
    print(select_team," won the toss")
    u_opt = (input("Choose bat or ball: ")).lower()
 
elif random_toss == 2 and toss == "tails":
    print(select_team,"won the toss")
    u_opt = (input("Choose bat or ball: ")).lower()    
  
else:
    print("\nYou lost the toss")
 
    if random_opt == 1:
        c_opt = "bat"
        print(second_team,"choose to",c_opt)
 
    elif random_opt == 2:
        c_opt = "ball"
        print(second_team," choose to",c_opt)

#first innings------------------------------------------
print("\n---------- First Innings Begins ----------")
 
runs_1 = 0
wickets_1 = 0
balls_1 = 0
 
while wickets_1 != 2 and balls_1 != 12:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 1 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6 for update your score")
 
    else:
        print(select_team," choice: ",u_choice,"\n", second_team,"choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_1 += 1
 
        else:
            if u_opt == "bat" or c_opt == "ball":
                Bat_first = "You"
                Ball_first = "Computer"
                runs_1 += u_choice
 
            elif u_opt == "ball" or c_opt == "bat":
                Bat_first = "Computer"
                Ball_first = "You"
                runs_1 += c_choice
 
        print(select_team,"Score =",runs_1,"/",wickets_1)
 
        balls_1 += 1
 
        if balls_1 == 5:
            print("End of Over 1")
 
        elif balls_1 == 10:
            print("End of Over 2")
 
        print("Balls remaining: ",10 - balls_1)
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:",select_team)
print("Runs =",runs_1)
print("wickets =",wickets_1)
 
print("\n",Ball_first,"needs",runs_1 + 1,"runs to win.")
 
# Second Innings --------------------------------------------
 
print("\n---------- Second Innings Begins ----------")
 
runs_2 = 0
wickets_2 = 0
balls_2 = 0
 
while wickets_2 != 2 and balls_2 != 10 and runs_2 <= runs_1:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 1 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")
 
    else:
        print(select_team,"choice: ",u_choice,"\n",second_team," choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_2 += 1
 
        else:
            if Bat_first == "Computer": 
                runs_2 += u_choice
                Bat_second = "You"
 
            elif Bat_first == "You":
                runs_2 += c_choice
                Bat_second = "Computer"
 
        print(second_team,"Score =",runs_2,"/",wickets_2)
 
        balls_2 += 1
 
        if balls_2 == 6:
            print("End of Over 1")
 
        elif balls_2 == 12:
            print("End of Over 2")
 
        if runs_2 <= runs_1 and balls_2 <= 9 and wickets_2 != 2:
            print("To win:",runs_1 - runs_2 + 1,"runs needed from",10 - balls_2,"balls.")
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:",second_team)
print("Runs =",runs_2)
print("wickets =",wickets_2)
 
# Result of Match -----------------------------------
 
print("\n~~~~~~~~~~ Result ~~~~~~~~~~")
 
if runs_1 > runs_2:
 
    if Bat_first == "You": 
        print("\nCongratulations! ",select_team,"You won the Match by",runs_1 - runs_2,"runs.")
 
    else:
        print("\nBetter luck next time! ",second_team," won the Match by",runs_1 - runs_2,"runs.") 
 
elif runs_2 > runs_1:
 
    if Bat_second == "You": 
        print("\nCongratulations!",select_team," You won the Match by",2 - wickets_2,"wickets.")
 
    else:
        print("\nBetter luck next time!",second_team," won the Match by",2 - wickets_2,"wickets.")
 
else:
    print("The Match is a Tie.","\nNo one Wins.")