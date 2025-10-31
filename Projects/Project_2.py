#A tip calculator
# E.g If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00/ 5) * 1.12 = 33.6
#Round the result to 32 decimal places = 33.
print("Welcome to the tip calculator.")

Total_bill = float(input("What was the total bill in $? "))  

Percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15 "))


Percentage_tip_calculate = Percentage_tip / 100 * Total_bill

Total_bill += Percentage_tip_calculate

People = int(input("How many people to share the bill? "))
Each_pay = Total_bill/ People  

print("Each person pay: $" + str(round(Each_pay, 2)) + " ")
