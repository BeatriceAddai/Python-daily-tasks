import random
names_string = input("Give me everybody's names, separated by comma.")
names = names_string.split(",")

#Get the total number of items in list
length_names = len(names)
names_choice= random.randint(0, length_names-1) 
who_will_pay = names[names_choice]


print(who_will_pay + " is going to pay the bill")



