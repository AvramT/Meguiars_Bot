import random
from random import randint

# List of random names
names = ["Patrick", "Sonia", "Ricky", "Veronica", "Gary", "Louis", "Mary", "Ed", "Jose", "Carlos"]

# Welcome message with random name generator
def welcome():
    num = randint(0,9)

    name = (names[num])

    print("*** Welcome to Meguiar's! ***")
    print("*** My name is",name,"***")
    print("*** I'll be here to help you order New Zealand's finest car-care products. ***")

# Menu for click & collect or delivery

def order_type():
    print("Is your order for click & collect or delivery?")

    print("For click & collect, please enter 1.")
    print("For delivery, please enter 2.")

    while True:
        try: 
            delivery = int(input("Please enter a number. "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Click & Collect")
                    break

                elif delivery == 2:
                    print("Delivery")
                    break
            else:
                print("The number must be 1 or 2.")
        except ValueError:
            print("That is not a valid number.")
            print("Please enter 1 or 2.")


# Main function
def main():
    welcome()
    order_type()

main()


