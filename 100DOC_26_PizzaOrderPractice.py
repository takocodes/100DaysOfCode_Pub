print ("Welcome to Python Pizza Deliveries!")
bill = 0

## to-do: Work out how much they need to pay based on their size choice. ##
size = input("What size pizza do you want? S, M, or L: ").upper()
if size == "S":
    bill = 300
        ## 300 for small pizza ##
elif size == "M":
    bill = 400
        ## 400 for medium pizza ##
else:
    bill = 500
        ## 500 for large pizza ##

## to-do: Work out how much to add to their bill based off their pepperoni choice. ##
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
if add_pepperoni == "Y":
    if size == "S":
        bill += 20
    elif size == "M":
        bill += 30
    else:
        bill += 40
        ## Add P20.00 for small, P30.00 for medium, and P40.00 for large ##
        
## to-do: Work out their final amount based on whether they want extra cheese or not. ##
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
if extra_cheese == "Y":
    bill += 50
    ## Add P50.00 to the bill if they want extra cheese ##

print(f"Your final bill is P{bill}.00 ! Thank you for ordering!")