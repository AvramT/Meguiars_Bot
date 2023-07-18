import sys
import random
from random import randint

# List of random names
names = ["Patrick", "Sonia", "Ricky", "Veronica", "Gary", "Louis", "Mary", "Ed", "Jose", "Carlos"]

# List of product names
product_names = ['Wash Mitt','Wheel & Tire Cleaner (710ml)','Leather Cleaner/Conditioner (450ml)','Wash & Wax (1.7L)','Snow Foam (1.9L)','Wheel Brush','Ultimate Compound (450ml)','Glass Cleaner (710ml)','Microfibre Towel (3 pack)','Foam Applicator Pads (2 pack)','Headlight Restoration Kit','Cleaner Wax Paste (311g)']

# List of product prices
product_prices = [34.99, 33.99, 39.99, 66.99, 97.19, 22.99, 48.50, 23.99, 32.99, 10.99, 67.99, 46.95]

# List to store ordered products 
order_list = []

# List to store products prices
order_cost = []

# Customer details dictionary
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
def val_int(low, high, question):
    while True:
        try: 
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high}. ")
        except ValueError:
            print("That is not a valid number.")
            print(f"Please enter a number between {low} and {high}. ")

# Welcome message with random name generator
def welcome():
    num = randint(0,9)

    name = (names[num])

    print("*** Welcome to Meguiar's! ***")
    print("*** My name is",name,"***")
    print("*** I'll be here to help you order New Zealand's finest car-care products. ***")

# Menu for click & collect or delivery
def order_type():
    delivery_collect = ""

    LOW = 1
    HIGH = 2
    
    question = (f"Enter a number between {LOW} and {HIGH}. ")

    print("Is your order for click & collect or delivery?")
    print("For click & collect, please enter 1.")
    print("For delivery, please enter 2.")

    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print ("Click & Collect")
        del_pick = "Click & Collect"
        collect_info()
    else:
        print ("Delivery")
        delivery_info()
        del_pick = "Delivery"
    return delivery_collect

# Click & collect information - name and phone number
def collect_info():
    question = ("Please enter your name. ")
    customer_details['name'] = not_blank(question )
    #print(customer_details['name'])

    question = ("Please enter your phone number. ")
    customer_details['phone'] = not_blank(question )
    #print(customer_details['phone'])
    print(customer_details)

# Delivery information - name, phone number and address
def delivery_info():
    question = ("Please enter your name. ")
    customer_details['name'] = not_blank(question )
    #print(customer_details['name'])

    question = ("Please enter your phone number. ")
    customer_details['phone'] = not_blank(question )
    #print(customer_details['phone'])

    question = ("Please enter your house number. ")
    customer_details['house'] = not_blank(question )
    print(customer_details['house'])

    question = ("Please enter your street name. ")
    customer_details['street'] = not_blank(question )
    print(customer_details['street'])

    question = ("Please enter your suburb. ")
    customer_details['suburb'] = not_blank(question )
    print(customer_details['suburb'])
    print(customer_details)

# Product menu
def menu():
    number_product = 12

    for count in range(number_product):
        print("{} {} ${:.2f}" .format(count+1, product_names[count], product_prices[count]))

# Choose total number of products
def order_products():
    num_products = 0

    LOW = 1
    HIGH = float('inf')
    MENU_LOW = 1
    MENU_HIGH = 12

    question = (f"Please enter a number between {LOW} and {HIGH}. ")
    
    print("How many products would you like to order?")

    num_products = val_int(LOW, HIGH, question)

# Choose products from menu
    for item in range(num_products):
        while num_products > 0:
            print("Please choose your products by entering the number from the menu. ")
            question = (f"Please enter a number between {MENU_LOW} and {MENU_HIGH}. ")
            products_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            products_ordered = products_ordered -1
            order_list.append(product_names[products_ordered])
            order_cost.append(product_prices[products_ordered])
            [print("{} ${:.2f}" .format(product_names[products_ordered],product_prices[products_ordered]))]
            num_products = num_products-1

# Prints order out including: - if order is delivered or collected up - name and price of each product - total cost including a $9 delivery charge if less than 5 items ordered
def order_print(delivery_collect):
    print()
    total_cost = sum(order_cost)
    print("Your Details:")
    if delivery_collect == "Click & Collect":
        print("Your order is for click & collect. You will receive a text message when the products are ready for pickup.")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif delivery_collect == "Delivery":
        print("Your order is for delivery.")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details:")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    if delivery_collect == "Delivery" :
        if len(order_list) >= 5:
            print("No delivery surcharge is applied.")
        elif len(order_list) < 5:
            print("Since you ordered less than 5 items, a $9.00 delivery surcharge is applied.")
            total_cost = total_cost+9
    print("Total Order Cost:")
    print(f"${total_cost:.2f}")

# Option to confirm or cancel order

def cancel_confirm():
    LOW = 1
    HIGH = 2
    question = (f"Please enter a number between {LOW} and {HIGH}. ")

    print ("Please confirm your order.")
    print ("To confirm, please enter 1.")
    print ("To cancel, please enter 2.")

    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
            print("Order confirmed!")
            print("Your order has been sent to our kitchen.")
            print("Your delicious pizza will be with your shortly.")
            order_exit()
    elif confirm == 2:
        print("Your order has been cancelled.")
        print("You can restart your order or exit the BOT.")
        order_exit()

# Option to order again or exit the bot
def order_exit():
    LOW = 1
    HIGH = 2
    question = (f"Please enter a number between {LOW} and {HIGH}. ")

    print ("Would you like to order again or exit?")
    print ("To order again, please enter 1.")
    print ("To exit the BOT, please enter 2.")

    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
            print("New Order:")
            order_list.clear()
            order_cost.clear()
            customer_details.clear()
            main()
    elif confirm == 2:
        print("Exiting...")
        order_list.clear
        order_cost.clear()
        customer_details.clear
        sys.exit()

# Main function
def main():
    welcome()
    delivery_collect = order_type()
    print(delivery_collect)
    menu()
    order_products()
    order_print(delivery_collect)
    cancel_confirm()
    
main()



