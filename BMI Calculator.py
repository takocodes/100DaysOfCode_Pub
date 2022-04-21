# BMI Calculator (This was created as a part of the 100DaysCode Challenge for Python)
# Day 2 - Activity

#get user input
height = input("Enter your height in m: \n")
weight = input("Enter your weight in kg: \n")

#compute BMI using user input (height and weight)
#converted weight into integer
#converted height into a float
#computed for exponential value of height
#computed for the quotient of weight / height
bmi = (round(int(weight) / (float(height) ** 2)))

#prints out result
print(f"Your BMI is: {int(bmi)}")