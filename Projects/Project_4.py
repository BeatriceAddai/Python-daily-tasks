rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print("Welcome to Rock, Scissors and Paper Game!")
what_user_chooses = int(input("What do you want to choose? Type 0 for rock, 1 for paper and 2 for scissors "))

if what_user_chooses == 0:
    print(rock)
elif what_user_chooses == 1:
    print(paper)
elif what_user_chooses == 2:
    print(scissors)
else:
    print("This is a wrong option.")
 
print("Computer chose: ")
what_computer_chooses = random.randint(0, 2)

if what_computer_chooses == 0:
    print(rock)
elif what_computer_chooses == 1:
    print(paper)
elif what_computer_chooses == 2:
    print(scissors)
    


if what_user_chooses >= 3 or  what_user_chooses < 0:
    print("Wrong option, try again")

elif what_user_chooses == 0 and what_computer_chooses == 2:
    print("You wins")
elif what_computer_chooses == 0 and what_user_chooses == 2:
    print("You lose")

elif what_computer_chooses > what_user_chooses:
    print(" You lose")

elif what_computer_chooses < what_user_chooses:
    print("You win")
elif what_computer_chooses == what_user_chooses:
    print("It's a draw")



#My first trail didn't run exactly how it should be. Can anyone explain it to me?

# if what_computer_chooses == 0 and what_user_chooses == 0:
#     print("It's a draw")
# elif what_computer_chooses == 1 and what_user_chooses == 1:
#     print("It's a draw")
# elif what_computer_chooses == 2 and what_user_chooses == 2:
#     print("It's a draw")

# elif what_computer_chooses == 0 or what_user_chooses == 1:
#     print("You win") #ok
        
# elif what_computer_chooses == 1 or what_user_chooses == 0:
#     print("You lose, the computer wins") # ok




# elif what_computer_chooses == 1 and what_user_chooses == 2:
   
#     print("You win") #


# elif what_user_chooses == 0 and what_computer_chooses == 2:

#     print("You win")#


# else:
#     print("Wrong option, try again")     


