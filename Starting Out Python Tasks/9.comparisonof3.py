#input three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

#creates a list with the three integers
numbers = [num1, num2, num3]

#sorts the list in descending order
numbers.sort(reverse=True)

#output the sorted integers
print("Sorted integers (highest first):", numbers)
