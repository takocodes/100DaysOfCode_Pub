#Day 2 - Activity
# Find out how many days, weeks, and months left before you hit 90 y/o

#declared constants below as integers
YEAR = int(90)
MONTHS = int(12)
WEEKS = int(52)
DAYS = int(365)

#get user input
age = input("What is your age? \n")
intage = int(age)

#compute for years, months, weeks and, days
totalyear = (YEAR) - (intage)
intotalyear = int(totalyear)
totalmonths = ((YEAR)-(intage)) * (MONTHS)
totalweeks = intotalyear * WEEKS
totaldays = intotalyear * DAYS

#print output
print(f"You have {totalyear} years, {totalmonths} months, {totalweeks} weeks, and {totaldays} days before you hit 90 years old.")