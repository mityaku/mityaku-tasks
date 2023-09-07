num = int(input("Enter an integer between 100 and 999: "))

if num < 100 or num > 999:
    print("Number must be between 100 and 999.")
else:
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10

    print(f"{hundreds} hundreds, {tens} tens, and {units} units.")
