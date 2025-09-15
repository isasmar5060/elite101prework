print("Welcome to the Walmart Chatbot!")
name = input("What is your name? ")
age = int(input("Hello " + name + ", how old are you in years? "))

if age < 9:
    print(str(age) + "? That's so cool!")
    print("To use the chatbot, I'd recommend that you get a parent to help first. See you later!")
else:
    query = input(str(age) + "? Great! Would you like an itemized list of my capabilities, " + name + "? (Y/N) ")

    if query.lower() == "y":
        print("Great! Here it is:")
        print("Press 1 for how to find your nearest Walmart store.")
        print("Press 2 to search for an item in the catalog.")
        print("Press 3 to report a damaged product in-store.")
        print("Press 4 for contact information for your selected store.")
        print("Press 5 to exit the chatbot.")
        
        choice = int(input("Please enter a number from 1 to 5."))
        if choice == 1:
            print("words words words")
        elif choice == 2:
            print("words words words 2")
        elif choice == 3:
            print ("words words words 3")
        elif choice == 4:
            print("words words words 4")
        elif choice == 5:
            print ("Thank you for talking to me, see you!")
        
    elif query.lower() == "n":
        print("Thank you for your participation! Exiting the program now.")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
