# Meguiars Bot

# Imported modules
import sys
# - Provides various functions and variables used to manipulate 
#   different parts of the Python runtime environment.
import random
# - Generates random numbers in Python.
from random import randint
# - Returns an integer from specific range of numbers.

# List of random names for welcome message
names = ["Patrick", "Sonia", "Ricky", "Veronica",
         "Gary", "Louis", "Mary", "Ed", "Jose", "Carlos"]

# List of product names
product_names = ['Wash Mitt', 'Wheel & Tire Cleaner (710ml)', 'Leather Cleaner/Conditioner (450ml)', 'Wash & Wax (1.7L)', 'Snow Foam (1.9L)', 'Wheel Brush', 'Ultimate Compound (450ml)',
                 'Glass Cleaner (710ml)', 'Microfibre Towel (3 pack)', 'Foam Applicator Pads (2 pack)', 'Headlight Restoration Kit', 'Cleaner Wax Paste (311g)']

# List of product prices
product_prices = [34.99, 33.99, 39.99, 66.99, 97.19,
                  22.99, 48.50, 23.99, 32.99, 10.99, 67.99, 46.95]

# List to store ordered products 
# - Appends the names of the products ordered by the user.
order_list = []

# List to store products prices
# - Appends the prices of the products ordered by the user.
order_cost = []

# Customer details dictionary
# - A dictionary (list) that stores data, which in this case is the user's details.
customer_details = {}

# Validates inputs to check if they are blank

def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank.")

# Validates input to check if they are integers
# - Takes low, high and question as parameters.
# - Returns input if integer is valid. 


def val_int(low, high, question):
    while True: 
        # - Sets up while True loop.
        try:
            # - Prints question asking for input.
            num = int(input(question))
            # - Asks for integer input.
            if num >= low and num <= high:
                # - If num is between set boundaries, it will return num.
                return num
            else:
                # - If num is outside set boundaries, it prints an error message.
                print(f"Please enter a number between {low} and {high}. ")
        except ValueError:
            # - Prints error message if input is not an integer. 
            print("That is not a valid number.")
            # - Error message.
            print(f"Please enter a number between {low} and {high}. ")
            # - Gives instructions to user. 

# Valdiates input to check if they are alphabetical
# - Takes question as parameter. 
# - Returns response in title class if valid. 


def val_str(question):
    while True:
        # - Sets up while True loop.
        response = input(question)
        # - Asks for string (alphabetical) input.
        x = response.isalpha()
        # - Checks input is alphabetical and sets x to True if alpha. 
        if x == False:
            # - Prints error message if x is False.
            print("This must only contain letters. Please note that the bot does not accept spaces.")
        else:
            return response.title()
            # - Returns response in title class if True.

# Validates input to check if it is between 7 to 10 digits
# - Takes low, high and question as parameters.
# - Returns input if input is an integer between 7 to 10 digits. 


def val_ph(question, ph_low, ph_high):
    while True:
        # - Sets up while True loop.
        try:
            # - Prints question asking for input. 
            num = int(input(question))
            # - Asks for integer input.
            test_num = num
            # - Sets test_num to equal number, 
            # allows program to pull apart the inputted number 
            # and make sure it's a number. 
            count = 0
            while test_num > 0:
                # - Starts another while loop 
                # where test_num is bigger than 0. 
                test_num = test_num//10
                # - test_num is divided by 10 to split up number
                count = count+1
                # - Since count = 0, every digit
                # will be counted to check the number of digits
                # that have been entered.
            if count >= ph_low and count <= ph_high:
                # - If count is between set boundaries, it will return num.
                return num
            else:
                # - If num is outside set boundaries, it prints error message.
                print("New Zealand phone numbers have between 7 to 10 digits. Please note that the bot does not accept spaces.")
                # - Error message.
        except ValueError:
            print("Please enter a number.")
            # - Gives instructions to user.


ph_low = 7
ph_high = 10

# Welcome message with random name generator


def welcome():
    num = randint(0, 9)
    # - Sets num to randint which returns an integer number
    # from a specified range of numbers, 0 to 9 in this case.

    name = (names[num])
    # - Sets name to equal the list of names at the index of 
    # the random numbers. Each word in list has an index number
    # with the first one starting with 0 unless specified. 

    print("  __  __                  _            _      ")
    print(" |  \/  |                (_)          ( )     ")
    print(" | \  / | ___  __ _ _   _ _  __ _ _ __|/ ___  ")
    print(" | |\/| |/ _ \/ _` | | | | |/ _` | '__| / __| ")
    print(" | |  | |  __/ (_| | |_| | | (_| | |    \__ \ ")
    print(" |_|  |_|\___|\__, |\__,_|_|\__,_|_|    |___/ ")
    print("               __/ |                          ")
    print("              |___/                           ")
    # - Prints Meguiar's banner
    print()
    print("Welcome to Meguiar's!")
    # - Prints welcome message
    print("My name is", name,"and "
          "I'll be here to help you order"
          " New Zealand's finest car-care products.")
    # - Prints statement including random name generated
    # and purpose of the bot
    print()

# Menu for click & collect or delivery


def order_type():
    delivery_collect = ""
    # - Sets delivery_collect to empty

    LOW = 1
    HIGH = 2

    question = (f"Enter a number between {LOW} and {HIGH}. ")
    # - Questions asks user to enter a 1 or 2 
    # for click & collect or delivery. 

    print("Is your order for click & collect or delivery?")
    print("For click & collect, please enter 1.")
    print("For delivery, please enter 2.")
    print("Please note that there is a $9.00 delivery surcharge"
          " for orders with less than 5 items.")
    # - Prints statement to inform user to choose between 
    # click & collect or delivery, and that there is a 
    # $9.00 delivery surcharge for orders less than 5 items.

    delivery = val_int(LOW, HIGH, question)
    # - Sets delivery to equal validate input. Sends 
    # input through the function of validate input. Checks 
    # if the input is an integer between set boundaries. 
    if delivery == 1:
        # - If delivery is equal to 1.
        print("Click & Collect")
        # - Prints click & collect statement 
        delivery_collect = "Click & Collect"
        # - Sets delivery_collect to equal click & collect. 
        # Will be used in the order_print statement function.
        collect_info()
        # - Runs click & collect information function. 
    else:
        # - If delivery is not equal to 1.
        print("Delivery")
        # - Prints delivery statement
        delivery_collect = "Delivery"
        # - Sets delivery_collect to equal "delivery" 
        # Will be used in the order_print statement function. 
        delivery_info()
        # - Runs delivery information function. 
    return delivery_collect
    # Returns delivery_collect information back to delivery_collect.

# Click & collect information - name and phone number
# Takes in low, high and question as parameters when sending:
# - to check the string function for name
# - to check the phone function for phone number
# No returns.


def collect_info():
    question = ("Please enter your name. ")
    # - Question asking for name. 
    customer_details['name'] = val_str(question)
    # - Customer name will equal to val_str. Sends input through
    # the function of val_str.
    print(customer_details['name'])
    # - Prints customer name once input is returned from the val_str function. 

    question = ("Please enter your phone number. ")
    # - Question asking for phone number. 
    customer_details['phone'] = val_ph(question, ph_low, ph_high)
    # - Customer phone number will equal to val_ph. Sends input through
    # the function of val_ph. 
    print(customer_details['phone'])
    # - Prints customer's phone number once input is returned from the val_ph function.
    print()
    print("Your Details:")
    print(
        f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    print()
    # - Prints formatted customer details - name and phone number.

# Delivery information - name, phone number and address
# Takes in low, high and question as parameters when sending:
# - to check the string function for name, house number, street and suburb
# - to check the phone function for phone number
# - to validate input function for house number
# No returns. 


def delivery_info():
    question = ("Please enter your name. ")
    # - Question asking for name. 
    customer_details['name'] = val_str(question)
    # - Customer name will equal to val_str. Sends input through
    # the function of val_str.
    print(customer_details['name'])
    # - Prints customer name once input is returned from the val_str function. 

    question = ("Please enter your phone number. ")
    # - Question asking for phone number.
    customer_details['phone'] = val_ph(question, ph_low, ph_high)
    # - Customer phone number will equal to val_ph. Sends input through
    # the function of val_ph. 
    print(customer_details['phone'])
    # - Prints customer's phone number once input is returned from the val_ph function.

    question = ("Please enter your house number. ")
    # - Question asking for house number. 
    customer_details['house'] = not_blank(question)
    # - Customer house number will equal to not_blank. Sends input through
    # the function of not_blank.
    print(customer_details['house'])
    # - Prints customer's house number once input is returned from the not_blank function.

    question = ("Please enter your street name. ")
    # - Question asking for street name. 
    customer_details['street'] = val_str(question)
    # - Customer street name will equal to val_str. Sends input through
    # the function of val_str.
    print(customer_details['street'])
    # - Prints customer's street number once input is returned from the val_str function.

    question = ("Please enter your suburb. ")
    # - Question asking for suburb.
    customer_details['suburb'] = val_str(question)
    # - Customer suburb will equal to val_str. Sends input through
    # the function of val_str.
    print(customer_details['suburb'])
    # - Prints customer's suburb once input is returned from the val_str function.
    print()
    print("Your Details:")
    print(
        f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
        # - Prints formatted customer details - name, phone number, house number, street and suburb.  
    print()

def confirm_details():
    LOW = 1
    HIGH = 2

    print()
    print("Please confirm your details.")
    print("To move on, please enter 1.")
    print("To start again, please enter 2.")
    question = (f"Please enter a number between {LOW} and {HIGH}. ")
    # - Question asks user to enter 1 or 2 if they would like 
    # to confirm or change their details. 

    confirm = val_int(LOW, HIGH, question)
    # - Sets confirm to equal val_int. Sends input through function and 
    # checks if it is an integer and is between set boundaries by 
    # low and high.
    if confirm == 1:
        # - If confirm equals 1. 
        print()
        print("Your details have been confirmed!")
        # - Prints statement to inform user that their details have been confirmed.
        print()
    elif confirm == 2:
        order_list.clear()
        # - Clears data stored in order_list.
        order_cost.clear()
        # - Clears data stored in order_cost.
        customer_details.clear()
        # - Clears customer details dictionary. 
        main()
        # - Opens and runs main function.

# Product menu
# - Prints out list of products with price and index number.
# No parameters, no returns.


def menu():
    number_product = 12
    # - Sets number of products to 12.

    print("--------------------------")
    print("|     Meguiar's Menu      |")
    print("--------------------------")

    for count in range(number_product):
        # - Code counts through 12 times until no numbers are left.
        print("{} {} ${:.2f}" .format(
            count+1, product_names[count], product_prices[count]))
        # - Formats the list into 3 columns,
        # 1. Index number
        # 2. Product name
        # 3. Price formatted with $ sign to 2 decimal places

    print("--------------------------")

# Choose total number of products
# - Product(s) ordered from menu - prints each product with price
# Takes low, high aand question as parameters when sending:
# - To validate integer for number of products ordered 
# Takes menu_low, menu_high, question as parameters when sending:
# - To validate integer for products ordered


def order_products():
    # - Asks for total number of products to order.
    num_products = 0
    # - Sets number of products to 0.
    LOW = 1
    # - Constant used in num_products. 
    HIGH = 25
    # - Constant used in num_products.
    MENU_LOW = 1
    # - Constant used in products_ordered. 
    MENU_HIGH = 12
    # - Constant used in products ordered.

    print()
    print("How many products would you like to order?")
    print("Please note that there is a limit of 25 products each customer.")
    # - Print statement to inform user to order
    # and the 25 product limit.
    question = (f"Please enter a number between {LOW} and {HIGH}. ")
    # - Question including the set boundaries the 
    #   number must be in or equal to.

    num_products = val_int(LOW, HIGH, question)
    # - Sets num_products to equal val_int. Sends input through
    # function and checks if it is an integer and is between
    # set boundaries.

# Choose products from menu
    for item in range(num_products):
        # - Code counts through number of products ordered,
        # meaning it will repeat the same code until there
        # are no numbers remaining.
        while num_products > 0:
            # - Starts while loop where num_products is bigger than 0. 
            print("Please choose your products by entering the number from the menu. ")
            # - Print statement to inform user to choose their products
            question = (
                f"Please enter a number between {MENU_LOW} and {MENU_HIGH}. ")
            # - Question including the set boundaries the 
            # number must be in or equal to.
            products_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            # - Sets num_products to equal val_int. Sends input through
            # function and checks if it is an integer and is between
            # set boundaries by low and high. 
            products_ordered = products_ordered - 1
            # - Sets products_ordered to equal products_ordered - 1,
            # meaning that when a number is inputted, num_products
            # decreases by 1 until it is 0 and the code will 
            # stop repeating.
            order_list.append(product_names[products_ordered])
            # - Appends products name to the order_list 
            # which stores the information.
            order_cost.append(product_prices[products_ordered])
            # - Appends products prices to the order_list 
            # which stores the information.
            [print("{} ${:.2f}" .format(product_names[products_ordered],
                   product_prices[products_ordered]))]
            # - Prints information in two columns:
            # 1. Product name
            # 2. Product price formatted with $ sign to 2 decimal places
            num_products = num_products-1
            # - Sets num_products to equal num_products-1, meaning
            # that when a number is inputted, the num_products 
            # decreases by 1 until it is 0 and the code will stop
            # repeating.

# Prints order out including: 
# - If order is for delivery or click & collect
# - Customer details
# - Name and price of each product - total cost including any delivery surcharge
# Takes delivery_collect as a parameter.
# No returns.

def order_print(delivery_collect):
    print() 
    total_cost = sum(order_cost)
    # Sets total_cost to equal the sum of all prices of products_ordered.
    print("--------------------------")
    print("|    Meguiar's Cart      |")
    print("--------------------------")
    print("Your Details:")
    if delivery_collect == "Click & Collect":
        # - If delivery_collect equals Click & Collect from the order_type 
        # function, it prints the information required.
        print("Your order is for click & collect. You will receive a text message when the products are ready for pickup.")
        # - Print statement to inform user order is for click & collect.
        print(
            f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
        # - Prints customer name and phone number formatted as:
        # Customer Name: Avram
        # Customer Phone: 0224938284
    elif delivery_collect == "Delivery":
        # - If delivery_collect equals Delivery from the order_type 
        # function, it prints the information required.
        print("Your order is for delivery.")
        # - Print statement to inform user order is for delivery.
        print(
            f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
        # - Prints customer name, phone number and address. Formatted like
        # click & collect.
    print()
    print("Your Order Details:")
    count = 0
    # - Sets count to equal 0. 
    for item in order_list:
        # - For each product in the order list.
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        # - Prints infromation in 2 columns: 
        # 1. Product names
        # 2. Product prices formatted with $ sign to 2 decimal places
        count = count+1
        # - Sets count to equal count + 1, meaning as each product
        # is printed, the count will increase until there are no
        # more products left in the order list and they are all printed.
    print()
    if delivery_collect == "Delivery":
        # If delivery_collect equals Delivery
        if len(order_list) >= 5:
            # - If the order_list length is more than 5 index numbers, 
            # a print statement will inform the user that the order will
            # be delivered for free. 
            print("No delivery surcharge is applied.")
        elif len(order_list) < 5:
            # - If the order_list length is less than 5 index numbers, 
            # a print statement will inform the user that the order will
            # have a $9.00 delivery fee. 
            print(
                "Since you ordered less than 5 items, a $9.00 delivery surcharge is applied.")
            total_cost = total_cost+9
            # - Sets total_cost for delivery if the amount of products
            # ordered are less than 5 to equal total_cost + 9, which is 
            # the delivery fee. 
    print()
    print("Total Order Cost:")
    print(f"${total_cost:.2f}")
    print("--------------------------")
    # - Print statement of total cost formatted with $ sign and 2 decimal places.
    print()

# Option to confirm or cancel order
# - Takes in low, high and question as parameters 
# when sending to validate integer input function.
# - No returns.


def cancel_confirm():
    LOW = 1
    HIGH = 2

    print("Please confirm your order.")
    print("To confirm, please enter 1.")
    print("To cancel, please enter 2.")
    question = (f"Please enter a number between {LOW} and {HIGH}. ")
    # - Question asks user to enter 1 or 2 if they would like 
    # to confirm or cancel the order. 

    confirm = val_int(LOW, HIGH, question)
    # - Sets confirm to equal val_int. Sends input through function and 
    # checks if it is an integer and is between set boundaries by 
    # low and high.
    if confirm == 1:
        # - If confirm equals 1. 
        print()
        print("Order confirmed!")
        print("Your products are being prepared in our warehouse.")
        # - Prints statement to inform user that the order has been sent through.
        print()
        order_exit()
    elif confirm == 2:
        # If confirm equals 2. 
        print("Your order has been cancelled.")
        print("You can restart your order or exit the BOT.")
        # - Prints statement to inform user that the order has been cancelled.
        order_exit()
        # Open and runs a new exit function.

# Option to order again or exit the bot
# - Takes low, high and question as parameter
# when sending to validate integer input function.
# - No returns.


def order_exit():
    LOW = 1
    HIGH = 2
    question = (f"Please enter a number between {LOW} and {HIGH}. ")
    # - Question asks user to enter 1 or 2 if they would like to 
    # place a new order or exit the bot.

    print("Would you like to order again or exit?")
    print("To order again, please enter 1.")
    print("To exit the BOT, please enter 2.")

    confirm = val_int(LOW, HIGH, question)
    # Sets confirm to equal val_int. Sends input through function and
    # checks if it is an integer and is between set boundaries by 
    # low and high. 
    if confirm == 1:
        # - If confirm equals 1.
        print("New Order:")
        order_list.clear()
        # - Clears data stored in order_list.
        order_cost.clear()
        # - Clears data stored in order_cost.
        customer_details.clear()
        # - Clears customer details dictionary. 
        main()
        # - Opens and runs main function.
    elif confirm == 2:
        # - If confirm equals 2.
        print("Thank you for visiting Meguiar's!")
        print("Exiting...")
        order_list.clear
        # - Clears data stored in order_list.
        order_cost.clear()
        # - Clears data stored in order_cost.
        customer_details.clear
        # - Clears customer details dictionary.
        sys.exit()
        # - Uses sys module to exit program.

# Main function
# - No parameters, no returns.

def main():
    welcome()
    # - Welcome function.
    delivery_collect = order_type()
    # Order type function:
    # - runs click & collect or delivery function
    # depending on users choice.
    print("Order Type:",delivery_collect)
    confirm_details()
    # - Print statement for order type.
    menu()
    # - List function.
    order_products()
    # - Order products function.
    order_print(delivery_collect)
    # - Print order function.
    cancel_confirm()
    # Confirm or cancel order function:
    # - runs new order or exit function.


main()
# - Main function, runs the entire program.
