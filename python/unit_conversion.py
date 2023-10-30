# 1.print all the convertions
# 2.user choice
# 3.convertion with conditional statements


while True:
    convertions = {
        1: "Kilometers to miles",
        2: "Miles to kilometers",
        3: "Kilograms to pounds",
        4: "Pounds to kilograms",
        5: "Celsius to Fahrenheit",
        6: "Fahrenheit to Celsius",
        7: "Exit",
    }

    print("Unit Conversion Tool")
    for k, v in convertions.items():
        print(f"{k}.{v}")

    user_choice = int(input("Enter choice within 1 -7 : "))

    if user_choice == 1:
        kilometers = float(input("Enter distance in kilometers= "))
        miles = kilometers * 0.621
        print(f"Value in miles = {miles}")
    elif user_choice == 2:
        miles = float(input("Enter the distance in miles = "))
        kilometers = miles * 1.609
        print(f"Value in kilometers = {kilometers}")
    elif user_choice == 3:
        kilogram = float(input("Enter the weight in kilograms = "))
        pound = kilogram * 2.205
        print(f"Value in pound = {pound}")

    elif user_choice == 4:
        pound = float(input("Enter the weight in pound = "))
        kilogram = pound * 0.454
        print(f"Value in kilogram = {kilogram}")

    elif user_choice == 5:
        celsius = float(input("Enter the temperature in Celsius = "))
        farenheit = (celsius * (9 / 5)) + 32
        print(f"Value in Farenheit = {farenheit}")

    elif user_choice == 6:
        farenheit = float(input("Enter the temperature in farenheit = "))
        celsius = (5 / 9) * (farenheit - 32)
        print(f"Value in Celsius = {celsius}")
    elif user_choice == 7:
        print("Exiting the Unit Conversion Tool. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1 - 7).\n")
        break
