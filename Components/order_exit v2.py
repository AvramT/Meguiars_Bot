import sys

order_list = []
order_cost = []
customer_details = {}


print ("Would you like to order again or exit?")

print ("To order again, please enter 1.")
print ("To exit the BOT, please enter 2.")

while True:
    try: 
        confirm = int(input("Please enter a number. "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print("New Order:")
                order_list.clear()
                order_cost.clear()
                customer_details.clear()
                break

            elif confirm == 2:
                print("Exiting...")
                order_list.clear
                order_cost.clear()
                customer_details.clear
                sys.exit()
                break
        else:
            print("The number must be 1 or 2.")
    except ValueError:
        print("That is not a valid number.")
        print("Please enter 1 or 2.")
