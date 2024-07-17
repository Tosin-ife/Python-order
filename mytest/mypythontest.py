# Welcome quotes
print("Hello, welcome to Teehanz Cloud!!!!\n")

# Asking the customer for their name to know their records
name = input("What is your name?!!!!\n")

# Checking for their credit records with us
# checking there credit score to be certain they are truly aying the truth
if name == "Ben" or name == "Pat":
    credit_status = input("Is your credit score low? (yes/no)\n")
    credit_score = int(input("What is your credit score number?\n"))
    if credit_status.lower() == "yes" and credit_score < 450:
        print("Apologies, " + name + ", your low credit score restricts access.")
        exit()
    else:
        print("Well, now we can clear your record with us and charge to your card.\n")
else:
    print("Hello " + name + ", thank you so much for coming today!!!!!\n\n")

# If the name is relating to the if statement, it will back out
menu = "Black coffee, Espresso, Latte, Cappuccino, Frappuccino"

print(name + ", what would you love to have from the menu today? Here is what we are serving:\n\n" + menu)

# Time to ask for the price of the commodity
# Setting prices for coffee
order = input()

if order == "Frappuccino":
    price = 13
elif order == "Black coffee":
    price = 9
elif order == "Cappuccino":
    price = 12
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 8
else:
    print("Sorry, we don't have that here!!!!")
    price = 0

if price != 0:
    quantity = input("How many coffees would you like to order?\n")
    total = price * int(quantity)

    # Printing out the total cost of the coffee bought
    print("Your total is: $" + str(total))
    print("Sounds good " + name + ", we'll have your " + quantity + " " + order + "(s) ready for you in a moment!!!")
