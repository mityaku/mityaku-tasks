#input a number from the user
num = int(input("Enter a number between 1 and 10: "))

#checks if the input is within the valid range
if num < 1 or num > 10:
    print("Number must be between 1 and 10.")
else:
    #outputs the first 10 values of the times table
    print(f"{num}'s times table:")
    for i in range(1, 11):
        result = num * i
        print(result, end=" ")
