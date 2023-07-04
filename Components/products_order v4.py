# List of products names
product_names = ['Wash Mitt','Wheel & Tire Cleaner (710ml)','Leather Cleaner/Conditioner (450ml)','Wash & Wax (1.7L)','Snow Foam (1.9L)','Wheel Brush','Ultimate Compound (450ml)','Glass Cleaner (710ml)','Microfibre Towel (3 pack)','Foam Applicator Pads (2 pack)','Headlight Restoration Kit','Cleaner Wax Paste (311g)']

# List of products prices 
product_prices = [34.99, 33.99, 39.99, 66.99, 97.19, 22.99, 48.50, 23.99, 32.99, 10.99, 67.99, 46.95]

# List to store ordered products 
order_list = []

# List to store products prices
order_cost = []

# List to store order cost 

def menu():
    number_product = 12

    for count in range(number_product):
        print("{} {} ${:.2f}" .format(count+1, product_names[count], product_prices[count]))
        
menu()

# Ask for a total number of products for order
num_products = 0

def order_products():
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

    # Choose product from menu
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

menu()
order_products()



