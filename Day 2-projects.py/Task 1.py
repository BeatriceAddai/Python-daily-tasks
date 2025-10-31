#Print the last character of a string 
#print("hello" [ 4]  )

#A program to add digits in 2 digit number
#two_digit_number = input("Enter your two digit number: ")

#first_digit = int(two_digit_number [0])
#second_digit = int(two_digit_number[1])
#result = first_digit + second_digit
#print(result)

#A program to calculate BMI 
#weight = input("Enter your weight in kg: ")
#height = input("Enter your height in m: ")
#print(type(weight))
#print(type(height))
#BMI = int(weight) / float(height) ** 2
#BMI_nearest_num = int(weight) // float(height) ** 2

#print(BMI)
#print(BMI_nearest_num)

#A program to calculate days, weeks and months left if you live until 90 years old
#age = input("What's your current age?")
# age_as_int = int(age)

#years_remaining = 90 - age_as_int
#days_remaining = years_remaining * 365
#weeks_remaining = years_remaining * 52
#months_remaining = years_remaining * 12

#message = (f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
#print(message)

#A tip calculator
# If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00/ 5) * 1.12 = 33.6
#Round the result to 32 decimal places = 33.

print("Welcome to the tip calculator.")

Total_bill = float(input("What was the total bill in $? "))
print(type(Total_bill))



Percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15 "))


Percentage_tip_calculate = Percentage_tip / 100 * Total_bill

Total_bill += Percentage_tip_calculate

People = int(input("How many people to share the bill? "))
Each_pay = Total_bill/ People  

print("Each person pay: $" + str(round(Each_pay, 2)) + " ")
