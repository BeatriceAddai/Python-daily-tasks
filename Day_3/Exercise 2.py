#A program that interprets the Body Mass Index (BMI) based on a user's weight and height
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = round(weight / height**2)
print(f"Your BMI is { BMI }")

if BMI < 18.5:
    print("You're are underweight")
elif BMI < 25:
    print("You have a normal weight")
elif BMI < 30:
    print("You're overweight")
elif BMI < 35:
     print("You're obese")
else:
    print("Sorry but you're clinically obese.")



