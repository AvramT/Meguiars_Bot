# List of products names
product_names = ['Wash Mitt','Wheel & Tire Cleaner (710ml)','Leather Cleaner/Conditioner (450ml)','Wash & Wax (1.7L)','Snow Foam (1.9L)','Wheel Brush','Ultimate Compound (450ml)','Glass Cleaner (710ml)','Microfibre Towel (3 pack)','Foam Applicator Pads (2 pack)','Headlight Restoration Kit','Cleaner Wax Paste (311g)']

# List of pizza prices 
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

num_products = int(input("How many products do you want to order? "))

print(num_products)

# Choose products from menu
print("Please choose your products by entering the number from the menu. ")
for item in range(num_products):
    while num_products > 0:
        products_ordered = int(input())
        products_ordered = products_ordered-1
        order_list.append(product_names[products_ordered])
        order_cost.append(product_prices[products_ordered])
        num_products = num_products-1

print(order_list)
print(order_cost)


