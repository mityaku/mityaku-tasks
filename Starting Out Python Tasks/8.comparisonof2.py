#input two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

#creates a list with the two integers
numbers = [num1, num2]

#sorts the list in descending order
numbers.sort(reverse=True)

#output the sorted integers
print("Sorted integers (highest first):", numbers)
