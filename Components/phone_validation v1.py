question = ("Please enter your phone number. ")

ph_low = 7
ph_high = 10

while True:
    try:
        num = int(input(question))
        test_num = num
        count = 0
        while test_num > 0:
            test_num = test_num//10
            count = count+1
        if count >= ph_low and count <= ph_high:
            print(num)
            break
        else:
            print("New Zealand phone numbers have between 7 to 10 digits.")
    except ValueError:
            print("Please enter a number.")



