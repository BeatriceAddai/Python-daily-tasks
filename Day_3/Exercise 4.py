#A program to build an automatic pizza order program
print("Welcome to Python Pizza Deliveries")
size = input("Which size of the pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Yes or No")
extra_cheese = input("Want extra cheese? Yes or No ")



Total_Bill = 0
if size == "S":
    Total_Bill  += 50 
    print("The Small size is $50")

elif size == "M":
     Total_Bill += 100
     print("The Medium size is $50")
else : 
    Total_Bill  += 150
    print("The Large size is $150")

if add_pepperoni == "Yes":
    if size == "S":
        Total_Bill += 2
    else:
        Total_Bill + 3

if extra_cheese == "Yes":
        Total_Bill += 1
     
print(f"Your final bill is $ {Total_Bill}")
     
     
     

     
     

    


