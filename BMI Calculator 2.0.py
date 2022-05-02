#Day 3 - BMI Calculator v2

# Greetings
from traceback import print_tb


print("This is a beginner level BMI calculator. This program will simply compute for your BMI and the result will be based from your age, height and, weight. \n \n")

# Get user input while converting height to float and weight to int //and age to int.//
height = float(input("Enter your height in m: \n"))
weight = int(input("Enter your weight in kg: \n"))
# age = int(input("Enter your age: \n"))

# Compute BMI using user input (height and weight)
# Compute for exponential value of height
# Compute for the quotient of weight / height
bmi = (round(weight) / (height) ** 2)

# Prints out result
print(f"Your BMI is: {int(bmi)} \n")

# Checking to see if underweight
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("Your weight is normal.")
elif bmi > 25 and bmi < 30:
    print("You are overweight.")
elif bmi > 30 and bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
