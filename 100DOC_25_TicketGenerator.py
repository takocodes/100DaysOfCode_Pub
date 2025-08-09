print("Welcome to the rollercoaster!")
height= int(input("What is your height?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 250
        print("Children tickets are P250.00.")
    elif age <= 18:
        bill = 350
        print("Youth tickets are P350.00")
    else:
        bill = 600
        print("Adult tickets are P600.00")
    
    wants_photo = input("Do you want a photo taken? Y or N").upper()
    if wants_photo == "Y":
        ## Add P150.00 to total bill ##
        #total = bill + 150
        bill += 150
        print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")