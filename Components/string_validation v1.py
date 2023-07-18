question = "Please enter your name. "

while True:
    response = input(question)
    x = response.isalpha()
    if x == False:
        print("This must only contain letters.")
    else:
        print(response.title())
        break


    