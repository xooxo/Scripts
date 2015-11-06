#!/usr/bin
#####BATTLESHIPS-Mert ARIKAN#####
#

import random

comp_ships=[]
pc_ships=[]
numbers=[1,2,3,4,5,6,7,8,9,10]
letters=["A","B","C","D","E","F"]
comp_guess=[] #for saving previous guesses
order=["player"] #determine whose order.

    
##Computer Ships##
i=0
while i!=5:
    if random.choice(letters)+str(random.choice(numbers))in comp_ships:
        continue
    else:
        comp_ships.append(random.choice(letters)+str(random.choice(numbers)))
        i+=1
    if i==5:
        break


##Player Ships##
j=0
while j!=5:
    coordinate=raw_input("Please enter your ship coordinate")
    if coordinate=="":
        print("There is not any coordinate like this")
    elif not coordinate[0].upper() in letters or not coordinate[1] in str(numbers):
        print "There is not any coordinate like this."
    elif not coordinate.upper() in pc_ships:
        pc_ships.append(coordinate.upper())
        j+=1
    elif coordinate.upper() in pc_ships:
        print("You have a ship at this coordinate")
        
    if j==5:
        break
    
##FIGHT!##
while len(pc_ships)!=0 or len(comp_ships)!=0:
    while order==["player"]:
        shot=raw_input("Please enter coordinate to shoot> ")
        if shot=="":
            print "There is not any coordinate like this."
        elif not shot[0].upper() in letters or not shot[1] in str(numbers):
            print("There is not any coordinate like this!")
        elif shot.upper() in comp_ships:
            print("You shoot!")
            comp_ships.remove(shot)
            print("Computer have %d ship(s)!" %(len(comp_ships)))
        elif not shot.upper() in comp_ships:
            print("You miss!")
            order.append("opponent")
            order.remove("player")

    while order==["opponent"]:
        comp_choice=random.choice(letters)+str(random.choice(numbers))
        ####Time to add some action! :)###
        if not comp_choice in comp_guess:
            comp_guess.append(comp_choice)
        else:
            while comp_choice in comp_guess:
                comp_choice=random.choice(letters)+str(random.choice(numbers))
                if not comp_choice in comp_guess:
                    break
        ################################
        if comp_choice in pc_ships:
            print("Comp shoot your %s ship!" %(comp_choice))
            pc_ships.remove(comp_choice)
            print("You have %d ship(s)!" %(len(pc_ships)))
        elif not comp_choice in pc_ships:
            print("Comp shoot %s ;but miss!" %(comp_choice))
            order.append("player")
            order.remove("opponent")

    if len(pc_ships)==0:
        print("You lose!")
        break
    elif len(comp_ships)==0:
        print("You won!")
        break




