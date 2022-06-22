#Day 4 - Leap Year #

# Greetings #
print("This is a beginner level Applciation, this program will simply determine if the entered year is a Leap Year. \n \n")

# Get user input #
year = int(input("Which year do you want to check? \n"))

# Determine if the year that user entered is a Leap Year #
# Conditions are: #
# 1. on every year that is evenly divisible by 4 #
# 2. except every year that is evenly divisible by 100 #
# 3. unless the year is also evenly divisible by 400 #

if year % 4 == 0 and year % 400 != 0 and year % 100 != 0:
    print("The year you entered is a Leap Year")
else:
    print("The entered year is not a Leap Year")