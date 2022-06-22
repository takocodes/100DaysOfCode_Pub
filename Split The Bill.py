#Day 2 - Activity
#This is a simple Tip Calculator program created for #100DaysOfCode Challenge for Python

#get user input
#change user input to appropriate variable type (int, float)
bill = float(input("What is your total bill? \n"))
percentage = int(input("how many percentage of tip do you want to give? \n"))
headcount = int(input("how many people to split the bill? \n"))

#compute for total amount of tip per headcount

totaltip = percentage / 100 * bill
final_tip = "{:.2f}".format(totaltip)
totalbill = (totaltip + (bill)) / headcount
final_amount = "{:.2f}".format(totalbill)

#print result showing total tip per head and overall total bill per head
print(f"Total tip per head is : {final_tip} \n")
print(f"Each person should pay: {final_amount} \n")