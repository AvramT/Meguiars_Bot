# Menu for user to choose either click & collect or delivery

# Bugs: 
# - Make it only accept 1 or 2

print ("Is your order for click & collect or delivery?")

print ("For click & collect, please enter 1.")
print ("For delivery, please enter 2.")

low = 1
high = 2

while True:
    try: 
        delivery = int(input("Please enter a number. "))

        if delivery == 1:
            print ("Click & Collect")

        elif delivery == 2:
            print ("Delivery")
            break

    except ValueError:
        print ("That is not a valid number.")
        print ("Please enter 1 or 2.")




