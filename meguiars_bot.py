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
                    collect_info()
                    break

                elif delivery == 2:
                    print("Delivery")
                    delivery_info()
                    break
            else:
                print("The number must be 1 or 2.")
        except ValueError:
            print("That is not a valid number.")
            print("Please enter 1 or 2.")

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
    
    while True:
        try:
            num_products = int(input("How many products would you like to order? "))
            if num_products >= 1 and num_products <= float('inf'):
                break
            else:
                print("You cannot have a negative number.")
        except ValueError:
            print("That is not a valid number. ")
            print("Please enter a minimum order quantity of 1.")

    for item in range(num_products):
        while num_products > 0:
            while True:
                try:
                    products_ordered = int(input("Please choose your products by entering the number from the menu. "))
                    if products_ordered >= 1 and products_ordered <= 12:
                        break
                    else:
                        print("Your order must be between 1 and 12. ")
                except ValueError:
                    print("That is not a valid number. ")
                    print("Please enter a number between 1 or 12. ")
            products_ordered = products_ordered -1
            order_list.append(product_names[products_ordered])
            order_cost.append(product_prices[products_ordered])
            [print("{} ${:.2f}" .format(product_names[products_ordered],product_prices[products_ordered]))]
            num_products = num_products-1

# Main function
def main():
    welcome()
    order_type()
    menu()
    order_products()
    
main()


