print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
   ''')




print("Welcome to Treasure Island!")
print("Your mission is to find the treasure")
print("You're at the cross road. ")

which_direction = input('Where do you want to go? Type " left" or "right" ' )
lower_case_left = which_direction.lower()


if which_direction == "right":
    print("Oops, you've landed in your enemy's camp. Going back is impossible")

else:
    print("You have come to a lake. There is an Island in the middle of the lake")

Lake_cross = input(' Type wait to "wait" for a boat or type "swim" to swim across ')
lower_case_left = Lake_cross.lower()




if Lake_cross == "swim":
    print("Game over! The lake is poisoned.")

if  Lake_cross == "wait":
    colour = input('You arrived at the Island unharmed. There is a house with three doors. One "red", one "yellow" and one "blue". Which colour do want to choose? ')
    if colour == "blue":
        print("You've entered a beast room. Game over")
    elif colour == "red":
        print("You've entered washroom. Game over")
    elif colour == "yellow":
      print("Congrats ! you've won! Go for the treasure. You're a millionire now!")
    else:
      print("You chose a door that doesn't exist. Game over")

    