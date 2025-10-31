#A program to calculate BMI 
weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ") 
print(type(weight))
print(type(height))
BMI = int(weight) / float(height) ** 2
BMI_nearest_num = int(weight) // float(height) ** 2

print(BMI)
print(BMI_nearest_num)
