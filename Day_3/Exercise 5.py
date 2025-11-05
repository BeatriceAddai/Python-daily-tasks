print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n ")

#Counting true in the names
lower_case_name = name1.lower()
lower_case_name.count("t")
lower_case_name.count("r")
lower_case_name.count("u")
lower_case_name.count("e")
Total_lower_case_name = lower_case_name.count("t") + lower_case_name.count("r") + lower_case_name.count("u") + lower_case_name.count("e")
 

lower_case_name_name2 = name2.lower()
lower_case_name_name2.count("t")
lower_case_name_name2.count("r")
lower_case_name_name2.count("u")
lower_case_name_name2.count("e")
Total_lower_case_name_name2 = lower_case_name_name2.count("t") + lower_case_name_name2.count("r") + lower_case_name_name2.count("u") + lower_case_name_name2.count("e")

Result_true = (Total_lower_case_name) + (Total_lower_case_name_name2)


#Counting love in the names
lower_case_name = name1.lower()
lower_case_name.count("l")
lower_case_name.count("o")
lower_case_name.count("v")
lower_case_name.count("e")
Total_lower_case_name = lower_case_name.count("l") + lower_case_name.count("o") + lower_case_name.count("v") + lower_case_name.count("e")



lower_case_name = name2.lower()
lower_case_name.count("l")
lower_case_name.count("o")
lower_case_name.count("v")
lower_case_name.count("e")
Total_lower_case_name_name2 = lower_case_name.count("l") + lower_case_name.count("o") + lower_case_name.count("v") + lower_case_name.count("e")

Result_love = (Total_lower_case_name) + (Total_lower_case_name_name2)
Love_Score = str(Result_true) + str(Result_love)


print(f"Your score is  {Love_Score} ") 

if Love_Score < "10" or Love_Score > "90":
    print(f"Your score is {Love_Score}, you go together like coke and mentos ")

elif Love_Score >= "40" and Love_Score <="50":
    print("Your score is {Love_Score} you are alright together")
else:
     print(f"Your score is {Love_Score}")

