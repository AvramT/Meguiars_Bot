# Menu for user to choose either click & collect or delivery

print("Is your order for click & collect or delivery?")

print("For click & collect, please enter 1.")
print("For delivery, please enter 2.")

while True:
    try: 
        delivery = int(input("Please enter a number. "))
        if delivery >= 1 and delivery <= 2:
            if delivery == 1:
                print ("Click & Collect")
                break

            elif delivery == 2:
                print ("Delivery")
                break
        else:
            print("The number must be 1 or 2.")
    except ValueError:
        print ("That is not a valid number.")
        print ("Please enter 1 or 2.")

        



