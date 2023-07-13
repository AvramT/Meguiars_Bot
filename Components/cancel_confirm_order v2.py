print ("Please confirm your order.")

print ("To confirm, please enter 1.")
print ("To cancel, please enter 2.")

while True:
    try: 
        confirm = int(input("Please enter a number. "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print("Order confirmed!")
                print("It has been sent to the factory and your products will be with you ASAP.")
                break

            elif confirm == 2:
                print("Your order has been cancelled.")
                print("You can restart your order or exit the BOT.")
                break
        else:
            print("The number must be 1 or 2.")
    except ValueError:
        print("That is not a valid number.")
        print("Please enter 1 or 2.")

