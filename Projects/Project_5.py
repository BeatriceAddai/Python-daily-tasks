#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#Eazy Level
Password = ""
length_letters = len(letters)
for i in range(1, nr_letters + 1):
    random_letters = random.randint(0, length_letters-1) 
    user_letters = letters[random_letters]
    Password +=  user_letters

length_symbols = len(symbols)
for n in range(1, nr_symbols + 1):
    random_symbol = random.randint(0, length_symbols-1)
    user_symbol = symbols[random_symbol]
    
    Password +=  user_symbol

length_numbers = len(numbers)
for n in range(1, nr_numbers + 1):
    random_numbers = random.randint(0, length_numbers-1)
    user_choice = numbers[random_numbers]
    Password +=  user_choice

print(f" Your   Password is:  {Password} ")

#Another Easy way
# Password = ""
# for char in range(1, nr_letters + 1):
#     Password += random.choice(letters) 

# for char in range(1, nr_symbols + 1):
#     Password += random.choice(symbols) 

# for char in range(1, nr_numbers + 1):
#     Password += random.choice(numbers) 

# print(f" Your   Password is:  {Password} ")

 
#Hard Level
# Password_List = []
# for char in range(1, nr_letters + 1):
#     Password_List += random.choice(letters) 

# for char in range(1, nr_symbols + 1):
#     Password_List += random.choice(symbols) 

# for char in range(1, nr_numbers + 1):
#     Password_List += random.choice(numbers) 

# print(Password_List)
# random.shuffle( Password_List )
# print(Password_List)

#Converting  it back to string
# Password = ""
# for char in Password_List:
#     Password += char

# print(f" Your   Password is:  {Password} ")


