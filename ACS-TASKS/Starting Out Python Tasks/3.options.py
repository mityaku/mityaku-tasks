while True:
    option = int(input("Enter an option (1, 2, or 3): "))
    if option >= 1 and option <= 3:
        print("You have selected option number", option)
        break
    else:
        print("Number must be between 1 and 3. Please try again.")
