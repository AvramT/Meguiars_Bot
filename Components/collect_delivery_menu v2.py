# Menu for user to choose either click & collect or delivery
print("Do you want your order delivered or will you collect it?")

print("For delivery, enter 'd' or enter 'c' for click & collect.")

delivery = input()

if delivery == "d":
    print("Delivery")

elif delivery == "c":
    print("Click & Collect")

else:
    print("That was not a valid input.")




