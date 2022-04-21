#Day 2 - Activity
#This is a simple Tip Calculator program created for #100DaysOfCode Challenge for Python

#get user input
#change user input to appropriate variable type (int, float)
bill = float(input("What is your total bill? \n"))
percentage = int(input("how many percentage of tip do you want to give? \n"))
headcount = int(input("how many people to split the bill? \n"))

#compute for total amount of tip per headcount

totaltip = percentage / 100 * bill
totalbill = (totaltip + (bill)) / headcount

#print result showing total tip per head and overall total bill per head
print(f"Total tip per head is : {totaltip} \n")
print(f"Total bill(tip included) per head is: {totalbill} \n")